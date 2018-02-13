from tkinter import *

master=Tk()
master.geometry('100x100')
a=[]

line=[]
line1=[]
OPTIONS = [a]


with open("/etc/passwd") as f:
  line=f.read().splitlines()

for i in range(0,len(line)):
  line1.append(line[i].split(":"))
  if(line1[i][6]=='/bin/bash'):
    a[25:]=line1[i][0].split(":")

variable = StringVar(master)
variable.set(a[0]) # default value

w = OptionMenu(master, variable, *a)
w.pack()

def ok():
    print ("value is:" + variable.get())

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()

