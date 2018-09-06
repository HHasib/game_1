from sys import exit



	
def points(scr):
	score = 0
	score = scr + score
	return score
	
def dead():
	
	exit(0)
	
	
	
def start():
	
	print "Each right answer gains 10 points."
	print "Each wrong answer deducts 10 points."
	print "use skip if you do not know the answer. That will deduct 5 points."
	print "Are you ready?"
	
	
	ans = raw_input("> ")
	
	if ans == "yes":
		first_question()
	elif ans == "no":
		dead()
	else:
		print "Sorry. I did not get that."
		
				
def first_question():
	
	print "What goes up when rain comes down?" #displays the question
	
	
	ans = raw_input("> ") #takes user input
	
	if ans == "umbrella": #if correct answer moves to next question and adds point
		print "congratz! you have got it correct."
		points(10)
		second_question()
		
	elif ans == "skip":
		points(-5)
		second_question()	
	else:
		points(-10)
		print "Answer: umbrella"
		second_question()
		
	
def second_question():
	print "I have a head, a tail but no body. Who am I?"
	
	ans = raw_input("> ")
	
	if ans == "coin":
		print "congratz! you have got it correct."
		points(10)
		third_question()
		
	elif ans== "skip":
		points(-5)
		third_question()
		
	elif ans == "exit":
		dead()
	else:
		points(-10)
		print "The answer is: coin"
		third_question()
	
def third_question():

	print "I have keys but no locks, I have a space but no room, You can enter, but can't go outside. What am I?"
	
	ans = raw_input("> ")
	
	if ans == "keyboard":
		print "congratz! you have got it correct."
		points(10)
		dead()
		
		
	elif ans== "skip":
		points(-5)
		dead()
		
	elif ans=="exit":
		dead()
	else:

		points(-10)
		dead()
	

start()
