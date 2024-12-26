from abc import ABC, abstractmethod
from errors import index_error, value_error


class Checkbox(ABC):
    checkbox_es: int = 0
    created_checkboxes: int = 0

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsCheckbox(Checkbox):
    def create_checkbox(self) -> int:
        while True:
            try:
                self.checkbox_es = int(input('How many create checkboxes for Windows?: '))
                if self.checkbox_es <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_checkboxes = self.checkbox_es
                return self.created_checkboxes
            except ValueError:
                print(f'\n{value_error}\n')


class MacOSCheckbox(Checkbox):
    def create_checkbox(self) -> int:
        while True:
            try:
                self.checkbox_es = int(input('How many create checkboxes for MacOS?: '))
                if self.checkbox_es <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_checkboxes = self.checkbox_es
                return self.created_checkboxes
            except ValueError:
                print(f'\n{value_error}\n')


class LinuxCheckbox(Checkbox):
    def create_checkbox(self) -> int:
        while True:
            try:
                self.checkbox_es = int(input('How many create checkboxes for Linux?: '))
                if self.checkbox_es <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_checkboxes = self.checkbox_es
                return self.created_checkboxes
            except ValueError:
                print(f'\n{value_error}\n')
