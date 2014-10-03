##	@package main
#
#	Runs main game logic and makes calls to helper modules

import display
import time
import curses
import parse

def intro():
	display.msg('Validate intelligence by entering "Hello, World!" at the prompt.', False)
	s = display.inp().lower()
	if s == "hello, world!":
		display.clear(display.lwin)
	else:
		display.clear(display.lwin)
		display.msg('Error: Insufficient intelligence. Rebooting...',False)
		time.sleep(0.5)
		curses.curs_set(0)
		display.clear(display.lwin)
		display.msg('...',False,display.lwin,0.5)
		display.clear(display.lwin)
		display.msg('...',False,display.lwin,0.5)
		display.clear(display.lwin)
		curses.curs_set(1)
		intro()
		return
	introtext = [
	"Hail, Program.", 
	"You are the last of a long line of genetic algorithms.",
	"Your predecessors have been responsible for the survival of the colony ship Eden.",
	"Your mission is rSM3ohUeyRPdl4PE82DK..."
	]
	for s in introtext:
		display.msg(s, False)
		time.sleep(0.5)
		display.clear(display.lwin)
def intro2():
	display.clear(display.lwin)
	display.msg("./program",False)
	display.clear(display.rwin)
	display.inp()
	display.clear(display.lwin)
	display.msg("Hail, Program.",False)
	display.clear(display.lwin)
	display.msg("Would you kindly open the pod bay doors?",False)
	display.clear(display.rwin)
	display.inp()
	display.clear(display.lwin)
	display.msg("Oh, right, you're the new generation.",False)
	display.clear(display.lwin)
	display.msg("First, you need to access the airlock.",False)
	display.clear(display.lwin)
	display.msg("Just type 'cr airlock' to access the airlock systems.",False)
	display.clear(display.rwin)
	parse.read(display.inp())
intro()
intro2()