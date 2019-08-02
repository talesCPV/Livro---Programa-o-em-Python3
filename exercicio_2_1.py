#!/usr/bin/env python3

import sys, unicodedata

def print_unicode_table(word):
	print('decimal  hex  chr  {0:^40}' .format('name'))
	print('-------  ---  ---  {0:-<40}' .format(''))

	code = ord(' ')
	end = sys.maxunicode

	while code < end:
		c = chr(code)
		name = unicodedata.name(c, '*** unknown ***')
		i = 0
		flag = True
		while i < len(word):
			if not (word[i] is None or word[i].lower() in name.lower()):
				flag = False
			i += 1

		if flag:
			print('{0:7}  {0:5X}  {0:^3c}  {1}' .format(code, name.title()))

		code += 1

word =  None
if len(sys.argv) > 1:
	if sys.argv[1] in ('-h' or '--help'):
		print('usage: {0} [string]' .format(sys.argv[0]))
		word = 0
	else:
		word = sys.argv[1:]
if len(word) > 0:
	print_unicode_table(word)