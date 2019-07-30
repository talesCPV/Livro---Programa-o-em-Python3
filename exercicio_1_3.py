#!/usr/bin/env python3

import random

artigos = ['o','a','os','as','um','uma','algum','nenhum','alguma','nenhuma']
sujeito = ['gato','cachorro','homem','mulher','cabra','galinha','sapo','menino','menina','computador']
verbo   = ['atropelou','comeu','deixou','passou','programou','arrumou']

frase  = random.choice(artigos) + ' ' 
frase += random.choice(sujeito) + ' '
frase += random.choice(verbo) + ' '
frase += random.choice(artigos) + ' '
frase += random.choice(sujeito)

print(frase)
