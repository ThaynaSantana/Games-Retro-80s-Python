import random
chances=1
print("MÍSSIL ROBOTICO")
print("INSIRA O CÓDIGO CORRETO")
print("UMA LETRA DE (A-Z)")
print("DESMONTE O MÍSSIL")
print("VOCÊ TEM 4 CHANCES")
secret_code_number = random.randrange(26)+1+64
secret_code = chr(secret_code_number)
while chances<=4:
	chances+=1
	guess=ord(input().upper())
	if guess==secret_code_number:
		print("TICK...FZZZZZ...CLICK...")
		print("VOCE CONSEGUIU!")
	elif guess<secret_code_number:
		print("MAIS")
	elif guess>secret_code_number:
		print("MENOS")
	print(" THAN {}".format(chances))
print("BOOOOOOOMMMM...")
print("VOCÊ ESTRAGOU COM TUDO.")
print("O CODIGO CORRETO É {}".format(secret_code))
