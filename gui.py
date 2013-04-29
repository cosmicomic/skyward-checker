from Tkinter import *
import tkMessageBox
import main

def display_text(text):
	tkMessageBox.showinfo(text)

root = Tk()
root.geometry("340x320")

root.title("Skyward Checker")

text_frame = Frame(root)

update = Button(text_frame)
update["text"] = "update"
update["command"] =  main.update

get_changes = Button(text_frame)
get_changes["text"] = "Get Changes",
get_changes["command"] = main.get_changes

username = Entry(text_frame)

username_label = Label(text_frame)
username_label["text"] = "username"

password = Entry(text_frame)

password_label = Label(text_frame)
password_label["text"] = "password"

welcome_label = Label(text_frame)
welcome_label["text"] = "Welcome!"
welcome_label.place(x = 160, y = 48, width = 68, height = 24)

submit = Button(text_frame, text="Submit", command = display_text("OK!"))

text_frame.pack()

uname = "None"
pword = "None"
root.mainloop()