from http.client import HTTPException
from lists import *


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
