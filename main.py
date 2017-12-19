print('\nWelcome to The Game')
#The standard format for room names is (Position)(Step no.). Deviation from this may result in severe confusion. Comments should be added when possible.
#Every dialogue should start with \n for optimal visual effect.
def L1():
	#unfinished
	#This is for the left room, after choice zero.
	print('\nAs you enter a bright light catches your eye in the corner of the room.')
	print('\nA voice echoes: \"Well done survivor! Now enter the tunnel...\"')
	c2 = str(input('\nA:"Who are you?"\nD: Walk into the tunnel\n Your choice: '))
	if(c2 == 'a'):
		print('\nYou whisper out: \"Who.. are you? And what do you want?\"')
	elif(c2 == 'd'):
		exit()
def R1():
	#unfinished
	#This is for the right room, after choice zero.
	print('\nYou enter what seems to be an abandoned classroom.')
	print('\n\"Help me... Help me...\"')
	print('\nAs you search around the room ou find a body on the floor.')
	c2 = str(input('\nA: Examine the body\nD: Run!\n Your choice: '))
	if(c2 == 'a'):
		print('\nThe body seems to be emitting a foul stench.')
		print('\nAs you further search the body, you find dark spots on it.')
		print('\nSuddenly a claw springs out of the body!')
		c2a = str(input('A: Punch it! Grab grab the claw\nB: Back away from de body'))
	elif(c2 == 'd'):
		print('\nAs you head back into the starting room, it seems different.')
		print('\nThere is now a table in the centre of the room with a knife on it.')
		print('\nAs you look back you see a man at the door staring at you.')
		c2a = str(input('A: Pick up the knife to defend yourself\nB: Run!'))
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