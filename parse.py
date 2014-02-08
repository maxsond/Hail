##	@package parse
#
#	Reads player input and produces appropriate output

import display
import winsize
from creator import Room
x = winsize.x()
y = winsize.y()
## Attempts to read input from player
#
# Must be able to be split into at least two words. Any number of words after the first is treated as a single string.
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
		command(noun,verb)
	elif verb == "quit":
		t = "Thanks for playing!"
		display.clear()
		p = display.msg(t)
		display.end()
		curses.endwin()
		exit()
	else:
		display.clear()
		m = "Error. Unknown command."
		display.msg(m)
		m = "Valid commands are: cr"
		display.msg(m)
		m = "Or enter 'quit game' to format your own hard drive."
		display.msg(m)
		display.clear()
		return None
## Processes a noun-verb pair as a command
def command(noun,verb):
	if verb == 'cr':
		roomlist = {
		'airlock': Room('Airlock'), 
		'bridge': Room('Bridge'),
		'hydroponics': Room('Hydroponics'),
		'medical': Room('Medical'),
		'engineering': Room('Engineering'),
		'propulsion': Room('Propulsion')
		}
		if noun in roomlist:
			m = "Command accepted. Accessing room diagnostics for " + noun + "."
			display.msg(m)
			display.msg(roomlist[noun].cam())
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