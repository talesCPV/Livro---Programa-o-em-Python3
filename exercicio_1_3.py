#!/usr/bin/env python3

import random

artigos_m = ['o','um','algum','nenhum']
artigos_f = ['a','uma','alguma','nenhuma']
sujeito_m = ['gato','cachorro','homem','bode','galo','sapo','menino','computador']
sujeito_f = ['gata','cadela','mulher','cabra','galinha','cobra','menina','cadeira']
verbo     = ['atropelou','comeu','deixou','passou','programou','arrumou','comprou']

i = 0
while i < 6:
	genero = random.randint(0,1)

	if genero:
		frase  = random.choice(artigos_f) + ' ' 
		frase += random.choice(sujeito_f) + ' '
	else:
		frase  = random.choice(artigos_m) + ' ' 
		frase += random.choice(sujeito_m) + ' '

	frase += random.choice(verbo) + ' '
	genero = random.randint(0,1)

	if genero:
		frase += random.choice(artigos_f) + ' ' 
		frase += random.choice(sujeito_f) + ' '
	else:
		frase  = random.choice(artigos_m) + ' ' 
		frase += random.choice(sujeito_m) + ' '

	print(frase)
	i += 1