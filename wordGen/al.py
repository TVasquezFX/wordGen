import random


lower  = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper() 
num = "0123456789"
sym = "[]{}()*%@?!"

all = lower + upper + num + sym
length = 30

for x in range(6):
	password = "".join(random.sample(all,length))
	print(password)
