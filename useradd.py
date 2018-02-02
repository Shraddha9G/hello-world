
from tkinter import *
from tkinter import messagebox 
 
root=Tk()
root.geometry('300x100')

def click():
	ans=e1.get()
	#print("%s user added" %(ans))
	if ans == 'admin':
		L2 = Label(root,text="%s user already exists" %(ans)).grid(row=4,column=1)
		ans=e1.append()
	else:
		L2 = Label(root,text="%s user added" %(ans)).grid(row=4,column=1)
		ans=e1.append()

L1=Label(root,text="UserName").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
 
b=Button(root,text="Add User",command=click).grid(row=2,column=1)
root.mainloop()
