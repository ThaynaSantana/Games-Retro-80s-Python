import random
import os
import time
print("VITAL MESSAGE")
print("HOW DIFFICULT? (4-10)")
d = int(input())
while d<4 or d>10:
	print("HOW DIFFICULT? (4-10)")
	d = int(input())
secret_message=""
i=1
while i<=d:
	secret_message=secret_message+chr(random.randrange(26)+65)
	i+=1
os.system('cls')
print("SEND THIS MESSAGE:")
print(secret_message)
time.sleep(d-2)
os.system('cls')
guess=input().upper()
if guess==secret_message:
	print("MESSAGE CORRECT")
	print("THE WAR IS OVER!")
else:
	print("YOU GOT IT WRONG")
	print("YOU SHOULD HAVE SENT:")
	print(secret_message)
