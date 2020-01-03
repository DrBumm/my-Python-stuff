import tkinter as tk
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        self.cookies = 0
        self.multiplier = 1
        self.multiplierlvl = 1
        self.cookie_img = PhotoImage(file="Cookie.png")
        
        Frame.__init__(self, master)
        self.pack()

        self.cookie_button = Button(self, text=str(1*self.multiplier) + "+ Keks(e)", relief=FLAT, borderwidth=0, command=self.add_cookie)
        self.cookie_button.config(image=self.cookie_img)
        self.cookie_button.pack()

        self.multiplier_button = Button(self, text="Kekse x" + str(self.multiplier+self.multiplierlvl) + " (" + str(100*self.multiplierlvl) + ") Kekse", relief=FLAT, borderwidth=0, command=self.multiplier)
        self.multiplier_button.pack()

        self.display_cookies = Label(self, text="Du  hast schon: "+ str(self.cookies) + " Kekse")
        self.display_cookies.pack()

    def add_cookie(self):
        self.cookies += 1

        self.display_cookies["text"] = "Du hast schon: " + str(self.cookies) + " Kekse"

    def multiplier(self):
        print(12)
        self.multplier += self.multiplierlvl
        self.multiplier *= 2

        self.multiplier_button["text"] = "Kekse x" + str(self.multiplier+self.multiplierlvl) + " (" + str(100*self.multiplierlvl) + ") Kekse"

root = Tk()

root.title("Cookie Klicker")
root.minsize(width=300, height=200)
root.maxsize(width=300, height=200)

window = Window(master=root)

window.mainloop()
