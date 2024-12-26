from http.client import HTTPException
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from random import sample, choice, randint, random
from enum import Enum

app = FastAPI()

characters = [
    # {"id": 1, "name": "Vasya", "strength": 0, "agility": 0, "stamina": 0, "level": 1, "availablePoints": 5}
]

bots = [
]

lobbies = {  # 1: {"players": [
    #     {"id": 1, "name": "Vasya", "strength": 0, "agility": 0, "stamina": 0, "level": 1, "availablePoints": 5},
    # ]}
}

fights = [
    # {"fightId": 1, "player_turn": True, "playerId": 1, "botId": 2, "lobbyId": 1}
]


def return_obj(obj):
    if len(obj) > 0:
        return obj[0]
    raise HTTPException


def get_char(Id: int):
    char = [char for char in characters if char.id == Id]
    return return_obj(char)


def get_lobby(id: int):
    lobby = lobbies.get(id)
    if lobby:
        return lobby
    raise HTTPException


def get_fight(id: int):
    fight = [f for f in fights if f.get("fightId") == id]
    return return_obj(fight)


def get_bot(id: int):
    bot = [b for b in bots if b.id == id]
    return return_obj(bot)


class Character(BaseModel):
    id: int = len(characters) + 1
    name: str = None
    strength: int = 0
    agility: int = 0
    stamina: int = 0
    level: int = 1
    availablePoints: int = 10


class Bot:
    id: int = len(bots) + 1
    name: str = "Bot"
    level: int = 1
    strength: int = randint(1, level * 5)
    agility: int = randint(1, level * 5)
    stamina: int = randint(1, level * 5)
    hit_places = ['head', 'chest', 'groin', 'feet']

    def attack(self):
        return choice(self.hit_places)

    def block(self):
        return sample(self.hit_places, 2)


class Lobby(BaseModel):
    lobbyId: int = len(lobbies) + 1
    players: list = []


class AttackParam(str, Enum):
    head = 'head'
    chest = 'chest'
    groin = 'groin'
    feet = 'feet'


class Fight(BaseModel):
    fightId: int = len(fights) + 1
    player_turn: bool
    playerId: int
    botId: int
    lobbyId: int


class Move(BaseModel):
    playerHit: bool
    opponentHit: bool
    playerDamageDealt: int
    opponentDamageDealt: int
    playerHealth: int
    opponentHealth: int


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
