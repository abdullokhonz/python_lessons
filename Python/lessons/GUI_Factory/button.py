from abc import ABC, abstractmethod
from errors import index_error, value_error


class Button(ABC):
    button_s: int = 0
    created_buttons: int = 0

    @abstractmethod
    def create_button(self):
        pass


class WindowsButton(Button):
    def create_button(self) -> int:
        while True:
            try:
                self.button_s = int(input('How many create buttons for Windows?: '))
                if self.button_s <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_buttons = self.button_s
                return self.created_buttons
            except ValueError:
                print(f'\n{value_error}\n')


class MacOSButton(Button):
    def create_button(self) -> int:
        while True:
            try:
                self.button_s = int(input('How many create buttons for MacOS?: '))
                if self.button_s <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_buttons = self.button_s
                return self.created_buttons
            except ValueError:
                print(f'\n{value_error}\n')


class LinuxButton(Button):
    def create_button(self) -> int:
        while True:
            try:
                self.button_s = int(input('How many create buttons for Linux?: '))
                if self.button_s <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_buttons = self.button_s
                return self.created_buttons
            except ValueError:
                print(f'\n{value_error}\n')
