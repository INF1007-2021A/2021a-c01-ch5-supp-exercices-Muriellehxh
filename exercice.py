#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	list_sous_tot = []
	for tup in data:
		list_sous_tot.append(tup[2]*tup[1])

	formated_sous_tot = format(sum(list_sous_tot), '.2f')
	taxes = format(0.15 * float(formated_sous_tot), '.2f')
	total = format(float(taxes) + float(formated_sous_tot), '.2f')


	return f"{name}\nSOUS TOTAL{' '*(5)}{formated_sous_tot} $\n" \
		   f"TAXES{' '* 10}{taxes} $\n" \
		   f"TOTAL{' '* 10}{total} $"


def format_number(number, num_decimal_digits): # 	REVOIR !!!
	decimal_part = number % 1.0
	print(decimal_part)

	return []



def get_triangle(num_rows):

	n = 1
	width = num_rows * 2 + 1

	print('+' * width)
	for row in range(0, num_rows):
		A = 'A' * n
		space = (width - 2 - n)//2
		n+=2
		print( f"+{' '*space}{A}{' '*space}+" )
	print('+' * width)


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
