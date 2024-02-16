
from tkinter import *

root = Tk()
root.title("Weathr App")
root.resizable(0,0)
root.geometry("1000x800")
root.config(background="lightblue")


searchFrameImage = PhotoImage(file="search.png")
searchInputFrame = Label(root, image=searchFrameImage, bg="lightblue")
searchInputFrame.place(x=160, y=110)

searchEntery = Entry(root, width=30, font=("verdana", 12), bg="#404040", fg="white", justify="center")
searchEntery.place(x=190, y=135)

searchButtonImage = PhotoImage(file = "search_icon_2.png")
searchButtom = Button(root, image=searchButtonImage, cursor="hand2")
searchButtom.place(x=510, y=130)

#micButtonImage = PhotoImage(file = "mic.png")
#micButton = Button(root, image=micButtonImage, cursor="hand2")
#micButton.place(x=550, y=130)

logoImage = PhotoImage(file="logo.png")
logo = Label(root, image=logoImage, background="lightblue")
logo.place(x=260, y=250)

root.mainloop()