import tkinter as tk
import buttons

width = 800
height = 700


def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys
    import tty

    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch


getch = _find_getch()


class Window:
    def __init__(self):
        self.blst = []
        self.objih = "wall"
        self.o = 0.0
        self.x = 0.0
        self.y = 0.0
        self.buttons = []
        self.obj_buttons = []
        self.done = False
        self.root = tk.Tk()
        self.player_on_field = False
        self.canvas = tk.Canvas(self.root, height=height, width=width)
        self.canvas.pack()

        self.frame1 = tk.Frame(self.root, bg="white")
        self.frame1.place(relwidth=1, relheight=0.25)
        self.frame1.pack(side="bottom")

        self.frame2 = tk.Frame(self.root, bg="white")
        self.frame2.place(relwidth=1, relheight=0.75)

        self.frame3 = tk.Frame(self.root, bg="white")
        self.frame3.place(relwidth=1, relheight=1)

        self.root.title("Minibyte-Engine")

        self.button1 = tk.Button(self.frame3, text="", command=self.start)
        self.button1.place(relwidth=1, relheight=1)

        self.text_label = tk.Label(self.frame3, text="Welcome to the Minibyte-Engine!!")
        self.text_label.place(relx=0.02, rely=0.45)
        self.text_label.config(font=("Courier", 30))

    def start(self):
        self.frame3.destroy()
        self.frame1.config(bg="white")
        self.frame2.config(bg="white")
        buttons.create_buttons(self, tk)

        for i in range(400): #20
            self.buttons[i].place(relx=0+self.x, rely=0+self.y, relwidth=0.05, relheight=0.05)
            self.buttons[i].config(fg="white")
            self.x += 0.05
            if self.x >= 1.0:
                self.y += 0.05
                self.x = 0

        self.obj_buttons.append(tk.Button(self.frame1, text="Wall", command=lambda : self.change_objih("wall"),
                                          relief=tk.FLAT))
        self.obj_buttons[0].config(bg="black", fg="white")
        self.obj_buttons[0].pack(side=tk.LEFT)

        self.obj_buttons.append(tk.Button(self.frame1, text="Player", command=lambda : self.change_objih("player"),
                                          relief=tk.FLAT))
        self.obj_buttons[1].config(bg="white", fg="black")
        self.obj_buttons[1].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Gegner", command=lambda : self.change_objih("enemie"),
                                          relief=tk.FLAT))
        self.obj_buttons[2].config(bg="white", fg="black")
        self.obj_buttons[2].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Ziel", command=lambda : self.change_objih("finish"),
                                          relief=tk.FLAT))
        self.obj_buttons[3].config(bg="white", fg="black")
        self.obj_buttons[3].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Delete", command=lambda : self.change_objih("delete"),
                                          relief=tk.FLAT))
        self.obj_buttons[4].config(bg="white", fg="black")
        self.obj_buttons[4].pack(side=tk.LEFT, padx=50)

        self.obj_buttons.append(tk.Button(self.frame1, text="Play", command=self.play, relief=tk.FLAT))
        self.obj_buttons[5].config(bg="white", fg="black")
        self.obj_buttons[5].pack(side=tk.LEFT)

    def place_obj(self, btid):
        if self.objih == "wall":
            if self.buttons[int(btid)]["text"] == "+":
                self.player_on_field = False
            self.buttons[int(btid)].config(bg="black", text="", fg="black")
        elif self.objih == "player":
            if self.buttons[int(btid)]["text"] != "+" and not self.player_on_field:
                self.player_on_field = True
                self.buttons[int(btid)].config(bg="white", text="+", fg="black", font=("Courier", 20, "bold"))
        elif self.objih == "enemie":
            if self.buttons[int(btid)]["text"] == "+":
                self.player_on_field = False
            self.buttons[int(btid)].config(bg="white", text="M", fg="black", font=("Courier", 30, "bold"))
        elif self.objih == "finish":
            if self.buttons[int(btid)]["text"] == "+":
                self.player_on_field = False
            self.buttons[int(btid)].config(bg="white", text=":", fg="black", font=("Courier", 30, "bold"))
        elif self.objih == "delete":
            if self.buttons[int(btid)]["text"] == "+":
                self.player_on_field = False
            self.buttons[int(btid)].config(bg="white", text="", fg="white")

    def change_objih(self, ctobj):
        self.objih = ctobj

    def play(self):
        global getch
        self.frame1.destroy()
        self.frame2.place(relwidth=1, relheight=1)
        self.objih = None
        while not self.done:
            inp = getch()
            if inp == "w":
                for i in range(400):
                    if self.buttons[i]["text"] == "+":
                        ppos = i
                        break
                try:
                    self.buttons[ppos].config(text="")
                    self.buttons[ppos-10].config(text="+")
                except IndexError:
                    continue
            if inp == "s":
                for i in range(400):
                    if self.buttons[i]["text"] == "+":
                        ppos = i
                        break
                try:
                    self.buttons[ppos].config(text="")
                    self.buttons[ppos+10].config(text="+")
                except IndexError:
                    continue

    def mainloop(self):
        self.root.mainloop()


window = Window()
window.mainloop()
