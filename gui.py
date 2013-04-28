from Tkinter import *
import main

class Application(Frame):
    def createWidgets(self):
        self.UPDATE = Button(self)
        self.UPDATE["text"] = "Update"
        self.UPDATE["command"] =  main.update

        self.UPDATE.pack({"side": "left"})

        self.GET_CHANGES = Button(self)
        self.GET_CHANGES["text"] = "Get Changes",
        self.GET_CHANGES["command"] = main.get_changes
		
        self.GET_CHANGES.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()