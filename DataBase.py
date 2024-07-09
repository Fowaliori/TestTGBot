import datetime

import psycopg2
from tkinter import *
from psycopg2 import *
from datetime import *


def printUsers(event):
    conn = psycopg2.connect(dbname="testtgbase", user="postgres", password="123", host="127.0.0.1", port="5959")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userstg")
    list = []
    for person in cursor.fetchall():
        list.append(f"{person[0]}: {person[1]} - {person[2]} - {person[3]}")
    list_var = Variable(value=list)
    list_listbox = Listbox(listvariable=list_var, width=50)
    list_listbox.place(x=0, y =200)
    conn.commit()
    cursor.close()
    conn.close()

print(datetime.now().date())
def addUser(event):
    conn = psycopg2.connect(dbname="testtgbase", user="postgres", password="123", host="127.0.0.1", port="5959")
    cursor = conn.cursor()


window = Tk()
window.title("Интерфейс для работы с базой данных")
window.geometry("1920x1080")
addNewUser = Button(text="Добавить нового пользователя")
addNewUser.place(x=0,y=0)
showUsers = Button(text="Показать всю таблицу")
showUsers.place(x=200,y=0)
showUsers.bind("<ButtonPress>", printUsers)

window.mainloop()