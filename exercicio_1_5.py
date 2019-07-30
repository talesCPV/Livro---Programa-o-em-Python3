#!/usr/bin/env python3

def ordenar(old_list):
	new_list = []

	while len(old_list) > 0:
		i = 0
		menor = 0
		while i < len(old_list):
			if old_list[i] < old_list[menor]:
				menor = i
			i += 1

		new_list.append(old_list[menor])
		old_list.remove(old_list[menor])

	return new_list




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

				ord_lista = ordenar(lista)
				val_central = 0
				if (len(ord_lista)%2):	
					val_central = ord_lista[len(ord_lista)//2]
				else:
					val_central = ((ord_lista[len(ord_lista)//2] + (ord_lista[len(ord_lista)//2]-1))/2)


				print('números:',ord_lista)
				print('qtd:',len(ord_lista),'soma:',soma,'min:',minimo,' max:',maximo,' média:',soma/len(ord_lista),'valor central:',val_central)

			break
		else:
			print('Valor digitado não corresponde a um número inteiro.')








