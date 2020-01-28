import time
import sys
import re
from datetime import datetime
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def curtime():
	now = datetime. now()
	current_time = now. strftime(f"{bcolors.OKGREEN}%H:%M:%S{bcolors.ENDC}")
	print("Current Time =", current_time)
def processbar():
	toolbar_width = 40
	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1))
	for i in range(toolbar_width):
		time.sleep(0.1)
		sys.stdout.write("-")
		sys.stdout.flush()
	sys.stdout.write("]\n")
print(f"""{bcolors.WARNING}
				WELCOME TO THE DEMONS PLACE
				    DARE NOT TO ENTER!!
Imagine's dragon was captured by the demons. Imagine needs your help to free his dragon from the cruel demons by helping him get past the doors on the way to the dragon.
     {bcolors.ENDC} """) 

print(f"{bcolors.OKGREEN}Type 'Ready' to begin the challenge.{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}For help reach out to any organiser near you , if you dont find one yell 'Help' any one of us hears you (if that was loud enough will help you)༼ つ ◕_◕ ༽つ{bcolors.ENDC}")
while True: 
	Start = input("Are you Ready:")
	if Start == "Ready":
		print("Setting Up The Environment!")
		processbar()
		print("""
		Quest 1
		Regex : d[a-z][a-z][a-z][a-z]@[a-z][a-z][a-z][a-z][a-z]\.[a-z][a-z][a-z]
		"""
		)
		email = input(">>:")
		match = re.findall("d[a-z][a-z][a-z][a-z]@[a-z][a-z][a-z][a-z][a-z]\.[a-z][a-z][a-z]",email)
		if len(match) > 0:
			print("Success, You Got It Right")
			processbar()
			print("""
			From : demon@iambad.com
			To   : goodman@sentinel.com

			Subject : Password to first lock

			Message : cGFzc3dvcmQK
			"""
			)
			print("Got Access to Demons email")
			print("Even Demons have started using email these days ◕︵◕")
			gate1 = input("Enter the passowd for gate1:")
			if gate1 == "password":
				print("""\╭☞ \╭☞""")
				print("Moving to Gate2")
				processbar()	
				print("""
				Quest 2
				Regex : \D\d\d\d\D
				"""
				)
				nice = input(">>:")
				match2 = re.findall("\D\d\d\d\D",nice)
				if len(match2) > 0:
					print("Success, You Got It Right")
					print("This looks like demons email password")
					print("Use these creds to login to his email")
					email2 = input("Email:")
					if (email2 == email):
						password = input("Password:")
						if (password == nice ):
							print("OOPS , Demon changes his password yester day night")
							print("""
							Quest 3
Regex1 : \s
							""")
							inin1 = input(">>:")
							matchinin1 = re.findall("\s",inin1)
							if len(matchinin1) > 0:

								print("New Password of demon is : i_am_not_so_bad")
								print("Use demons actual mail and password to login to his email")
								actemail = input("Email:")
								if actemail == "demon@iambad.com":
									actpass = input("Password:")
									if actpass == "i_am_not_so_bad":
										print("Verifing Credentials")
										processbar()
										print("Logging In")
										processbar()
										print("Login successful")
										print("""
				Yay , Our Dragon is free now!!!!
										\||/							                
										|  @___oo
						      			/\  /\   / (__,,,,|
						     			) /^\) ^\/ _)
						    			)   /^\/   _)
						     			)   _ /  / _)
						 		/\  )/\/ ||  | )_)
							       <  >      |(,,) )__)
						                ||      /    \)___)							                     | \____(      )___) )___
						                \______(_______;;; __;;;

											""")
										curtime()
										break
									else:
										break
								else:
									break
							else:
								break				
						else:
							print("Wrong password")
							break
					else:
						break
				else:
					break	
		else:
			break
