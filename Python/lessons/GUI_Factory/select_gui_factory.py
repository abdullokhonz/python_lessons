from gui_factory import WindowsFactory, MacOSFactory, LinuxFactory
from errors import index_error, value_error


def select_gui_factory():
    gui_factories: list = [WindowsFactory(), MacOSFactory(), LinuxFactory()]
    select: int
    selected_gui_factory: gui_factories
    while True:
        try:
            select = int(input('1. Windows Factory\n2. MacOS Factory\n3. Linux Factory\nSelect GUI Factory: '))
            if select <= 0:
                print(f'\n{index_error}\n')
                continue
            selected_gui_factory = gui_factories[select - 1]
            return selected_gui_factory
        except IndexError:
            print(f'\n{index_error}\n')
        except ValueError:
            print(f'\n{value_error}\n')
