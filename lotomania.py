#!/usr/bin/env python3

import sys

def get_line(line):
	i = 0
	field = ''
	resp = []
	flag = True
	count = 0
	while i < len(line):
		if line[i] == ' ' and flag:
			flag = False
			count += 1
			resp.append(field)
			field = ''
		elif line[i] != ' ' and not flag:
			flag = True
		else:
			field += line[i]

		if count == 22:
			return resp

		i += 1


def cria_lista():
	resp = []
	for i in range(100):
		resp.append(0)
	return resp


def add_estatistic(line):
	i = 2
	while i < len(line):
		estatistic[int(line[i])] += 1
		i += 1


def num_partner():
	for i in range(100):
		lista = cria_lista()
		for x in data:
			if '{0:0>2}'.format(i) in x:
				for y in x:
					lista[int(y)] += 1

		x = 0
		while x < len(lista):
			lista[x] = lista[x]/(len(lista)/100)
			x += 1

		maior = []
		while len(maior) < 20:
			tam = len(maior)
			x=0
			while tam == len(maior):
				if not x in maior:
					maior.append(x)
				x += 1

			x = 0
			while x < len(lista):
				if not x in maior and lista[x] >= lista[maior[-1]]:
					maior[-1] = x
				x += 1


		print('Para {0:0>2} -> {1}'.format(i,maior[1:]))



estatistic = cria_lista()

lines = 0
data = []

print('-' * 142)
print('{0:^8} {1:^12} {2:^120}'.format('N.Sort','Data','Numeros Sorteados'))
print('-' * 142)

while True:
    try:
    	line = get_line(input())
    	if line is not None:
    		add_estatistic(line)    		
	    	print(line)
	    	data.append(line[2:])
	    	lines += 1

    except EOFError:
        break


print('Quantidade de sorteios:', lines)
print('-' * 150)
print('Porcentagem de Ocorrências:')
print('-' * 150)

for x in range(10):
	row = ''
	for y in range(10):
		i = x * 10 + y
		row += '{0:0>2} -> {1:0>5.2f}% | '.format(i,(estatistic[i]/(lines/100)))
	print(row)
print('-' * 150)
print('Melhores Pares:')
print('-' * 150)

num_partner()
