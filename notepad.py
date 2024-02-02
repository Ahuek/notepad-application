from tkinter import *
from tkinter import filedialog
root=Tk()
root.configure(background='light blue')
def save_file():
    file_save=filedialog.asksaveasfilename(defaultextension='.txt')
    with open(file_save,'w') as file:
        file.write(t.get('1.0',END))
def new_file():
    t.delete('1.0',END)
def exit():
    root.quit()

b1=Button(root,text='save file',bg='blue',command=save_file)
b2=Button(root,text='New file',bg='blue',command=new_file)
b3=Button(root,text='exit',bg='blue',command=exit)
b1.pack()
b2.pack()
b3.pack()
t=Text(root,width=10000,height=1000)
t.pack()
root.mainloop()