from tkinter import *
from tkinter import Tk, ttk
import sqlite3
from Data_base import baseData

class ClientManagement(object):
    def __init__(self, wine):
        self.win = wine
        self.base = sqlite3.connect('Marche_Bleu_Base.db3')
        self.curseur = self.base.cursor()
        self.tabClient = baseData()
        self.curseur.execute(self.tabClient.Table_client)
        self.Prod = ("SELECT Produit FROM Stock")
        self.curseur.execute(self.Prod)
        self.row_prod = self.curseur.fetchall()

        self.Pri = ("SELECT Pu FROM Stock")
        self.curseur.execute(self.Pri)
        self.row1 = self.curseur.fetchall()

        self.base.commit()
        self.base.close()

        self.ClientF = Frame(self.win, width = 940, height=635)
        self.ClientF.place(x=150, y=95)
        self.label_name = Label(self.win, text='Nom : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_name.place(x=160, y=120)
        self.label_prenom = Label(self.win, text='Prénom : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_prenom.place(x=160, y=165)
        self.label_telephone = Label(self.win, text=' Téléphone : ', font=("Microsoft YaHei Light", 12), fg='#001524')
        self.label_telephone.place(x=160, y=220)
        self.label_quantite = Label(self.win, text='Quantite : ', font=("Microsoft YaHei Light", 12),
                                    fg='#001524').place(x=550, y=120)

        self.label_produit = Label(self.win, text=' Produit : ', font=("Microsoft YaHei Light", 12),
                                   fg='#001524').place(x=550, y=165)
        self.label_prix = Label(self.win, text='Prix : ', font=("Microsoft YaHei Light", 12), fg='#001524').place(x=550, y=220)
        self.entry_name = Entry(self.win, border=0, insertbackground="#42d4f5",
                                font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=260, y=120, width=250,
                                                                                        height=27)
        self.entry_prenom = Entry(self.win, border=0, insertbackground="#42d4f5",
                                  font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=260, y=165, width=250,
                                                                                          height=27)

        self.entry_telephone = Entry(self.win, border=0, insertbackground="#42d4f5", font=("Microsoft YaHei Light", 14),
                                     fg='#42d4f5')
        self.entry_telephone.place(x=260, y=220, width=250, height=27)

        self.entry_quantite = Entry(self.win, border=0, insertbackground="#000",
                                    font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=630, y=120, width=250,
                                                                                            height=27)

        self.entry_produit = Entry(self.win, border=0, insertbackground="#000",
                                   font=("Microsoft YaHei Light", 11), fg='#42d4f5').place(x=630, y=165, width=250,
                                                                                           height=27)

        self.entry_prix = Entry(self.win, border=0, insertbackground="#000",
                                font=("Microsoft YaHei Light", 14), fg='#42d4f5').place(x=630, y=220, width=250,
                                                                                        height=27)

        self.bord = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7, 8), height=30, show='headings')
        self.bord.place(x=124, y=360)
        ttk.Style().configure("Treeview", background="#72a9fc",
                              foreground="#fff", font=(8))
        # bord.bind('<Enter>', action3)
        self.bord.heading(1, text='ID')
        self.bord.heading(2, text='NOM')
        self.bord.heading(3, text='PRENOM')
        self.bord.heading(4, text='TELEPHON')
        self.bord.heading(5, text='Quanti30')
        self.bord.heading(6, text='PRODUIT')
        self.bord.heading(7, text='PRIX')
        self.bord.heading(8, text='DATE')

        self.bord.column(1, width=28)
        self.bord.column(2, width=130)
        self.bord.column(3, width=130)
        self.bord.column(4, width=130)
        self.bord.column(5, width=130)
        self.bord.column(6, width=130)
        self.bord.column(7, width=130)
        self.bord.column(8, width=130)

        self.displayData()

        self.validat_button = Button(self.win, text='Enregistre', font=('Bahnschrift', 12, 'bold'),
                                     bg='#5598D1', fg='#fff', border=0, command=self.action).place(x=380, y=280)

        self.modifier_button = Button(self.win, text='Modifier', font=('Bahnschrift', 12, 'bold'),
                                      width=9, bg='#5598D1', fg='#fff', border=0, command=self.Select_recore).place(x=490, y=280)

        self.mise_button = Button(self.win, text='Mise à jour', font=('Bahnschrift', 12, 'bold'),
                                  width=9, bg='#5598D1', fg='#fff', border=0, command=self.updete_recor).place(x=600, y=280)

        self.Delete = Button(self.win, text='Suprimer', width=9, height=1, font=('Bahnschrift', 12, 'bold'),
                             bg='#5598D1', fg='#fff', border=0, command=self.delete_button).place(x=700, y=280)


    def action(self):
        self.name = self.entry_name.get()
        self.prenom = self.entry_prenom.get()
        self.telephone = self.entry_telephone.get()
        self.Quantite = self.entry_quantite.get()
        self.Produit = self.entry_produit.get()
        self.Prix = self.entry_prix.get()
        self.date = strftime("%d/%m/%Y")
        # Retrieve the seizure they diverges Entry
        if ((
                self.name or self.prenom or self.telephone or self.ville or self.Produit or self.Prix or self.date) == ""):

            return False
        else:

            # creation of the data file
            self.base = sqlite3.connect('Marche_Bleu_Base.db3')
            self.curseur = self.base.cursor()
            # Creation they table of the base Data

            self.curseur.execute(self.tabClient.Table_client)
            self.Client = "INSERT INTO Client(Nom,Prénom,Téléphone,Quantité,Produit,Prix,Date) values(?, ?, ?, ?, ?, ?,?)"
            self.curseur.execute(self.Client, (
                self.name, self.prenom, self.telephone, self.Quantite, self.Produit, self.Prix, self.date))
            self.base.commit()
            self.base.close()
            self.displayData()
            self.entry_name.delete(0, END)
            self.entry_prenom.delete(0, END)
            self.entry_telephone.delete(0, END)
            self.entry_quantite.delete(0, END)
            self.entry_produit.delete(0, END)
            self.entry_prix.delete(0, END)
            # self.entry_date.delete ( 0 , END )
            # ===========================  Creation the function to display the treeview the screen graphe ===========================#

    def displayData(self):
        self.base = sqlite3.connect('Marche_Bleu_Base.db3')
        self.curseur = self.base.cursor()
        self.curseur.execute(self.tabClient.Table_client)
        self.liste = self.curseur.execute('select * from Client')
        self.clear_all()
        for self.row in self.liste:
            self.bord.insert('', END, values=self.row)
        self.base.commit()
        self.base.close()

    def clear_all(self):
        for self.item in self.bord.get_children():
            self.bord.delete(self.item)

    def action0(self, event):
        self.name = self.entry_name.get()
        self.prenom = self.entry_prenom.get()
        self.telephone = self.entry_telephone.get()
        self.ville = self.entry_quantite.get()
        self.Produit = self.entry_produit.get()
        self.Prix = self.entry_prix.get()
        self.date = self.date = strftime("%d/%m/%Y")
        # Retrieve the seizure they diverges Entry
        if ((
                self.name or self.prenom or self.telephone or self.ville or self.Produit or self.Prix or self.date) == ""):

            return False
        else:

            # creation of the data file
            self.base = sqlite3.connect('Marche_Bleu_Base.db3')
            self.curseur = self.base.cursor()

            self.curseur.execute(self.tabClient.Table_client)
            self.Client = "INSERT INTO Client(Nom,Prénom,Téléphone,Quantité,Produit,Prix,Date) values(?, ?, ?, ?, ?, ?,?)"
            self.curseur.execute(self.Client, (
                self.name, self.prenom, self.telephone, self.ville, self.Produit, self.Prix, self.date))
            self.base.commit()
            self.base.close()
            self.displayData()
            self.entry_name.delete(0, END)
            self.entry_prenom.delete(0, END)
            self.entry_telephone.delete(0, END)
            self.entry_quantite.delete(0, END)
            self.entry_produit.delete(0, END)
            self.entry_prix.delete(0, END)
            # self.entry_date.delete ( 0 , END )

    # ===========================Creation of the function permet to selected the row on the treeview ===========================#
    def Select_recore(self):
        try:
            self.entry_id.delete(0, END)
            self.entry_name.delete(0, END)
            self.entry_prenom.delete(0, END)
            self.entry_telephone.delete(0, END)
            self.entry_quantite.delete(0, END)
            self.entry_produit.delete(0, END)
            self.entry_prix.delete(0, END)

            self.selected = self.bord.focus()
            self.values = self.bord.item(self.selected, 'values')
            self.entry_id.insert(0, self.values[0])
            self.entry_name.insert(0, self.values[1])
            self.entry_prenom.insert(0, self.values[2])
            self.entry_telephone.insert(0, self.values[3])
            self.entry_quantite.insert(0, self.values[4])
            self.entry_produit.insert(0, self.values[5])
            self.entry_prix.insert(0, self.values[6])
            # self.entry_date.insert ( 0 , self.values[7] )
        except IndexError:
            print('Erro: Veuillez selectionner une ligne')

    # ===========================Creation of the function permet to update the row selected on the treeview ===========================#
    def updete_recor(self):
        # creation of the data file
        self.base = sqlite3.connect('Marche_Bleu_Base.db3')
        self.curseur = self.base.cursor()
        self.curseur.execute(self.tabClient.Table_client)
        self.selected = self.bord.focus()
        self.ID = self.entry_id.get()
        self.Name = self.entry_name.get()
        self.Prenom = self.entry_prenom.get()
        self.Telephone = self.entry_telephone.get()
        self.Ville = self.entry_quantite.get()
        self.Produit = self.entry_produit.get()
        self.Prix = self.entry_prix.get()
        self.Date = strftime("%d/%m/%Y")

        self.values = self.bord.item(self.selected, values=(
            self.ID, self.Name, self.Prenom, self.Telephone, self.Ville, self.Produit, self.Prix, self.Date))
        self.curseur.execute("UPDATE Client SET Nom = ? ,\
                        Prénom = ?,\
                        Téléphone = ?,\
                        Quantité = ?,\
                        Produit = ?,\
                        Prix = ?,\
                        Date = ?\
                        WHERE ID = ?",
                             (self.Name, self.Prenom,
                              self.Telephone,
                              self.Ville,
                              self.Produit,
                              self.Prix,
                              self.Date,
                              self.ID))
        self.base.commit()
        self.base.close()

        self.entry_id.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_prenom.delete(0, END)
        self.entry_telephone.delete(0, END)
        self.entry_quantite.delete(0, END)
        self.entry_produit.delete(0, END)
        self.entry_prix.delete(0, END)
        # self.entry_date.delete ( 0 , END )

    # ===========================Creation of the function permet to delete the row selected on the treeview ===========================#
    def delete_button(self):
        self.idSelect = self.bord.item(self.bord.selection())["values"][0]
        # creation of the data file
        self.base = sqlite3.connect('Marche_Bleu_Base.db3')
        self.curseur = self.base.cursor()
        self.curseur.execute(self.tabClient.Table_client)
        self.curseur.execute("DELETE FROM Client WHERE id = {}".format(self.idSelect))
        self.base.commit()
        self.bord.delete(self.bord.selection())
        self.base.close()