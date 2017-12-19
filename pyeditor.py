from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import pyttsx3
import pyperclip
import webbrowser
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import sys

# adding highlighting in the future.
# modules_used
class app():
    """user interface layout """

    def __init__(self, frame):
        frame = Frame()
        frame.pack()
        root.title("Pyeditor")
        ttk.Style().configure("TLable", relief="raised")
        ttk.Style().configure("Tframe", padding=10, width="10", relief="raised",  background="green")
        ttk.Style().configure("TButton", padding=4, relief="raised", background="#ff4",  foreground="black")
        self.fileName = StringVar()
        self.filename = Label(text="File Name")
        self.filename.pack(fill="both")
        self.filen = ttk.Entry(textvariable=self.fileName, width="20")
        self.filen.pack(side="top")
        self.v = self.fileName.get()
        self.contentdisplay = Label(text="File Contents")
        self.contentdisplay.pack(fill="both", padx=19)
        self.contents = Text()
        self.contents.pack(fill="both")
        self.openfile = ttk.Button(text="Open", command=self.fileopen)
        self.openfile.pack(side="left")
        self.save = ttk.Button(text="Add Content", command=self.save)
        self.save.pack(side="left")
        self.fullsave = ttk.Button(text="Save", command=self.overwrite)
        self.fullsave.pack(side="left")
        self.Newfile = ttk.Button(text="New file", command=self.new)
        self.Newfile.pack(side="left")
        self.cleartext = ttk.Button(text="Clear txt", command=self.clearfile)
        self.cleartext.pack(side="left")
        self.Speak = ttk.Button(text="Speak text", command=self.textSpeak)
        self.Speak.pack(side="left")
        self.About = ttk.Button(text="About me", command=self.about)
        self.About.pack(side="left")
        self.Copy = ttk.Button(text="Copy text", command=self.copytext)
        self.Copy.pack(side="left")
        self.Copy = ttk.Button(text="Paste text", command=self.Pastetext)
        self.Copy.pack(side="left")
        self.webview = ttk.Button(text="Web view", command=self.webview)
        self.webview.pack(side="left")
        self.search = ttk.Button(text="Search", command=self.searchit)
        self.search.pack(side="left")
        self.Exit = ttk.Button(text="Exit", command=self.Exitprogram)
        self.Exit.pack(side="left")
        self.showcurrent = ttk.Button(text="Check Stack Overflow", command=self.searchStack)
        self.showcurrent.pack(side="left")
    """user interface controls and functions"""


    def fileopen(self):
        try:
            self.v = self.fileName.get()
            with open(self.v, "r") as r:
                content = r.read()
                self.contents.insert(INSERT, content)
        except:
            messagebox.showwarning("error", "file not found")

    def save(self):
        try:
            self.v = self.fileName.get()
            with open(self.v, "a") as w:
                w.write(self.contents.get(1.0, END))
        except:
            messagebox.showwarning("error", "file not found")

    def new(self):
        self.v = self.fileName.get()
        with open(self.v, "w") as w:
            w.write("")

    def clearfile(self):
        try:
            self.v = self.fileName.get()
            with open(self.v, "w+") as w:
                w.write("")
                self.contents.insert(INSERT, "")
        except:
            messagebox.showwarning("file not found")

    def overwrite(self):
        try:
            self.v = self.fileName.get()
            with open(self.v, "w") as w:
                w.write(self.contents.get(1.0, END))
        except:
            messagebox.showwarning("error", "file not found")

    def textSpeak(self):
        self.engine = pyttsx3.init()
        self.engine.say(self.contents.get(1.0, END))
        self.engine.runAndWait()

    def about(self):
        messagebox.showinfo("about", "created by:Technowizard \n\nyear:2017")

    def copytext(self):
        self.Copiedtext = pyperclip.copy(self.contents.get(1.0, END))

    def Pastetext(self):
        self.contents.insert(INSERT, pyperclip.paste())

    def webview(self):
        try:
            self.v = self.fileName.get()
            with open(self.v, "r") as r:
                webbrowser.open_new(self.v)
        except:
            messagebox.showwarning("error", "file not found")

    def searchit(self):
        self.v = self.fileName.get()
        webbrowser.open_new_tab("https://www.google.com/search?q=" + self.v)

    def Exitprogram(self):
        sys.exit()

    def searchStack(self):
        self.v = self.fileName.get()
        webbrowser.open_new_tab("https://www.stackoverflow.com/search?q=" + self.v)

    def run(self):
        try:
            self.v = self.fileName.get()
            with open(self.v, "r") as r:
                os.startfile(self)
        except:
            messagebox.showwarning("error", "file not found")


root = Tk()
App = app(root)
root.iconbitmap("Paomedia-Small-N-Flat-Pencil.ico")
root.mainloop()
