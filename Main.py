from tkinter import *
from datetime import*
from datetime import datetime
from time import strftime
from Stock import Stock
from Client_Management import ClientManagement
import sqlite3
from Data_base import baseData

class Main(object):
    @classmethod
    def __init__(self):
        self.win = Tk()
        self.win.title("Bleu Market")
        self.win.resizable(width=False, height=False)
        self.win.geometry("1060x690")

        self.topbar = Frame(self.win, bg="#dee2e6", width=1060).place(x=0, y=0, height=56)
        self.leftbar = Frame(self.win, bg="#dee2e6", width=124).place(x=0, y=56, height=690)

        # self.hors()
        # self.power = PhotoImage(file='Deconnecton.gif')
        # self.power = self.power.zoom(50)
        # self.power = self.power.subsample(250)
        # self.off = Button(self.win, image=self.power, border=0, command=quit)
        # self.off.place(x=1250, y=20)


        # self.Vente = Button(self.leftbar,text = "CLient", width=13, height= 2,
        #     font=('Microsoft YaHei Light', 12, 'bold'), bd= 0, command=ClientManagement(self.win)).place(x = 0, y = 250)


        self.Stock1 = Button(self.leftbar, text="Stock", width=12, height=2,
                         font=('Microsoft YaHei Light', 12, 'bold'), bd= 0, command=Stock(self.win)).place(x=0, y=350)




        self.win.mainloop()

    def hors(self):
        self.date = strftime("%d/%m/%Y")
        self.time = strftime("%H%M:%S")
        self.timeLab = Label(self.topbar, text=self.date + '  ' + self.time, bg='#fff', font=('Bahnschrift', 16))
        self.timeLab.place(x=1000, y=30)
        self.timeLab.after(1000, self.hors)

if __name__ == '__main__':
    Main()