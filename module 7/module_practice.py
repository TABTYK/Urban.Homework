import os
import tkinter
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename(initialfile='/',title='Выберите файл:',
                                          filetypes=(('text-file','.txt'),
                                                     ('all-files','*')))
    text['text'] = text['text'] + filename
    os.startfile(filename)

def print_info():
    messagebox.showinfo('ÍNFO','В этом приложение возможно открыть любой интересующий вас файл.'
                               '\nНажмите выбрать файл и в появившемся окне выберите файл который надо открыть.( ͡° ͜ʖ ͡°)')

def print_about():
    messagebox.showinfo('ABOUT','Версия приложения:1.0\nПриложение написано на Python.( ͡° ͜ʖ ͡°)')

#Настройка окна
window = tkinter.Tk()
window.title("VasyaTyChtoDelaesh'")
window.geometry('550x550+700+220')
window.configure(bg='silver')
window.iconbitmap(default='avg.png')
window.resizable(False,False)

#Настройка верхнего меню
main_menu = Menu()
main_menu.add_cascade(label='Info',command=print_info)
main_menu.add_cascade(label='About',command=print_about)
window.config(menu=main_menu)

#Добавление текста, кнопки
text = tkinter.Label(window, text='File:', height=6,width = 70,background='green',foreground='yellow')
text.grid(column =1,row =1)
button_select = tkinter.Button(window,width=20,height=3,text='Выбрать файл',
                               background='yellow',foreground='green',command=file_select)
button_select.grid(column=1,row=2)
window.mainloop() # постоянная работа приложения