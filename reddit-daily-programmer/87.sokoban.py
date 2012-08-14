# For the reddit daily programmer challenge

# Challenge: http://www.reddit.com/r/dailyprogrammer/comments/y2lbv/8102012_challenge_87_difficult_sokoban_game/
# Solution: http://www.reddit.com/r/dailyprogrammer/comments/y2lbv/8102012_challenge_87_difficult_sokoban_game/c5rv38d
# by @dvoiss on github / @daveasaurus on reddit

# Uses curses and plays in the terminal. This started out pretty minimal but 
# then grew a bit in complexity, so it isn't very clean: the grid is a 
# one-dimensional list, it isn't object-oriented, and doesn't have any 
# other bells and whistles, I kept it under 100 lines. 
# (this version is commented)
#
# When you win it just exits the game :) 
# Otherwise if you want to quit press any key other than the arrow keys.

import curses

player, level, level_width, win_positions = None, None, 0, []
text_items = ["", "Game by daveasaurus", "Daily Programmer Challenge: 8/10/2012",
			"left, right, up, down to move", "any other key quits",
			"http://redd.it/y2lbv", "https://gist.github.com/dvoiss", "" ]

# read the file passed in:
def read_level(file):
	global level, level_width, player, win_positions
	level_string = ''
	level = []
	file = open(file, 'r')
	for line in file.readlines():
		if (line[0] != ';' and line.find('#') != -1):
			level_string += line
			level_width = max(level_width, len(line))

	# normalize all the lines to be the same line width
	for line in level_string.split('\n'):
		level += list(str.ljust(line, level_width))

	# this represents the player's position
	player = level.index('@')

	# build the "win positions" (indicated by a '.')
	position = 0
	while True:
		try:
			position = level.index('.', position + 1)
			win_positions.append(position)
		except ValueError:
			break

# determines whether the player or block ('$') can move to a position
def can_move(position):
	return level[position] == ' ' or level[position] == '.'

# handles horizontal movement
def move_horizontal(direction):
	global level, player
	if (can_move(player + direction)):
		level[player] = ' '
		player += direction
		level[player] = '@'
	elif (level[player + direction] == '$'):
		if (can_move(player + direction * 2)):
			level[player + direction * 2] = '$'
			level[player] = ' '
			player += direction
			level[player] = '@'

# handles vertical movement
def move_vertical(direction):
	global level, level_width, player
	if (can_move(player + level_width * direction)):
		level[player] = ' '
		player += level_width*direction
		level[player] = '@'
	elif (level[player + direction*level_width] == '$'):
		if (can_move(player + direction * 2 * level_width)):
			level[player + direction*2*level_width] = '$'
			level[player] = ' '
			player += level_width*direction
			level[player] = '@'

# our loop function,
# every time through the loop it checks for user input 
# and for the victory condition
def loop(screen):
	# get the size of the lines to center on the screen:
	global text_items
	text_width = max( len(text_items[2]) + 6, level_width )
	
	# draw the informational text lines:
	for idx, line in enumerate(text_items):
		screen.addstr(idx, 0, str.center(line, text_width))

	# check for victory condition
	# also draw a '.' where the blocks need to go,
	# this is done because in the player move function I simply make
	# the position the player was at before a blank character ' ' instead
	# of checking for whether it should be a '.' character
	win = True
	for position in win_positions:
		if level[position] == ' ':
			level[position] = '.'
		if level[position] != '$':
			win = False

	# exit the game if victorious
	if win:
		return

	# draw each line of the level on the screen, centered:
	for y in range(0, len(level) / level_width):
		screen.addstr(y + len(text_items), 0, str.center( str.join('', 
			level[ y*level_width : (y + 1) * level_width ]), text_width ))

	# wait for input:
	c = screen.getch()
	if (c == curses.KEY_LEFT):
		move_horizontal(-1)
	elif(c == curses.KEY_RIGHT):
		move_horizontal(1)
	elif(c == curses.KEY_UP):
		move_vertical(-1)
	elif(c == curses.KEY_DOWN):
		move_vertical(1)
	else:
		return

	loop(screen)

# read the level
read_level('level.xsb')

# initialize curses
curses.initscr()
curses.curs_set(0)
curses.wrapper(loop)
curses.endwin()