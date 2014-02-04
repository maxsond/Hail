## 	@package creator
#	Handles creation and manipulation of objects

##	Room Dictionary
#
#	Stores Room objects using a string (should be a valid Room name) as the key and a Room object as the value
roomdict = {}

class Room:

	def __init__(self,name,maxocc=0,occlist=[],exitlist=[],thinglist=[],oxygen=100,desc="Needs a description"):
		self.name = name
		self.maxocc = maxocc
		self.occlist = occlist
		self.exitlist = exitlist
		self.thinglist = thinglist
		self.oxygen = oxygen
		self.desc = desc
	## Displays room description
	#
	# Starts with name, then a blank line, then the description of the room concatenated with sentences describing its contents.
	def cam(self):
		r = self.name + '\n\n' + self.desc
		return r

class Char:
	
	def __init__(self,name,job,friends,loc,oxygen=100):
		self.name = name
		self.job = job
		self.friends = friends
		self.loc = location
		self.oxygen = oxygen
		
	## Moves character from curroom to newroom
	
	def move(curroom,newroom):
		self.loc = newroom
		curroom.occlist.index(self).pop()
		newroom.occlist.append(self)