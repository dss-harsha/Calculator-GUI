from tkinter import *

window = Tk()
window.geometry("700x750")
window.minsize(700,750)
window.maxsize(700,750)
window.config(bg="gray")
window.title("Mini Calculator")


def click(event):
	global calvalue
	text = event.widget.cget("text")
	if(text == '='):
		if(calvalue.get().isdigit()):
			value=int(calvalue.get())
		else:
			value = eval(screen.get())

		calvalue.set(value)
		screen.update()
	elif(text == 'C'):
		calvalue.set("")
		screen.update()
	else:
		calvalue.set(calvalue.get()+text)

calvalue = StringVar()
calvalue.set("")
f = Frame(window,padx=20,pady=20)
screen = Entry(f,textvar=calvalue,font="lucida 50 bold",bg='light blue')
screen.pack(fill=X, padx=20, pady=15)
f.pack()


row1 = ["7","8","9","+"]
row2 = ["4","5","6","-"]
row3 = ["1","2","3","*"]
row4 = ["0","C","=","/"]

f = Frame(window,bg="gray",padx=30,pady=10)

for i in row1:
	b = Button(f,text=i,padx=8,font="lucida 25 bold")
	b.pack(side=LEFT,padx = 10,pady=10)
	b.bind("<Button-1>",click)
f.pack()

f = Frame(window,bg="gray",padx=30,pady=10)

for i in row2:
	b = Button(f,text=i,padx=10,font="lucida 25 bold")
	b.pack(side=LEFT,padx = 10,pady=10)
	b.bind("<Button-1>",click)
f.pack()

f = Frame(window,bg="gray",padx=30,pady=10)

for i in row3:
	b = Button(f,text=i,padx=10,font="lucida 25 bold")
	b.pack(side=LEFT,padx = 10,pady=10)
	b.bind("<Button-1>",click)
f.pack()

f = Frame(window,bg="gray",padx=30,pady=10)

for i in row4:
	b = Button(f,text=i,padx=10,font="lucida 25 bold")
	b.pack(side=LEFT,padx = 10,pady=10)
	b.bind("<Button-1>",click)
f.pack()

window.mainloop()