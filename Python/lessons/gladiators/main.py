import uvicorn
from fastapi import FastAPI
from classes import *
from functions import *

app = FastAPI()


@app.get("/")
async def check() -> str:
    return "checking..."


@app.post("/api/characters")
async def create_character(name: dict) -> Character:
    char = Character(name=name["name"])
    characters.append(char)
    return char


@app.get("/api/characters/{id}")
async def get_character(id: int) -> Character:
    return get_char(id)


@app.put("/api/characters/{id}/attributes")
async def adjust_character_attributes(id: int, upgrade: dict) -> dict:
    char = get_char(id)

    amount_pt = upgrade["agility"] + upgrade["stamina"] + upgrade["strength"]
    if not amount_pt <= char.availablePoints:
        raise HTTPException

    # Обновление навыков
    char.strength += upgrade["strength"]
    char.agility += upgrade["agility"]
    char.stamina += upgrade["stamina"]
    char.availablePoints -= amount_pt

    return dict(char)


@app.post("/api/lobbies")
async def create_lobby():
    lobby = Lobby()
    lobbies[len(lobbies) + 1] = lobby
    return lobby


@app.post("/api/lobbies/{lobbyId}/join")
async def join_lobby(lobbyId: int, char_id: dict):
    # Поиск лобби
    lobby = get_lobby(lobbyId)

    # Поиск персонажа
    character = get_char(char_id["characterId"])

    # Подключение персонажа в лобби
    if character in lobby.players:
        raise HTTPException
    lobbies[lobbyId].players.append(character)

    return lobby


@app.post("/api/lobbies/{lobbyId}/fights")
def start_fight(lobbyId: int):
    lobby = get_lobby(lobbyId)

    char = lobby.players[0]

    bot = Bot()
    bots.append(bot)

    fight = Fight(player_turn=True, playerId=char.id, botId=bot.id, lobbyId=lobbyId)
    fights.append(dict(fight))

    return fight


@app.post("/api/fights/{fightId}/moves")
def make_move(fightId: int, attack: AttackParam, block1: AttackParam, block2: AttackParam):
    fight = get_fight(fightId)

    # Получение персонажа и бота
    char: Character = get_char(fight.get("playerId"))
    bot = get_bot(fight.get("botId"))

    # Ход бота
    bot_block = bot.block()
    bot_attack = bot.attack()

    ###
    playerHit = False
    opponentHit = False
    char_damage = 0
    bot_damage = 0
    ###

    # Итоги
    if not (attack in bot_block or (random() > 1 - min(0.3, bot.agility / 100))):
        char_damage = char.strength * (1.5 if random() > 1 - min(0.4, char.agility) else 1)
        bot.stamina -= char_damage
        playerHit = True
    if not (bot_attack in [block1, block2] or (random() > 1 - min(0.3, char.agility / 100))):
        bot_damage = bot.strength * (1.5 if random() > 1 - min(0.4, bot.agility) else 1)
        char.stamina -= bot_damage
        opponentHit = True

    return Move(
        playerHit=playerHit,
        opponentHit=opponentHit,
        playerDamageDealt=char_damage,
        opponentDamageDealt=bot_damage,
        playerHealth=char.stamina,
        opponentHealth=bot.stamina
    )


if __name__ == "__main__":
    uvicorn.run(app)
