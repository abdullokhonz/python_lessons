from tkinter import Tk


def screen_size() -> Tk.winfo_screen:
    root: Tk = Tk()

    screen_width: float = root.winfo_screenwidth()
    screen_height: float = root.winfo_screenheight()

    root.destroy()

    screen_width: int = 800 if screen_width > 800 else screen_width
    screen_height: int = 800 if screen_height > 800 else screen_height

    return screen_width, screen_height
