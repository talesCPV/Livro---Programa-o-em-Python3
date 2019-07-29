#!/usr/bin/env python3

lista = []
while True:
	try:
		val = input('Digite um valor ou "Enter" pra finalizar: ')
		dg = int(val)
		lista.append(dg)
	except:
		if val == '':
			if len(lista) > 0:
				i = 0
				soma = 0
				minimo = lista[0]
				maximo = 0
				while i < len(lista):
					soma += lista[i]
					if lista[i] <= minimo:
						minimo = lista[i]
					elif lista[i] >= maximo:
						maximo = lista[i]

					i += 1

				print('números:',lista)
				print('qtd:',len(lista),'soma:',soma,'min:',minimo,' max:',maximo,' média:',soma/len(lista))

			break
		else:
			print('Valor digitado não corresponde a um número inteiro.')







