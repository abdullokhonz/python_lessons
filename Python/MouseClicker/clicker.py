# import: Библиотеки
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from keyboard import add_hotkey, remove_hotkey
from mouse import click
from time import sleep
from threading import Thread
from json import load, dump


def save_settings(user_settings) -> None:
    with open("resources/settings.json", "w", encoding="utf-8") as file:
        dump(user_settings, file)


def load_settings() -> dict:
    try:
        with open("resources/settings.json", "r", encoding="utf-8") as file:
            return load(file)
    except FileNotFoundError:
        return {"click_speed": .01, "mouse_button": "left", "selected_hotkey": "Z", "lang": "ru"}


# name: type = data: Переменные
settings: dict = load_settings()
click_speed: float = float(settings['click_speed'])
is_clicking: bool = False
click_thread: None = None
selected_mouse_btn: str = settings['selected_mouse_btn']
selected_hotkey: str = settings['selected_hotkey']
lmb_clicks: int = 0
rmb_clicks: int = 0
selected_lang: str = settings['lang']


# def: Функции
def load_language(langs) -> dict:
    with open(f"resources/lang/{langs}.json", "r", encoding="utf-8") as file:
        langs = load(file)
        return langs


lang: dict = load_language(selected_lang)


def change_lang() -> None:
    def save_lang() -> None:
        settings['lang'] = select_lang.get()
        save_settings(settings)
        window_change_lang.grab_release()
        window_change_lang.destroy()
        messagebox.showwarning(f'{lang['warning']}', f'{lang['show_warning']}')
        finish()

    # Tk: Создание и настройка окна
    window_change_lang: Toplevel = Toplevel()
    window_change_lang.geometry('350x150+575+300')
    window_change_lang.resizable(False, False)
    window_change_lang.title(f'{lang['change_lang']}')

    # Radiobutton: Выбор языка
    en, ru = 'en', 'ru'
    select_lang: StringVar = StringVar(value=settings['lang'])
    rad_en: ttk.Radiobutton = ttk.Radiobutton(window_change_lang, text=f'{lang['en']}', value=en, variable=select_lang)
    rad_ru: ttk.Radiobutton = ttk.Radiobutton(window_change_lang, text=f'{lang['ru']}', value=ru, variable=select_lang)
    rad_en.place(x=50, y=50)
    rad_ru.place(x=200, y=50)

    # Button: Сохранить
    btn_save_lang: ttk.Button = ttk.Button(window_change_lang, text=f'{lang['save']}', command=save_lang)
    btn_save_lang.place(width=80, height=30, x=150, y=112)

    # Buttob: Отмена
    btn_cancel_lang: ttk.Button = ttk.Button(window_change_lang, text=f'{lang['cancel']}',
                                             command=lambda: (
                                                 window_change_lang.grab_release(), window_change_lang.destroy())
                                             )
    btn_cancel_lang.place(width=80, height=30, x=250, y=112)

    window_change_lang.grab_set()
    window_change_lang.mainloop()


def change_hotkey() -> None:
    def select_hotkey(word) -> None:
        hotkey.set(value=word)
        window_change_hotkey.grab_release()
        window_change_hotkey.destroy()

    # Tk: Создание и настройка окна
    window_change_hotkey: Toplevel = Toplevel()
    window_change_hotkey.geometry('450x225+525+250')
    window_change_hotkey.resizable(False, False)
    window_change_hotkey.title(f'{lang['change_hotkey']}')

    # Настройка столбцов и строк сетки
    for c in range(5):
        window_change_hotkey.columnconfigure(index=c, weight=1,
                                             minsize=75)  # Минимальный размер для равномерного распределения
    for r in range(6):
        window_change_hotkey.rowconfigure(index=r, weight=1,
                                          minsize=45)  # Минимальный размер для равномерного распределения

    # Создание кнопок
    w: int = 65
    for r in range(5):
        for c in range(6):
            if w <= 90:
                btn_hotkey = ttk.Button(window_change_hotkey, text=chr(w), width=8,
                                        command=lambda word=chr(w): select_hotkey(word))
                btn_hotkey.grid(row=r, column=c, sticky="nsew", padx=8,
                                pady=8)  # "nsew" для равномерного распределения по ячейке
                w += 1
            else:
                break

    # Отключение автоматической подгонки сетки
    window_change_hotkey.grid_propagate(False)

    # Button: Отмена
    btn_cancel_hotkey: ttk.Button = ttk.Button(window_change_hotkey, text=f'{lang['cancel']}',
                                               command=lambda: (
                                                   window_change_hotkey.grab_release(), window_change_hotkey.destroy())
                                               )
    btn_cancel_hotkey.place(width=80, height=30, x=362, y=187)

    window_change_hotkey.grab_set()
    window_change_hotkey.mainloop()


def set_clicker() -> None:
    global is_clicking, click_thread
    is_clicking = not is_clicking
    if is_clicking:
        btn_change_lang['state'] = 'disabled'
        btn_change_hotkey['state'] = 'disabled'
        btn_apply['state'] = 'disabled'
        btn_exit['state'] = 'disabled'
        click_thread = Thread(target=clicking)
        click_thread.start()
    else:
        if click_thread:
            btn_change_lang['state'] = 'enabled'
            btn_change_hotkey['state'] = 'enabled'
            btn_apply['state'] = 'enabled'
            btn_exit['state'] = 'enabled'
            click_thread.join()  # Ожидаем завершения потока
            click_thread = None


def clicking() -> None:
    while is_clicking:
        click(button=selected_mouse_btn)
        sleep(click_speed)


add_hotkey(f'Alt + {selected_hotkey}', set_clicker)


def validate_input(char) -> bool:
    if char.isdigit():
        return True
    elif char == '.' and '.' not in ent_click_speed.get():
        return True
    else:
        return False


def apply() -> None:
    global click_speed, selected_mouse_btn, selected_hotkey
    if float(ent_click_speed.get()) < .01:
        messagebox.showerror(f'{lang['error']}', f'{lang['show_error']}')
    else:
        remove_hotkey(f'Alt + {selected_hotkey}')
        save_settings(settings)
        messagebox.showinfo(f'{lang['info']}', f'{lang['show_info']}')
        lab_text_click_speed['text'] = f'{lang['click_speed']}:\t{click_speed} {lang['sec']}'
        click_speed = float(ent_click_speed.get())
        selected_mouse_btn = mouse_btn.get()
        selected_hotkey = hotkey.get()
        settings['click_speed'] = ent_click_speed.get()
        settings['selected_mouse_btn'] = mouse_btn.get()
        settings['selected_hotkey'] = hotkey.get()
        add_hotkey(f'Alt + {selected_hotkey}', set_clicker)


def clicker_lmb(event=None) -> None:
    global lmb_clicks
    lmb_clicks += 1
    lab_click_counter_lmb['text'] = f'{lang['lmb']}: {lmb_clicks}'


def clicker_rmb(event=None) -> None:
    global rmb_clicks
    rmb_clicks += 1
    lab_click_counter_rmb['text'] = f'{lang['rmb']}: {rmb_clicks}'


def finish() -> None:
    save_settings(settings)
    root.destroy()  # Закрытие окна


# Tk: Создание и настройка окна
root: Tk = Tk()
root.geometry('500x500+500+150')
root.resizable(False, False)
root.title(f'{lang['title']}')
icon: PhotoImage = PhotoImage(file='resources/icons/mouse-clicker.png')
root.iconphoto(True, icon)

# Button: Изменить язык
btn_change_lang: ttk.Button = ttk.Button(root, text=f'{lang['lang']}', state='enabled', command=change_lang)
btn_change_lang.place(width=80, height=30, x=400, y=12)

# Label: Кол. кликов
lab_click_counter_lmb: ttk.Label = ttk.Label(root, text=f'{lang['lmb']}: {lmb_clicks}', font=16)
lab_click_counter_rmb: ttk.Label = ttk.Label(root, text=f'{lang['rmb']}: {rmb_clicks}', font=16)
lab_click_counter_lmb.place(x=125, y=50)
lab_click_counter_rmb.place(x=300, y=50)

# Label: Скорость клика
lab_text_click_speed: ttk.Label = ttk.Label(root, text=f'{lang['click_speed']}:\t{click_speed} {lang['sec']}', font=16)
lab_text_click_speed.place(x=125, y=100)

# Label: Текст для поле ввода
lab_text_new_click_speed: ttk.Label = ttk.Label(root, text=f'{lang['change_speed']}:', font=16)
lab_text_new_click_speed.place(x=125, y=150)

# Entry: Поле для ввода скорости мыши
ent_click_speed: ttk.Entry = ttk.Entry(root, font=16, width=4)
ent_click_speed.place(x=325, y=150)
ent_click_speed.insert(0, str(click_speed))
ent_click_speed.configure(validate='key', validatecommand=(root.register(validate_input), '%S'))

# Radiobutton: ЛКМ или ПКМ
lmb, rmb = 'left', 'right'
mouse_btn = StringVar(value=settings['selected_mouse_btn'])
rad_lmb: ttk.Radiobutton = ttk.Radiobutton(root, text=f'{lang['lmb']}', value=lmb, variable=mouse_btn)
rad_rmb: ttk.Radiobutton = ttk.Radiobutton(root, text=f'{lang['rmb']}', value=rmb, variable=mouse_btn)
rad_lmb.place(x=175, y=200)
rad_rmb.place(x=275, y=200)

# Label: Текст для горячей клавиши
lab_text_hotkey: ttk.Label = ttk.Label(root, text=f'{lang['hotkey']}: Alt +', font=16)
lab_text_hotkey.place(x=125, y=250)

# Button: Кнопка для горячей клавиши
hotkey: StringVar = StringVar(value=settings['selected_hotkey'])
btn_change_hotkey: ttk.Button = ttk.Button(root, textvariable=hotkey, state='enabled', command=change_hotkey)
btn_change_hotkey.place(width=28, height=28, x=350, y=250)

# Button: Кнопка применение изменения
btn_apply: ttk.Button = ttk.Button(root, text=f'{lang['apply']}', state='enabled', command=apply)
btn_apply.place(width=100, height=35, x=200, y=300)

# Button: Кликер
btn_clicker: ttk.Button = ttk.Button(root, text=f'{lang['click']}', state='enabled')
btn_clicker.place(width=150, height=50, x=175, y=375)
btn_clicker.bind('<Button-1>', clicker_lmb)
btn_clicker.bind('<Button-3>', clicker_rmb)

# Button: Кнопка закрытие окна
btn_exit: ttk.Button = ttk.Button(root, text=f'{lang['exit']}', state='enabled', command=finish)
btn_exit.place(width=80, height=30, x=400, y=462)

root.protocol("WM_DELETE_WINDOW", finish)

root.mainloop()
