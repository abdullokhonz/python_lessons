from abc import ABC, abstractmethod
from button import WindowsButton, MacOSButton, LinuxButton
from checkbox import WindowsCheckbox, MacOSCheckbox, LinuxCheckbox
from text_field import WindowsTextField, MacOSTextField, LinuxTextField


class GUIFactory(ABC):
    buttons: int = 0
    checkboxes: int = 0
    text_fields: int = 0

    @abstractmethod
    def get_button(self):
        pass

    @abstractmethod
    def get_checkbox(self):
        pass

    @abstractmethod
    def get_text_field(self):
        pass

    @abstractmethod
    def return_buttons(self):
        pass

    @abstractmethod
    def return_checkboxes(self):
        pass

    @abstractmethod
    def return_text_fields(self):
        pass


class WindowsFactory(GUIFactory):
    def get_button(self) -> str:
        self.buttons += WindowsButton.create_button(self)
        return 'Windows buttons created and received!\n'

    def get_checkbox(self) -> str:
        self.checkboxes += WindowsCheckbox.create_checkbox(self)
        return 'Windows checkboxes created and received!\n'

    def get_text_field(self) -> str:
        self.text_fields += WindowsTextField.create_text_field(self)
        return 'Windows text fields created and received!\n'

    def return_buttons(self) -> str:
        return f'Windows buttons: {self.buttons}'

    def return_checkboxes(self) -> str:
        return f'Windows checkboxes: {self.checkboxes}'

    def return_text_fields(self) -> str:
        return f'Windows text fields: {self.text_fields}'


class MacOSFactory(GUIFactory):
    def get_button(self) -> str:
        self.buttons += MacOSButton.create_button(self)
        return 'MacOS buttons created and received!\n'

    def get_checkbox(self) -> str:
        self.checkboxes += MacOSCheckbox.create_checkbox(self)
        return 'MacOS checkboxes created and received!\n'

    def get_text_field(self) -> str:
        self.text_fields += MacOSTextField.create_text_field(self)
        return 'MacOS text fields created and received!\n'

    def return_buttons(self) -> str:
        return f'MacOS buttons: {self.buttons}'

    def return_checkboxes(self) -> str:
        return f'MacOS checkboxes: {self.checkboxes}'

    def return_text_fields(self) -> str:
        return f'MacOS text fields: {self.text_fields}'


class LinuxFactory(GUIFactory):
    def get_button(self) -> str:
        self.buttons += LinuxButton.create_button(self)
        return 'Linux buttons created and received!\n'

    def get_checkbox(self) -> str:
        self.checkboxes += LinuxCheckbox.create_checkbox(self)
        return 'Linux checkboxes created and received!\n'

    def get_text_field(self) -> str:
        self.text_fields += LinuxTextField.create_text_field(self)
        return 'Linux text fields created and received!\n'

    def return_buttons(self) -> str:
        return f'Linux buttons: {self.buttons}'

    def return_checkboxes(self) -> str:
        return f'Linux checkboxes: {self.checkboxes}'

    def return_text_fields(self) -> str:
        return f'Linux text fields: {self.text_fields}'
