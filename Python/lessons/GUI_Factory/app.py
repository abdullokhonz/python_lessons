from select_gui_factory import select_gui_factory

user = select_gui_factory()

print(user.get_button())
print(user.get_checkbox())
print(user.get_text_field())

print(user.return_buttons())
print(user.return_checkboxes())
print(user.return_text_fields())
