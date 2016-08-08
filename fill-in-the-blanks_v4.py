"""
 IPND Stage 2 Final Project

 You've built a Mad-Libs game with some help from Sean.
 Now you'll work on your own game to practice your skills and demonstrate what you've learned.

 For this project, you'll be building a Fill-in-the-Blanks quiz.
 Your quiz will prompt a user with a paragraph containing several blanks.
 The user should then be asked to fill in each blank appropriately to complete the paragraph.
 This can be used as a study tool to help you remember important vocabulary!

 Note: Your game will have to accept user input so, like the Mad Libs generator,
 you won't be able to run it using Sublime's `Build` feature.
 Instead you'll need to run the program in Terminal or IDLE.
 Refer to Work Session 5 if you need a refresher on how to do this.

 To help you get started, we've provided a sample paragraph that you can use when testing your code.
 Your game should consist of 3 or more levels, so you should add your own paragraphs as well!
"""
quiz_options = ['''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''','''___1___ is a ___2___ ___3___ that Udacity use to ___4___ the
basics of ___2___.''',''' Learning ___1___ can be hard and frustrating but once you ___2___, it can be very ___3___. ___1___ opens a 
new world of ___4___. Never ending ___4___''']

"""
 The answer for ___1___ is 'function'. Can you figure out the others?

 We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
 A .pyc file is a Python file that has been translated into "byte code".
 This means the code will run the same as the original .py file, but when you open it
 it won't look like Python code! But you can run it just like a regular Python file
 to see how your code should behave.

 Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
 In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
 How can you adapt that design to work with numbered blanks?

 If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
 """

answers = ["function","variables","true","list"],["Python","programming","language","teach"],["programming","succeed","rewarding","possibilities"] # nested lists of possible answers.
levels = ["easy","normal","hard"] 
questions =["___1___","___2___","___3___","___4___"] #available gaps to fill
selected_answer = [] # Current active answers based on level selection
selected_question = "" # Current active questions based on level selection

def user_selection(user_input,levels):
	# Loads matching question and answers (based on user input) into global variables. 
	counter = 0
	global selected_question
	global selected_answer
	for level in levels:
		if level.lower() == user_input.lower():
			selected_question = quiz_options[counter]
			selected_answer = answers[counter]
			return counter
		else:
			counter += 1
	return None


def answer_checker(user_input,answer):
	# Returns user input if the answer is correct and None if the answer is wrong
	if user_input.lower() == answer.lower():
		return user_input
	else:
		return None

def fill_the_blanks (selected_answer,questions):
# Check the answer and if correct, fill in the blanks and move to next question. If not correct, allow for 5 more attempts. 
	counter = 0
	global selected_question
	attempts = 5
	while attempts > -1 and counter < len(questions):
		user_input = raw_input("Please type your answer for question " + questions[counter] + ":")
		if answer_checker(user_input,selected_answer[counter]) == user_input:
			print "Good answer! \n" 
			selected_question = [w.replace(questions[counter],selected_answer[counter]) for w in selected_question] # Replaces question for answer
			attempts = 5
			counter += 1
			print " ".join(selected_question) + "\n"
		else:
			print "Wrong answer"
			print "You have " + str(attempts)+ " attempts remaning"
			attempts += -1
	return attempts_checker(attempts)
	

def attempts_checker(attempts):
	# Returns the below based on remaning attempts.
	if attempts < 0:
		return "Best Luck Next Time"
	else:
		return "Congrats, You are a hero"


def play_game(quiz_options,questions,levels):
	counter = 0
	#main function to run the game.
	global selected_question
	global selected_answer
	user_input = ""	

	# Asking user to select level until an available level is selected.
	while user_selection(user_input,levels) == None:
		user_input = raw_input("Please select one of the following levels: " + ", ".join(levels) + "\n")
	counter += user_selection(user_input,levels)

	print "You have selected " + user_input + "\n"

	selected_question = selected_question.split()
	print " ".join(selected_question)

	return fill_the_blanks (selected_answer,questions)



print play_game(quiz_options,questions,levels)

	



