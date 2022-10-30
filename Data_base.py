import sqlite3
class baseData():

    def __init__(self):
        self.base = sqlite3.connect ( 'Marche_Bleu_Base.db3' )
        self.curseur = self.base.cursor ()
        self.Table_client = "CREATE TABLE IF NOT EXISTS Client(id INTEGER PRIMARY KEY AUTOINCREMENT,\
               Nom TEXT NOT NULL,\
               Prénom TEXT NOT NULL,\
               Téléphone TEXT NOT NULL,\
               Quantité INTEGER,\
               Produit TEXT NOT NULL,\
               Prix INTEGER ,\
               Date TEXT NOT NULL)"
        self.Table_stock = "CREATE TABLE IF NOT EXISTS Stock(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                       Produit TEXT NOT NULL,\
                       Quantite INTEGER,\
                       Pu INTEGER,\
                       Catégorie TEXT NOT NULL,\
                       Date TEXT NOT NULL)"

        self.base.commit()
        self.base.close()

