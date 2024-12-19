import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Hesap Makinesi - Yunus Karatas")
        #setting window size
        width=558
        height=648
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_905=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_905["font"] = ft
        GLabel_905["fg"] = "#333333"
        GLabel_905["justify"] = "center"
        GLabel_905["text"] = "Rakam1"
        GLabel_905.place(x=110,y=200,width=70,height=25)

        GLabel_70=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_70["font"] = ft
        GLabel_70["fg"] = "#333333"
        GLabel_70["justify"] = "center"
        GLabel_70["text"] = "Rakam2"
        GLabel_70.place(x=230,y=200,width=70,height=25)

        GLabel_817=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_817["font"] = ft
        GLabel_817["fg"] = "#333333"
        GLabel_817["justify"] = "center"
        GLabel_817["text"] = "Sonuc"
        GLabel_817.place(x=370,y=200,width=70,height=25)

        GButton_954=tk.Button(root)
        GButton_954["bg"] = "#2b2a33"
        ft = tkFont.Font(family='Times',size=10)
        GButton_954["font"] = ft
        GButton_954["fg"] = "#fbfbfe"
        GButton_954["justify"] = "center"
        GButton_954["text"] = "+"
        GButton_954.place(x=50,y=420,width=70,height=25)
        GButton_954["command"] = self.GButton_954_command

        GButton_102=tk.Button(root)
        GButton_102["bg"] = "#2b2a33"
        ft = tkFont.Font(family='Times',size=10)
        GButton_102["font"] = ft
        GButton_102["fg"] = "#fbfbfe"
        GButton_102["justify"] = "center"
        GButton_102["text"] = "-"
        GButton_102.place(x=180,y=420,width=70,height=25)
        GButton_102["command"] = self.GButton_102_command

        GButton_491=tk.Button(root)
        GButton_491["bg"] = "#2b2a33"
        ft = tkFont.Font(family='Times',size=10)
        GButton_491["font"] = ft
        GButton_491["fg"] = "#fbfbfe"
        GButton_491["justify"] = "center"
        GButton_491["text"] = "*"
        GButton_491.place(x=310,y=420,width=70,height=25)
        GButton_491["command"] = self.GButton_491_command

        GButton_69=tk.Button(root)
        GButton_69["bg"] = "#2b2a33"
        ft = tkFont.Font(family='Times',size=10)
        GButton_69["font"] = ft
        GButton_69["fg"] = "#fbfbfe"
        GButton_69["justify"] = "center"
        GButton_69["text"] = "/"
        GButton_69.place(x=440,y=420,width=70,height=25)
        GButton_69["command"] = self.GButton_69_command

        GLineEdit_294=tk.Entry(root)
        GLineEdit_294["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_294["font"] = ft
        GLineEdit_294["fg"] = "#333333"
        GLineEdit_294["justify"] = "center"
        GLineEdit_294["text"] = ""
        GLineEdit_294.place(x=110,y=290,width=70,height=25)

        GLineEdit_213=tk.Entry(root)
        GLineEdit_213["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_213["font"] = ft
        GLineEdit_213["fg"] = "#333333"
        GLineEdit_213["justify"] = "center"
        GLineEdit_213["text"] = ""
        GLineEdit_213.place(x=230,y=290,width=70,height=25)

        GLineEdit_394=tk.Entry(root)
        GLineEdit_394["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_394["font"] = ft
        GLineEdit_394["fg"] = "#333333"
        GLineEdit_394["justify"] = "center"
        GLineEdit_394["text"] = ""
        GLineEdit_394.place(x=370,y=290,width=70,height=25)

    def GButton_954_command(self):
        print("command")


    def GButton_102_command(self):
        print("command")


    def GButton_491_command(self):
        print("command")


    def GButton_69_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    textBoxYazilanlar1 = tk.StringVar() #Değişken tanımlama
    textBoxYazilanlar2 = tk.StringVar() #Değişken tanımlama
    textBoxYazilanlar3 = tk.StringVar() #Değişken tanımlama
    root.mainloop()
