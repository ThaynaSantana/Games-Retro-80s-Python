import random
import os
import time
print("A SENHA QUE VALE A VIDA OU MORTE")
print("QUAL DIFICULDADE? (4-10)")
d = int(input())
while d<4 or d>10:
	print("QUAL DIFICULDADE? (4-10)")
	d = int(input())
secret_message=""
i=1
while i<=d:
	secret_message=secret_message+chr(random.randrange(26)+65)
	i+=1
os.system('cls')
print("INSIRA ESTE CÓDIGO:")
print(secret_message)
time.sleep(d-2)
os.system('cls')
guess=input().upper()
if guess==secret_message:
	print("CÓDIGO CORRETO")
	print("TERMINOU A GUERRA!")
else:
	print("VOCÊ ENTENDEU ERRADO")
	print("VOCÊ DEVERIA TER ENVIADO:")
	print(secret_message)
