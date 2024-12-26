from pydantic import BaseModel
from random import sample, choice, randint, random
from enum import Enum
from lists import *


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
