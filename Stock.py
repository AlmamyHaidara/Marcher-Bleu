from tkinter import *
from tkinter import Tk, ttk
import sqlite3
from Data_base import baseData


class Stock(object):

    def __init__(self, wine):
        self.win = wine
        self.Stock = Frame(self.win, height=650, width=1068).place(x = 122, y = 56)
        self.label_id = Label(self.win, text='ID : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_id.place(x=160, y=120)
        self.label_produit = Label(self.win, text='Produit : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_produit.place(x=160, y=165)
        self.label_quantite = Label(self.win, text=' Quantité : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_quantite.place(x=550, y=120)
        self.label_pu = Label(self.Stock, text=' Prix unitaire : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_pu.place(x=155, y=220)
        self.categorie = Label(self.Stock, text='Catégorie : ', font=("Microsoft YaHei Light", 12), fg='#001524').place(
            x=550, y=165)
        self.montant = Label(self.Stock, text='Montant : ', font=("Microsoft YaHei Light", 12), fg='#001524').place(
            x=550, y=215)

        self.entry_id = Entry(self.Stock, border=0, insertbackground="#42d4f5",
                    font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=270, y=120, width=250, height=27)

        self.entry_produit1 = Entry(self.Stock, border=0, insertbackground="#42d4f5",
                                    font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=270, y=165, width=250, height=27)

        self.entry_quantite1 = Entry(self.Stock, border=0, insertbackground="#42d4f5",
                                     font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=650, y=120, width=250,height=27)

        self.entry_pu = Entry(self.Stock, border=0, insertbackground="#42d4f5",
                              font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=270, y=220, width=250, height=27)
        self.entry_categorie = Entry(self.Stock, border=0, insertbackground="#42d4f5",
                font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=650, y=165, width=250, height=27)
        self.entry_montant = Entry(self.Stock, border=0, insertbackground="#42d4f5",
                font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=650, y=215, width=250, height=27)
        self.bord1 = ttk.Treeview(self.Stock, columns=(1, 2, 3, 4, 5, 6, 7, 8), height=30, show='headings')
        self.bord1.place(x=124, y=360)
        ttk.Style().configure("Treeview", background="#72a9fc",
                              foreground="#fff", font=(8))
        self.bord1.heading(1, text='ID')
        self.bord1.heading(2, text='NOM')
        self.bord1.heading(3, text='PRENOM')
        self.bord1.heading(4, text='TELEPHON')
        self.bord1.heading(5, text='Quantité')
        self.bord1.heading(6, text='PRODUIT')
        self.bord1.heading(7, text='PRIX')
        self.bord1.heading(8, text='DATE')

        self.bord1.column(1, width=28)
        self.bord1.column(2, width=130)
        self.bord1.column(3, width=130)
        self.bord1.column(4, width=130)
        self.bord1.column(5, width=130)
        self.bord1.column(6, width=130)
        self.bord1.column(7, width=130)
        self.bord1.column(8, width=130)

        self.validat_button1 = Button(self.Stock, text='Enregistre', font=('Bahnschrift', 12, 'bold'),
                                      bg='#5598D1', fg='#fff', border=0, command=self.validation)
        self.validat_button1.place(x=380, y=280)

        self.modifier_button1 = Button(self.Stock, text='Modifier', font=('Bahnschrift', 12, 'bold'),
                                       width=9, bg='#5598D1', fg='#fff', border=0)
        self.modifier_button1.place(x=490, y=280)

        self.mise_button1 = Button(self.Stock, text='Mise à jour', font=('Bahnschrift', 12, 'bold'),
                                   width=9, bg='#5598D1', fg='#fff', border=0)
        self.mise_button1.place(x=600, y=280)

        self.Delete1 = Button(self.Stock, text='Suprimer', width=9, height=1, font=('Bahnschrift', 12, 'bold'),
                              bg='#5598D1', fg='#fff', border=0)
        self.Delete1.place(x=700, y=280)
        self.displayDatas()
    def validation(self):
        self.id = self.entry_id.get()
        self.produit = self.entry_produit1.get()
        self.pu = self.entry_pu.get()
        self.quantite = self.entry_quantite1.get()
        self.categori = self.entry_categorie.get()
        self.date = strftime("%d/%m/%Y")
        if((self.Produit or self.quantite or self.pu or self.categori) == ""):
            return False
        else:
            self.list = [self.Produit, self.quantite, self.pu, self.categori, self.date]
            self.base = sqlite3.connect('Marche_Bleu_Base.db3')
            self.curseur.execute(self.tabStock.Table_stock)
            self.Stock = "INSERT INTO Stock(Produit,Quantite, Pu, Catégorie, Date ) values(?, ?, ?, ?, ?)"
            for items in self.list:
                self.curseur.execute(self.Stock, (items))
            self.base.commit()
            self.base.close()
            self.displayDatas()

    def displayDatas(self):
        self.base = sqlite3.connect('Marche_Bleu_Base.db3')
        self.curseur1 = self.base.cursor()
        self.tabStock = baseData()
        self.curseur1.execute(self.tabStock.Table_stock)
        self.liste = self.curseur1.execute('select * from Stock')
        self.clear_all1()
        for self.row in self.liste:
            self.bord1.insert('', END, values=self.row)
        self.base.commit()
        self.base.close()

    def clear_all1(self):
        for self.item in self.bord1.get_children():
            self.bord1.delete(self.item)








