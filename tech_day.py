

q1_correct = ["linux", "redhat", "unix", "red hat"]
q2_correct = ["bash"]
q3_correct = ["nano", "vim", "vi", "emacs", "ed", "sed"]
q4_correct = ["makefile", "make file"]
q5_correct = ["git", "svn", "mercurial", "subversion"]
q6_correct = ["compiled", "interpreted"]
q7_correct = ["header", "header files", "headers"]
q8_correct = ["main", "main function"]
q9_correct = [";", "semicolon", "semi colon"]
q10_correct = ["cout", "printf"]
q11_correct = ["int", "double", "long", "char", "bool", "short", "float"]
q12_correct = ["g++", "gcc", "clang"]
q13_correct = ["stackoverflow", "stackoverflow.com", "stack overflow"]





def question_grade(user_answer, correct_answers):
	while user_answer.lower() not in correct_answers:
		user_answer = raw_input("Sorry that's incorrect. Try again: ")




def main():
	'''
	main program. Displays questions.
	'''
	print "Hello, World! Computer Science is all about solving problems efficently. Engineers normally work in teams, so today you'll work with your team to answer these questions. To get started press enter when told to by the instructor."
	raw_input("Press Enter to continue...")
	print "First question: every computer runs on an operating system. What operating system is this computer running?"
	print "Press enter after you\'ve typed your answer"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q1_correct)
	print "Correct! This computer runs RedHat linux."
	print "One of the things people use on Linux is a terminal. In fact this program is running inside the terminal right now."
	print "Terminals have things called shells that execute your commands. What type of shell is this running?"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q2_correct)
	print "Correct! This shell uses BASH. There's tons of other shells out there like zsh and ksh that each have different features."
	print "A big part of computer science is writing code. This program, for instance, is written in Python."
	print "To write code you normally need a text editor. There are some text editors that can be used directly in the terminal! Name one"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q3_correct)
	print "Fantastic! Now that our code has been written we need a way to compile it. Fortunately you can create a file that specifies commands for compiling your code. What is this file called?"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q4_correct)
	print "Right! A Makefile is a pretty nifty file that lets us just type make instead of retyping all the compiler commands."
	print "A common thing we do while we code is use a source control system. Name a source control system! Note that there are lots, so if your answer is incorrect try a more popular system."
	user_answer = raw_input()
	question_grade(user_answer.lower(), q5_correct)
	print "Great! We've gone over how to write code and how to have source control. But how do we run it? First, we need to know the differences between programming languages."
	print "There's two major types of languages. Name one! Hint: Python is an example of one type and C++ is an example of another."
	user_answer = raw_input()
	question_grade(user_answer.lower(), q6_correct)
	print "Way to go! So there's interpreted languages and compiled languages. Let's talk about a popular compiled language, C++"
	print "The start of most C++ programs include a certain type of file. Something like #include <iostream>."
	print "What are these files called?"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q7_correct)
	print "Fantastic! These are header files and they contain names of functions (called function headers) or full functions for our program to run."
	print "Now there's one specific function every C++ program needs. What's this function called?"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q8_correct)
	print "You're on fire! Every C++ program needs a main fuction to run. The cool part is your program can have a ton of files but there will always be one file with a main function!"
	print "When you write C++ code you can write a comment, a conditional and a regular statement. All statements need to end the same way, like how you would end a sentence with a period. How do you end statements in C++?"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q9_correct)
	print "Nice! Fun fact, sometimes people forget to add the semicolon and spend hours debugging trying to figure out why their code doesn't run."
	print "Sometimes you want to print text to standard output, which in this case would be the terminal. Assuming we've already declared that we're using the standard namespace how do we write to standard output?"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q10_correct)
	print "Yep! We typically use cout to print to standard output. We can print something in our main function by typing cout << \"Hello, World!\";"
	print "Programs also have variables. Variables can be either a primative type or a user defined object. Name one C++ primitive type!"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q11_correct)
	print "There's definitely quite a few built in types. After we've built our program we need to compile it. What compiler do we use to compile C++?"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q12_correct)
	print "Woohoo! Okay last question. Programmers use one website a ton, what's the name of the website?"
	user_answer = raw_input()
	question_grade(user_answer.lower(), q13_correct)
	print "Good job! Those are all the questions for this quiz. If your team is finished yell \"StackOverflow!\""
main()
