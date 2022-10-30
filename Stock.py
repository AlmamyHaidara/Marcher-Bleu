from tkinter import *
from tkinter import Tk, ttk
import sqlite3
from Data_base import baseData


class Stock(object):

    def __init__(self, wine):
        self.win = wine
        # width_of_window = 868
        # height_of_window = 650
        # screen_width = self.win.winfo_screenwidth()
        # screen_height = self.win.winfo_screenheight()
        # x_coordinate = (screen_width / 2) - (width_of_window / 2)
        # y_coordinate = (screen_height / 2) - (height_of_window / 2)

        # self.win.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

        # self.navBar = Frame(self.win, height=650, width=100, bg="#5598D1")
        # self.navBar.place(x=0, y=0)

        self.stock = Frame(self.win, height=650, width=1068)
        self.stock.place(x = 100, y = 0)
        self.label_id = Label(self.stock, text='ID : ', font= 12, fg='#001524')
        self.label_id.place(x=20, y=23)
        self.label_produit = Label(self.stock, text='Produit : ',font= 12, fg='#001524')
        self.label_produit.place(x=20, y=83)
        self.categorie = Label(self.stock, text='Catégorie : ', font=12, fg='#001524')
        self.categorie.place( x=20 , y=138)
        self.label_quantite = Label(self.stock, text=' Quantité : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_quantite.place(x=300, y=23)
        self.label_pu = Label(self.stock, text=' Prix unitaire : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_pu.place(x=300, y=83)
        self.label_montant = Label(self.stock, text=' Montant : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_montant.place(x=300, y=138)


        self.entry_id = Entry(self.stock, border=0, insertbackground="#42d4f5", font=12 , fg='#42d4f5').place(x=114, y=23, width=150, height=27)

        self.entry_produit1 = Entry(self.stock, border=0, insertbackground="#42d4f5",font=12, fg='#42d4f5').place(x=114, y=83, width=150, height=27)

        self.entry_categorie = Entry(self.stock, border=0, insertbackground="#42d4f5",
                                     font=12, fg='#42d4f5').place(x=114, y=138, width=150, height=27)

        self.entry_quantite1 = Entry(self.stock, border=0, insertbackground="#42d4f5",
                                     font=12, fg='#42d4f5').place(x=418, y=28, width=150,height=27)

        self.entry_pu = Entry(self.stock, border=0, insertbackground="#42d4f5",
                              font=12, fg='#42d4f5').place(x=418, y=83, width=150, height=27)

        self.entry_montant = Entry(self.stock, border=0, insertbackground="#42d4f5",
                font=12, fg='#42d4f5').place(x=418, y=138, width=150, height=27)
        self.bord1 = ttk.Treeview(self.stock, columns=(1, 2, 3, 4, 5, 6, 7, 8), height=30, show='headings')
        self.bord1.place(x=0, y=281)
        ttk.Style().configure("Treeview", background="#72a9fc",
                              foreground="#fff", font=(6))
        self.bord1.heading(1, text='ID')
        self.bord1.heading(2, text='NOM')
        self.bord1.heading(3, text='PRENOM')
        self.bord1.heading(4, text='TELEPHON')
        self.bord1.heading(5, text='PRODUIT')
        self.bord1.heading(6, text='Quantité')
        self.bord1.heading(7, text='PRIX')
        self.bord1.heading(8, text='DATE')

        self.bord1.column(1, width=18)
        self.bord1.column(2, width=120)
        self.bord1.column(3, width=120)
        self.bord1.column(4, width=110)
        self.bord1.column(5, width=120)
        self.bord1.column(6, width=100)
        self.bord1.column(7, width=100)
        self.bord1.column(8, width=80)

        self.validat_button1 = Button(self.stock, text='Enregistre', font=12,
                                      bg='#5598D1', fg='#fff', border=0, command=self.validation)
        self.validat_button1.place(x=69, y=206)

        self.modifier_button1 = Button(self.stock, text='Modifier', font=12,
                                       width=9, bg='#5598D1', fg='#fff', border=0)
        self.modifier_button1.place(x=214, y=206)

        self.mise_button1 = Button(self.stock, text='Mise à jour', font=12,
                                   width=9, bg='#5598D1', fg='#fff', border=0)
        self.mise_button1.place(x=359, y=206)

        self.Delete1 = Button(self.stock, text='Suprimer', width=9, height=1, font=12,
                              bg='#5598D1', fg='#fff', border=0)
        self.Delete1.place(x=504, y=206)
        self.displayDatas()
       # self.win.mainloop()
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
            self.curseur.execute(self.tabstock.Table_stock)
            self.stock = "INSERT INTO stock(Produit,Quantite, Pu, Catégorie, Date ) values(?, ?, ?, ?, ?)"
            for items in self.list:
                self.curseur.execute(self.stock, (items))
            self.base.commit()
            self.base.close()
            self.displayDatas()

    def displayDatas(self):
        self.base = sqlite3.connect('Marche_Bleu_Base.db3')
        self.curseur1 = self.base.cursor()
        self.tabstock = baseData()
        self.curseur1.execute(self.tabstock.Table_stock)
        self.liste = self.curseur1.execute('select * from stock')
        self.clear_all1()
        for self.row in self.liste:
            self.bord1.insert('', END, values=self.row)
        self.base.commit()
        self.base.close()

    def clear_all1(self):
        for self.item in self.bord1.get_children():
            self.bord1.delete(self.item)








