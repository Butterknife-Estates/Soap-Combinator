#!/usr/apps/bin/python

#Soap Combinator program
#Butterknife Estates
from Tkinter import *

DIVRES=0.5
MAX=10

class Soap: #The class for the entire window and its workings
	def __init__(self, master):
		self.root = Canvas(master, width=50, height=100)
		master.title("Oil Calculator")
		self.oilnum = Spinbox(master, from_=2, to=MAX, width=10, command=self.addsub)	#Number in oil spinbox
		self.oilsave=int(self.oilnum.get())	#Number of oil entries active
		self.oiltarget=160			#Initial target mixture
		self.targ = Entry(master, width=10, textvariable=self.oiltarget)
		self.targ.insert(0,160)			#Set inital value in the box
		self.percent=100
		self.lab = Label(master, width=10, textvariable=self.percent)
		self.oilnum.grid(row=0, column=0)	#Places them on the grid
		self.targ.grid(row=0, column=1)
		self.lab.grid(row=0,column=2)

		self.scales=[]		#Array of scales
		self.locked=[]		#Array of boolean locks
		self.value=[]		#Array of values for each oil
		self.valueent=[]	#Array of entry boxes for the values
		self.lockb=[]		#Array of checkboxes for the locks
		disstate=NORMAL
		for i in range(MAX):	#Initializes all the entry boxes
		    self.scales.append(Scale(master, from_=0, to=100, orient=HORIZONTAL, resolution=DIVRES, state=disstate))
		    self.scales[i].set(100.0/(self.oilsave))
		    self.locked.append(False)
		    self.lockb.append(Checkbutton(master, text="Lock", variable=self.locked, state=disstate))
		    self.valueent.append(Entry(master, width=10, state=disstate))
		    self.valueent[i].insert(0,self.oiltarget/(self.oilsave))
		    self.scales[i].grid(row=i+1, column=0)
		    self.lockb[i].grid(row=i+1, column=1)
		    self.valueent[i].grid(row=i+1, column=2)
		    if i >= self.oilsave-1:	#Disables entries 
			disstate=DISABLED
		calcgo = Button(master, text="Calculate", command=self.pushUpdate)
		calcgo.grid(row=12)		#Adds calculate button

	def update(self):	#Main function that updates the sliders
	    	oilactual=0
		vlist = []
		pplist = []
		vvlist = []
		for i in range(self.oilsave):
			oilactual+=self.scales[i].get()*int(self.valueent[i].get())/100.0	#Adds up the actual oil mixture
			pplist.append(self.scales[i].get())					#Gets a list of percentages for indexing
			vvlist.append(int(self.valueent[i].get()))					#Gets a list of values for indexing
			if ~self.locked[i]:							#Makes a list of all unlocked sliders
				vlist.append(int(self.valueent[i].get()))
		self.percent=sum(pplist)							#Updates the percentage
		
		print vlist
		vlist.sort()									#Sorts the unlocked sliders
		
		if self.percent != 100:								#Adjusts sliders to compensate for a bad percentage
			neg=(100-self.percent)/abs(100-self.percent)	#Negative if too high and positive if too low
			negbool = neg==1 #True if too low; false if too high

						
			#If p is too low and oila is less than oilt, use highest that is not 100
			#If p is too low and oila is more than oilt, use lowest that is not 100
			#If p is too high and oila is less than oilt, use lowest that is not 0
			#If p is too high and oila is more than oilt, use highest that is not 0
			
			while True:
				if negbool: #Too low. Gain percents
					if oilactual < self.oiltarget:
						ind=-1	#Choose highest oil
					else:
						ind=0	#Choose lowest oil
				else: #Too high. Lose percents
					if oilactual > self.oiltarget:
						ind=-1	#Choose highest oil
					else:
						ind=0	#Choose lowest oil
				i=vvlist.index(vlist[ind])
				if pplist[i]>=100:
					vlist.pop(ind)
				else:
					break
			
			
			while self.percent != 100.0 and self.scales[i].get()<100.0 and self.scales[i].get()>0.0:
				temp = self.scales[i].get()
				print self.percent, (100-self.percent)/abs(100-self.percent),temp
				self.scales[i].set(temp+DIVRES*neg)
				self.percent+=DIVRES*neg
		else:	
			neg=(self.oiltarget-oilactual)/abs(-oilactual+self.oiltarget)	#Positive if too low, negative if too high
			if len(vlist) < 2:	#Exits if there aren't enough options
				return False

			high=vvlist.index(vlist[-1])
			low =vvlist.index(vlist[0])
			if len(vlist) < 2 or high==low:						#Exits if there aren't enough options
				return False				
			while (neg*oilactual <= neg*self.oiltarget) and (self.scales[high].get() > 0) and (self.scales[low].get() < 100):
				
				temph=self.scales[high].get()
				self.scales[high].set((temph+neg*DIVRES))
				templ=self.scales[low].get()
				self.scales[low].set((templ-neg*DIVRES))
				oilactual += float(self.valueent[high].get())*DIVRES/100.0*neg
				oilactual += float(self.valueent[low].get())*DIVRES/100.0*-neg
				print neg, oilactual, self.oiltarget, self.scales[high].get(), self.scales[low].get()
		for i in range(self.oilsave):							#Updates widgets
			self.scales[i].update()
			self.lockb[i].update()
			self.valueent[i].update()
		self.lab.update()
		return True
			

			
			

	def addsub(self):						#Adds or removes entries
	    while self.oilsave != int(self.oilnum.get()):
		    if self.oilsave<int(self.oilnum.get()):
    			i=self.oilsave
			disstate=NORMAL
        		self.oilsave+=1
		    if self.oilsave>int(self.oilnum.get()):
		        i=self.oilsave-1
        		disstate=DISABLED
        		self.oilsave-=1
		    self.scales[i].configure(state=disstate)
		    self.lockb[i].configure(state=disstate)
		    self.valueent[i].configure(state=disstate)
		    self.valueent[i].insert(0,self.oiltarget/(self.oilsave))
		    self.scales[i].update()
		    self.lockb[i].update()
		    self.valueent[i].update()
	    #self.update()
	    
	    
	def slider(self):						#Use this function when slider is moved (unused)
		#temp = self.locked[i]
		#self.locked[i]=True
		self.update()
		self.update()
		#self.locked[i]=temp
		
	def pushUpdate(self):						#What happens when the calculate button is pressed
		i=0
		while i < 2 and ~self.update():			#Update up to 10 times! Just in case
			i+=1
			
		
				


if __name__ == "__main__":	#Main
    root = Tk()
    wind = Soap(root)
    root.mainloop()

