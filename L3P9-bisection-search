print "Please think of a number between 0 and 100!"
top = 100
bottom = 0
guess = 50 # (top - bottom) / 2 + bottom

while True:
	print "Is your secret number %r?" % guess
	print "Enter 'h' to indicate the guess is too high.",
	print "Enter 'l' to indicate the guess is too low.",
	print "Enter 'c' to indicate I guessed correctly.",
	feedback = raw_input()
	
	if feedback == 'h':
		top = guess
		
	elif feedback == 'l':
		bottom = guess
		
	elif feedback == 'c':
		print "Game over. Your secret number was %r." % guess
		break
		
	else:
		print "I don't understand. 'h', 'l', or 'c' only."
		
	guess = (top - bottom) / 2 + bottom
