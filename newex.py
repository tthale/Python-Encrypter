import Tkinter as tk
from Crypto.Cipher import AES
import base64
import os


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Please Input your Information")
        self.geometry("360x200+400+300")
        self.warn = tk.Label(self, text = "Please Don't use any Commas")
        self.warn.pack()
        self.user = tk.Label(self, text ="Username:  ")
        self.user.place(x = 65, y = 45)
        self.name = tk.Entry(self, bd = 2)
        self.name.place(x= 140, y = 45)
        self.pas = tk.Label(self, text="Password:  ")
        self.pas.place(x = 65, y = 85)
        self.word = tk.Entry(self, bd = 2, show = "*")
        self.word.place(x = 140, y = 85)
        self.button = tk.Button(self, text="Finish", width = 10, height = 1, command=self.on_button)
        self.button.place(x = 145, y = 135)

    def on_button(self):
        self.encrypt(self.name.get() + "," + self.word.get())
        self.destroy()
        
    def encrypt(self, raw_string):
        text = open("exam.txt", "w")
        if (len(os.getcwd()) < 16):
            key = ((os.getcwd())+(os.getcwd()))[0:16]
        else: key = (os.getcwd())[0:16]    
        iv = 'Homework_Crawler'
        cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        encrypted = base64.b64encode(iv + cipher.encrypt(raw_string))
        print("encrypted=" + encrypted)
        text.write(encrypted)
        text.close()

app = SampleApp()
app.mainloop()