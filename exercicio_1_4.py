#!/usr/bin/env python3

import random

def get_int():
	while True:
		try:
			val = input('Digite um número de 1 a 10:')
			num = int(val)
			if  1 <= num <= 10:
				return num
			else:
				print('O número deve ser de 1 a 10 linhas')
		except ValueError:
			if val == '':
				return 5
			else:
				print('O valor digitado não é um número válido.')

artigos_m = ['o','um','algum','nenhum']
artigos_f = ['a','uma','alguma','nenhuma']
sujeito_m = ['gato','cachorro','homem','bode','galo','sapo','menino','computador']
sujeito_f = ['gata','cadela','mulher','cabra','galinha','cobra','menina','cadeira']
verbo     = ['atropelou','comeu','deixou','passou','programou','arrumou','comprou']

i = 0
tot = get_int()

print()

while i < tot:
	frase = '     '
	genero = random.randint(0,1)

	if genero:
		frase += random.choice(artigos_f) + ' ' 
		frase += random.choice(sujeito_f) + ' '
	else:
		frase += random.choice(artigos_m) + ' ' 
		frase += random.choice(sujeito_m) + ' '

	frase += random.choice(verbo) + ' '
	genero = random.randint(0,1)

	if genero:
		frase += random.choice(artigos_f) + ' ' 
		frase += random.choice(sujeito_f) + ' '
	else:
		frase += random.choice(artigos_m) + ' ' 
		frase += random.choice(sujeito_m) + ' '

	print(frase)
	i += 1

print()