#!/usr/bin/env python3

import os,sys

# git init
# git add exercicio_1_1.py
# git commit -m "first commit"
# remote add origin https://github.com/talesCPV/Livro---Programa-o-em-Python3.git
# git push -u origin master

#try:
prg = sys.argv[1]
rep = sys.argv[2]
os.system('git init')
os.system('git add ' + prg)
os.system('git commit -m' + rep)
os.system('remote add origin https://github.com/talesCPV/Livro---Programa-o-em-Python3.git')
os.system('git push -u origin master')
os.system('talesCPV')

#except:
#	print(err)