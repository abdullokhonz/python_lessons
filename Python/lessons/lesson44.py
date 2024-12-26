from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name: str, health: int, strength: int):
        self.name, self.health, self.strength = name, health, strength

    @abstractmethod
    def attack(self):
        pass

    def characteristic(self):
        return f'Характеристика персонажа:\nName: {self.name}, Health: {self.health}, Strength: {self.strength}.'


class Warrior(Character):
    def attack(self):
        return 'Атака персонажа: Удар мечом.'


class Mage(Character):
    def attack(self):
        return 'Атака персонажа: Огненный шар.'


class Rogue(Character):
    def attack(self):
        return 'Атака персонажа: Выстрел арбалетом.'


class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self, name: str, health: int, strength: int):
        pass


class WarriorFactory(CharacterFactory):
    def create_character(self, name: str, health: int, strength: int):
        return Warrior(name, health, strength)


class MageFactory(CharacterFactory):
    def create_character(self, name: str, health: int, strength: int):
        return Mage(name, health, strength)


class RogueFactory(CharacterFactory):
    def create_character(self, name: str, health: int, strength: int):
        return Rogue(name, health, strength)


change_character = int(input('Персонажи:\n1. Warrior\n2. Mage\n3. Rogue\nВыберите персонажа: '))

character_factory = WarriorFactory() if change_character == 1 else \
    MageFactory() if change_character == 2 else \
    RogueFactory() if change_character == 3 else None

character = character_factory.create_character(input('Имя персонажа: '), int(input('Здоровье персонажа: ')),
                                               int(input('Сила персонажа: ')))

print(character.attack())
print(character.characteristic())
