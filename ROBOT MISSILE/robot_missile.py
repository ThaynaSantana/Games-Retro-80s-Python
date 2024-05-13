import random
chances=1
print("ROBOT MISSILE")
print("TYPE THE CORRECT CODE")
print("LETTER (A-Z) TO")
print("DEFUSE THE MISSILE.")
print("YOU HAVE 4 CHANCES")
secret_code_number = random.randrange(26)+1+64
secret_code = chr(secret_code_number)
while chances<=4:
	chances+=1
	guess=ord(input().upper())
	if guess==secret_code_number:
		print("TICK...FZZZZZ...CLICK...")
		print("YOU DID IT!")
	elif guess<secret_code_number:
		print("LATER")
	elif guess>secret_code_number:
		print("EARLIER")
	print(" THAN {}".format(chances))
print("BOOOOOOOMMMM...")
print("YOU BLEW IT.")
print("THE CORRECT CODE WAS {}".format(secret_code))
