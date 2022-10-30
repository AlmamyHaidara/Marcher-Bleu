import sqlite3
from tkinter import *
from tkinter import messagebox,ttk
# import tkcalendar
from datetime import *

class login_and_password:
    def __init__(self):
        self.wine = Tk ( )
        self.wine.title ( 'Login' )
        # self.wine.iconbitmap ( 'Project_logo.ico' )
        self.wine.config ( bg = '#023E8A' )
        self.wine.geometry ( '500x500' )

        self.Login = Label ( self.wine , text = 'Login' , font = ('Bahnschrift' , 24 , 'bold') , fg = '#DDDDDD' , bg = '#023E8A' )
        self.Login.place ( x = 200 , y = 50 )
        self.usernameEntry = Entry ( self.wine , bg = '#023E8A' , font = ('Bahnschrift' , 11) , fg = '#DDDDDD' , border = 0 )
        self.usernameEntry.place ( x = 120 , y = 160 , width = 250 , height = 30 )
        self.usernameEntry.insert ( 0 , "Username" )
        self.usernameEntry.bind ( '<Enter>' , self.enterU )
        self.usernameEntry.bind ( '<Leave>' , self.LeaveU )
        self.ligneU = Frame ( self.wine , height = 2 , width = 250 )
        self.ligneU.place ( x = 120 , y = 190 )

        self.passwordEntry = Entry ( self.wine , bg = '#023E8A' , font = ('Bahnschrift' , 11) , fg = '#DDDDDD' , border = 0 )
        self.passwordEntry.place ( x = 120 , y = 260 , width = 250 , height = 30 )
        self.passwordEntry.insert ( 0 , "Password" )
        self.passwordEntry.bind ( '<Enter>' , self.enterP )
        self.passwordEntry.bind ( '<Leave>' , self.LeaveP )
        self.ligneP = Frame ( self.wine , height = 2 , width = 250 )
        self.ligneP.place ( x = 120 , y = 290 )
        self.var = StringVar ( )
        self.LabelError = Label ( self.wine , textvariable = self.var , fg = 'red' , font = ('Bahnschrift' , 8) , bg = '#023E8A' )
        self.LabelError.place ( x = 120 , y = 310 , width = 250 )
        self.Submit = Button ( self.wine , text = 'Submit' , bg = '#00509d' , font = ('Bahnschrift' , 14 , 'bold') ,
                          fg = '#DDDDDD' , border = 0 , command = self.action )
        self.Submit.place ( x = 100 , y = 360 , width = 290 , height = 40 )

        self.wine.mainloop ( )

    def enterU(self,event):
        self.usernameEntry.delete ( 0 , END )
        self.usernameEntry.place ( x = 120 , y = 160 , width = 250 , height = 30 )
        self.Username = Label ( self.wine , text = 'Username' , font = ('Bahnschrift' , 11) , fg = '#DDDDDD' , bg = '#023E8A' )
        self.Username.place ( x = 122 , y = 135 )

    def LeaveU(self,event):
        self.usernameEntry.place ( x = 120 , y = 160 , width = 250 , height = 30 )

    def enterP(self,event):
        self.passwordEntry.delete ( 0 , END )
        self.passwordEntry.place ( x = 120 , y = 260 , width = 250 , height = 30 )
        self.Password = Label ( self.wine , text = 'Password' , font = ('Bahnschrift' , 11) , fg = '#DDDDDD' , bg = '#023E8A' )
        self.Password.place ( x = 122 , y = 225 )

    def LeaveP(self,event):
        self.passwordEntry.place ( x = 120 , y = 260 , width = 250 , height = 30 )

    def action(self):
        self.user = self.usernameEntry.get ( )
        self.password = self.passwordEntry.get ( )
        if ((self.user or self.password) == ""):
            messagebox.showerror ( 'Info' , 'Please fill in the form correctly' )
            return False
        else:
            self.conn = sqlite3.connect ( 'Marche_Bleu_Base.db3' )
            self.conn.execute ( "CREATE TABLE IF NOT EXISTS User(user TEXT NOT NULL, password TEXT NOT NULL)" )
            self.conn.execute ( "INSERT INTO User(user,password) VALUES('admin','admin')" )
            self.curs = self.conn.cursor ( )
            self.curs.execute ( "SELECT * FROM User WHERE user = ? AND password = ? " , (self.user , self.password) )
            self.row = self.curs.fetchone ( )
            if self.row:
                messagebox.showinfo ( 'Info' , 'Login Succes' )
            else:
                self.var.set ( 'Please the password or the user is not available.' )
            self.conn.commit ( )
            self.conn.close ( )
            self.usernameEntry.delete(0,END)
            self.passwordEntry.delete(0,END)
            self.wine.destroy()



if __name__ == '__main__':
    login_and_password()


