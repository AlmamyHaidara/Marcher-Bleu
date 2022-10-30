def action1(self):
    self.Produit = self.entry_produit1.get()
    self.quantite = self.entry_quantite1.get()
    self.pu = self.entry_pu.get()
    self.categori = self.entry_categorie.get()
    self.date = strftime("%d/%m/%Y")
    self.list = [self.Produit, self.quantite, self.pu, self.categori, self.date]
    if ((self.Produit or self.quantite or self.pu or self.categori) == ""):

        return False
    else:

        self.base = sqlite3.connect('Marche_Bleu_Base.db3')

        self.curseur.execute(self.tabStock.Table_stock)
        self.Stock = "INSERT INTO Stock(Produit,Quantite, Pu, Catégorie, Date ) values(?, ?, ?, ?, ?)"
        for i in range(len(self.list)):
            self.curseur.execute(self.Stock, (i))

        self.base.commit()
        self.base.close()
        self.displayDatas()
        self.entry_produit1.delete(0, END)
        self.entry_quantite1.delete(0, END)
        self.entry_pu.delete(0, END)
        self.entry_categorie.delete(0, END)


# ===========================  Creation the function to display the treeview the screen graphe ===========================#
def displayDatas(self):
    self.base1 = sqlite3.connect('Marche_Bleu_Base.db3')
    self.curseur1 = self.base1.cursor()
    self.tabStock = baseData()
    self.curseur1.execute(self.tabStock.Table_stock)
    self.liste = self.curseur1.execute('select * from Stock')
    self.clear_all1()
    for self.row in self.liste:
        self.bord1.insert('', END, values=self.row)
    self.base1.commit()
    self.base1.close()


def clear_all1(self):
    for self.item in self.bord1.get_children():
        self.bord1.delete(self.item)


# ===========================Creation of the function permet to selected the row on the treeview ===========================#
def Select_recore1(self):
    self.entry_id.delete(0, END)
    self.entry_produit1.delete(0, END)
    self.entry_quantite1.delete(0, END)
    self.entry_pu.delete(0, END)
    self.entry_categorie.delete(0, END)

    self.selected = self.bord1.focus()
    self.values = self.bord1.item(self.selected, 'values')
    self.entry_id.insert(0, self.values[0])
    self.entry_produit1.insert(0, self.values[1])
    self.entry_quantite1.insert(0, self.values[2])
    self.entry_pu.insert(0, self.values[3])
    self.entry_categorie.insert(0, self.values[4])


# ===========================Creation of the function permet to update the row selected on the treeview ===========================#
def updete_recor1(self):
    self.base = sqlite3.connect('Marche_Bleu_Base.db3')
    self.curseur = self.base.cursor()
    self.curseur.execute(baseData.table1())
    self.selected = self.bord1.focus()
    self.ID = self.entry_id.get()
    self.Produit = self.entry_produit1.get()
    self.quantite1 = self.entry_quantite.get()
    self.Pu = self.entry_pu.get()
    self.Categorie = self.entry_categorie.get()
    self.date = strftime("%d/%m/%Y")

    self.values = self.bord1.item(self.selected, values=(
        self.ID, self.Produit, self.quantite, self.Pu, self.Categorie, self.date))
    self.curseur.execute("UPDATE Stock SET  Produit = ?,\
                    Quantite = ?,\
                    Pu = ?,\
                    Catégorie = ?,\
                    Date = ?\
                    WHERE ID = ?",
                         (self.Produit,
                          self.quantite,
                          self.Pu,
                          self.Categorie,
                          self.date,
                          self.ID))
    self.base.commit()
    self.base.close()

    self.entry_id.delete(0, END)
    self.entry_produit.delete(0, END)
    self.entry_quantite1.delete(0, END)
    self.entry_pu.delete(0, END)
    self.entry_categorie.delete(0, END)
    # self.entry_date.delete ( 0 , END )


# ===========================Creation of the function permet to delete the row selected on the treeview ===========================#
def delete_button(self):
    self.idSelect = self.bord1.item(self.bord1.selection())["values"][0]
    # creation of the data file
    self.base = sqlite3.connect('Marche_Bleu_Base.db3')
    self.curseur = self.base.cursor()
    self.curseur.execute(self.tabStock.Table_stock)
    self.curseur.execute(f"DELETE FROM Stock WHERE id = {self.idSelect}")
    self.base.commit()
    self.bord1.delete(self.bord1.selection())
    self.base.close()


def operation(self):
    self.base = sqlite3.connect('Marche_Bleu_Base.db3')
    self.curseur = self.base.cursor()
    self.curseur.execute(self.tabStock.Table_stock)
    self.sub = self.curseur.execute(
        f"SELECT Quantite - {int(self.entry_quantite1.get())} FROM Stock WHERE Produitéq = {self.entry_produit.get()} ")
    self.curseur.execute("UPDATE Stock SET Quantite = ?,\
                    WHERE id = ?",
                         (self.sub,
                          self.ID
                          ))
    self.base.commit()
    self.base.close()
    pass
