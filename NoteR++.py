from tkinter.filedialog import *
import sys
from tkinter import *
from tkinter.messagebox import *

root = Tk()
label = Label(root,text="Note<<R>>M",fg="indigo")
label.pack()
text = Text(root)
text.pack(fill=BOTH,expand=1)

def savefile():
	t = text.get(0.0,END)
	file = filedialog.asksaveasfilename(defaultextension=".txt")
	f = open(file,'w')
	f.write(t)
	f.close()

button = Button(root,text='SAVE',command=savefile,fg='red',bg="lightblue")
button.pack(side=RIGHT,padx=5,pady=5)
button2 = Button(root,text='QUIT',command=quit,bg="lightpink",fg="red")
button2.pack(side=LEFT)
root.mainloop()
