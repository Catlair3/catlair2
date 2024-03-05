import tkinter
from tkinter import messagebox


def start_up():
    import json
    with open('users.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


data = start_up()
print(data)


def func():
    user = entry.get()
    pas = entry2.get()
    if (user in data['users'].keys() and pas == data['users'][user]):
        return messagebox.showinfo('Вход',
                                   'Поздравляю, вы зашли!')

    else:
        return messagebox.showerror('Вход',
                            'Ошибка при вводе данных')
window = tkinter.Tk()
window.geometry('700x200')
tkinter.Label(text='Логин', font=('Arial, 15')).pack()
entry = tkinter.Entry(font=('Arial, 15'))
entry.pack()
tkinter.Label(text='Пароль', font=('Arial, 15')).pack()
entry2 = tkinter.Entry(font=('Arial, 15'))
entry2.pack()
button = tkinter.Button(text='Войти', width=10, height=2, command=func).pack()

window.mainloop()
