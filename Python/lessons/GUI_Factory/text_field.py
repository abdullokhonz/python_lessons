from abc import ABC, abstractmethod
from errors import index_error, value_error


class TextField(ABC):
    text_field_s: int = 0
    created_text_fields: int = 0

    @abstractmethod
    def create_text_field(self):
        pass


class WindowsTextField(TextField):
    def create_text_field(self) -> int:
        while True:
            try:
                self.text_field_s = int(input('How many create text fields for Windows?: '))
                if self.text_field_s <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_text_fields = self.text_field_s
                return self.created_text_fields
            except ValueError:
                print(f'\n{value_error}\n')


class MacOSTextField(TextField):
    def create_text_field(self) -> int:
        while True:
            try:
                self.text_field_s = int(input('How many create text fields for MacOS?: '))
                if self.text_field_s <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_text_fields = self.text_field_s
                return self.created_text_fields
            except ValueError:
                print(f'\n{value_error}\n')


class LinuxTextField(TextField):
    def create_text_field(self) -> int:
        while True:
            try:
                self.text_field_s = int(input('How many create text fields for Linux?: '))
                if self.text_field_s <= 0:
                    print(f'\n{index_error}\n')
                    continue
                self.created_text_fields = self.text_field_s
                return self.created_text_fields
            except ValueError:
                print(f'\n{value_error}\n')
