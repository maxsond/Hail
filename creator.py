roomdict = {}

class room:

	def __init__(self,name,maxocc=0,occlist=[],exitlist=[],thinglist=[],oxygen=100,desc="Needs a description"):
		self.name = name
		self.maxocc = maxocc
		self.occlist = occlist
		self.exitlist = exitlist
		self.thinglist = thinglist
		self.oxygen = oxygen
		self.desc = desc
		
	def cam(self):
		r = self.name + '\n\n' + self.desc
		return r

class char:
	
	def __init__(self,name,job,friends,loc,oxygen=100):
		self.name = name
		self.job = job
		self.friends = friends
		self.loc = location
		self.oxygen = oxygen
		
	def move(curroom,newroom):
		self.loc = newroom
		curroom.occlist.index(self).pop()
		newroom.occlist.append(self)