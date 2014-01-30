roomdict = {}
class room:

	def __init__(self,name,maxocc=0,occlist=[],exitlist=[],thinglist=[],oxygen=100):
		self.name = name
		self.maxocc = maxocc
		self.occlist = occlist
		self.exitlist = exitlist
		self.thinglist = thinglist
		self.oxygen = oxygen