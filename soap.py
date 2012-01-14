#Soap Combinator program
#Butterknife Estates
from Tkinter import *
master = Tk()

w = Canvas(master, width=500, height=800)
oilnum = Spinbox(master, from_=0, to=10)
oilnum.set(4)
oiltarget=160
targ = Entry(master, width=100, textvariable=oiltarget)
oilnum.grid(row=0, column=0)
targ.grid(row=0, column=1)

scales=[]
locked=[]
value=[]
valueent=[]
lockb=[]
for i in range(oilnum.get()):
    scales.append(Scale(master, from_=0, to=100, orient=HORIZONTAL, resolution=0.5))
    scales.set(100.0/oilnum.get())
    locked.append(False)
    value.append(100.0/oilnum.get())
    lockb.append(Checkbutton(master, text="Lock", variable=locked))
    valueent.append(Entry(master, width=60, textvariable=value))
    
    scales.grid(row=i+1, columnspan=3)
    lockb.grid(row=i+1, column=3)
    valueent.grib(row=i+1, column=4)

while 1:
    for i in range(oilnum.get()):
        



    
w.update()    

mainloop()