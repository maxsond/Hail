roomdict = {}
class room:

	def __init__(self,name,maxocc=0,occlist=[],exitlist=[],thinglist=[],oxygen=100):
		self.name = name
		self.maxocc = maxocc
		self.occlist = occlist
		self.exitlist = exitlist
		self.thinglist = thinglist
		self.oxygen = oxygen

class char:
	
	def __init__(self,name,job,friends,loc):
		self.name = name
		self.job = job
		self.friends = friends
		self.loc = location
		
	def move(curroom,newroom)
		self.loc = newroom
		curroom.occlist.index(self).pop()
		newroom.occlist.append(self)
		curroom.