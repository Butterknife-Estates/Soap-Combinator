#Soap Combinator program
#Butterknife Estates
from Tkinter import *

master = Tk()

root = Canvas(master, width=50, height=100)
master.title("Oil Calculator")
oilnum = Spinbox(master, from_=5, to=10, width=10)
#oilnum.set(4)
oilsave=oilnum.get()
oiltarget=160
targ = Entry(master, width=10, textvariable=oiltarget)
targ.insert(0,160)
oilnum.grid(row=0, column=0)
targ.grid(row=0, column=1)

scales=[]
locked=[]
value=[]
valueent=[]
lockb=[]
for i in range(int(oilnum.get())):
    scales.append(Scale(master, from_=0, to=100, orient=HORIZONTAL, resolution=0.5))
    scales[i].set(100.0/int(oilnum.get()))
    locked.append(False)
    lockb.append(Checkbutton(master, text="Lock", variable=locked))
    valueent.append(Entry(master, width=10))
    valueent[i].insert(0,100/int(oilnum.get()))
    scales[i].grid(row=i+1, column=0)
    lockb[i].grid(row=i+1, column=1)
    valueent[i].grid(row=i+1, column=2)

#while 1:
 #   for i in range(oilnum.get()):

	

def update():
	if oilsave<oilnum.get():
	    i=oilsave+1
	    scales.append(Scale(master, from_=0, to=100, orient=HORIZONTAL, resolution=0.5))
	    scales[i].set(100.0/int(oilnum.get()))
	    locked.append(False)
	    lockb.append(Checkbutton(master, text="Lock", variable=locked))
	    valueent.append(Entry(master, width=10))
	    valueent[i].insert(0,100/int(oilnum.get()))
	    scales[i].grid(row=i+1, column=0)
	    lockb[i].grid(row=i+1, column=1)
	    valueent[i].grid(row=i+1, column=2)
            oilsave+=1
	if oilsave>oilnum.get():
	    scales.pop()
	    lockb.pop()
	    valueent.pop()
	    scales.pop()
	    locked.pop()
	    oilsave-=1
	for i in range(oilsave);
	    if ~locked[i]:
		
def updateVol():
root.mainloop()
