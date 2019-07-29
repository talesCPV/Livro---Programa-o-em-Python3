#!/usr/bin/env python3

import sys

zero   = ['  **  ',' *  * ','*    *','*    *','*    *',' *  * ','  **  ']
um     = ['  * ',' ** ','  * ','  * ','  * ','  * ','****']
dois   = [' ***  ','*   *','    *','   * ','  *  ',' *   ','*****']
tres   = [' ****','*    *','    * ','   ** ','     *','*    *',' **** ']
quatro = ['    *','   **','  * *',' *  *','*****','    *','    *']
cinco  = ['*****','*    ','***  ','   **','    *','*   *',' *** ']
seis   = [' *** ','*   *','*    ','**** ','*   *','*   *',' *** ']
sete   = ['*****','*   *','   * ','  *  ',' *   ','*    ','*    ']
oito   = [' *** ','*   *','*   *',' *** ','*   *','*   *',' *** ']
nove   = [' *** ','*   *','*   *',' ****','    *','*   *',' *** ']

Digitos = [zero,um,dois,tres,quatro,cinco,seis,sete,oito,nove]

def change_dig(str_dg,int_dg):
	i = 0
	resp = ''
	while i < len(str_dg):
		if not str_dg[i] == ' ':
			resp += str(int_dg)
		else:
			resp += str_dg[i]
		i += 1
	return resp


try:
	my_args = sys.argv[1]
	row = 0
	while row < 7:
		col = 0
		line = ''
		while col < len(my_args):
			dg = int(my_args[col])
			line += change_dig(Digitos[dg][row],dg) + '  '
			col += 1
		print(line)
		row += 1

except IndexError:
	print('Parâmetros incorretos.')
	



