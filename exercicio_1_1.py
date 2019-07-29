#!/usr/bin/env python3

import sys

zero   = ['  **  ',' *  * ','*    *','*    *','*    *',' *  * ','  **  ']
um     = ['  * ',' ** ','  * ','  * ','  * ','  * ','****']
dois   = [' ***  ','*   *','    *','   * ','  *  ',' *   ','*****']
tres   = [' **** ','*    *','    * ','   ** ','     *','*    *',' **** ']
quatro = ['    *','   **','  * *',' *  *','*****','    *','    *']
cinco  = ['*****','*    ','***  ','   **','    *','*   *',' *** ']
seis   = [' *** ','*   *','*    ','**** ','*   *','*   *',' *** ']
sete   = ['*****','*   *','   * ','  *  ',' *   ','*    ','*    ']
oito   = [' *** ','*   *','*   *',' *** ','*   *','*   *',' *** ']
nove   = [' *** ','*   *','*   *',' ****','    *','*   *',' *** ']

Digitos = [zero,um,dois,tres,quatro,cinco,seis,sete,oito,nove]

try:
	my_args = sys.argv[1]
	row = 0
	while row < 7:
		col = 0
		line = ''
		while col < len(my_args):
			dg = int(my_args[col])
			line += Digitos[dg][row] + ' '
			col += 1
		print(line)
		row += 1

except IndexError:
	print('Parâmetros incorretos.')
	



