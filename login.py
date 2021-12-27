from tkinter import font
from typing import List
import Banco
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date

lg=Tk()
lg.title('ADMIN')
lg.geometry('250x200')
lg.configure(background='#dde')
lg.bind("<Escape>", lambda x: lg.destroy())

def logar():
    vLogin=Login.get()
    vSenha=Senha.get()
    try:
        Banco.cursor.execute("SELECT * FROM funcionarios WHERE nome='"+vLogin+"' AND codigo='"+vSenha+"'")
        if Banco.cursor.fetchone() is not None:
            Banco.cursor.execute("SELECT * FROM funcionarios WHERE nome='"+vLogin+"' AND codigo='"+vSenha+"'")
            Banco.cursor.fetchone()
            messagebox.showinfo(title='SUCESSO', message='Login realizado com sucesso!')
        else:
            messagebox.showerror(title='ERRO', message='Login ou senha incorretos!')
    except:
        print('Erro ao logar')

vLogin=StringVar()
vSenha=StringVar()
lbLogin=Label(lg, text='Login:', bg='#dde')
lbLogin.place(x=50, y=10)
Login=Entry(lg, textvariable=vLogin)
Login.place(x=50, y=30, width=150)
lbSenha=Label(lg, text='Senha:', bg='#dde')
lbSenha.place(x=50, y=60)
Senha=Entry(lg, textvariable=vSenha, show='*')
Senha.place(x=50, y=80, width=150)
bLogar=Button(lg, text='Logar', command=logar)
lg.bind("<Return>", lambda x: logar())
bLogar.place(x=50, y=110, width=150)
lg.mainloop()