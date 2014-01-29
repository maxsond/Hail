import creator
import display
import winsize
x = winsize.x()
y = winsize.y()
def read(sentence):
	try: 
		sarray = sentence.split(" ", 1)
		verb = sarray[0].lower()
		noun = sarray[1].lower()
	except:
		display.clear()
		t = "Error. Invalid input detected."
		p = display.msg(t)
		t = ""
		p = display.msg(t)
		display.clear()
		return None
	verblist = ["cr"]
	if verb in verblist:
		interact(noun,verb)
	elif verb == "quit":
		t = "Thanks for playing!"
		display.clear()
		p = display.msg(t)
		display.end()
		curses.endwin()
		exit()
	else:
		display.clear()
		m = "Humanity is not yet capable of such feats. Try doing something else."
		display.msg(m)
		m = "Valid verbs are: Taste, Feel, Listen, Smell, Push, and Pull."
		display.msg(m)
		m = "You can also type 'quit game' to recover your sight."
		display.msg(m)
		display.clear()
		return None

def command(noun,verb):
	pass
'''
def interact(noun,verb):
	interactdict = {
		"feel": "You reach out and touch the " + noun + ".",
		"push": "You lean into the " + noun + " and push.",
		"taste": "You brace your delicate palate and lick the " + noun + ".",
		"listen": "You listen intently to the " + noun + ".",
		"smell": "You take a long whiff of the " + noun + ".",
		"pull": "You tug at the " + noun + "."
		}
	newthingdict = {
		"feel": "What does it feel like?",
		"push": "What happens?",
		"taste": "What does it taste like?",
		"listen": "What does it sound like?",
		"smell": "What does it smell like?",
		"pull": "What happens?"
		}
	if noun in creator.thingdict:
		display.clear()
		t = interactdict[verb]
		h = len(t)/2
		p = display.msg(y/2,x/2-h,0.1,t)
		p.tw(True)
		if creator.thingdict[noun].feel == "":
			display.clear()
			t = newthingdict[verb]
			h = len(t)/2
			p = display.msg(y/2,x/2-h,0.1,t)
			creator.thingdict[noun].feel = display.inp(p)
		else:
			display.clear()
			t = creator.thingdict[noun].feel
			h = len(t)/2
			p = display.msg(y/2,x/2-h,0.1,t)
			p.tw(True)
	else:
		creator.thingdict[noun] = creator.thing(noun)
		display.clear()
		t = interactdict[verb]
		h = len(t)/2
		p = display.msg(y/2,x/2-h,0.1,t)
		p.tw(True)
		display.clear()
		t = newthingdict[verb]
		h = len(t)/2
		p = display.msg(y/2,x/2-h,0.1,t)
		creator.thingdict[noun].feel = display.inp(p)
'''