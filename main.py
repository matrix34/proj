print('\nWelcome to The Game')
#The standard format for room names is (Position)(Step no.). Deviation from this may result in severe confusion. Comments should be added when possible.
def L1():
	#unfinished
	#This is for the left room, after choice zero.
	print('\nAs you enter a bright light catches your eye in the corner of the room.')
	print('\nA voice echoes: \"Well done survivor! Now enter the tunnel...\"')
	c2 = str(input('\nA: Who are you?\nD:Walk into the tunnel\n Your choice: '))
	if(c2 == 'a'):
		print('\nYou whisper out: \"Who.. are you? And what do you want?\"')
	elif(c2 == 'd'):
		exit()
def R1():
	#unfinished
	#This is for the right room, after choice zero.
	exit()
def r0():
	#This is room zero, where the adventure starts~
	print('\n\"Errr... what\'s happening?\"')
	print('\nA sign pops up in front of the gloomy room: ')
	print('\n\"Left or right? Choose carefully!\"')
	c1 = str(input('\nA: Enter the left room\nD: Enter the right room\nYour choice: '))
	if(c1 == 'a'):
		L1()
	if(c1 == 'd'):
		R1()
def intr():
	#This is the introduction.
	intro = str(input('\nPress Z to start... '))
	if(intro == 'z'):
		r0()
	else:
		print('\nOi! Press Z!')
		intr()
intr()