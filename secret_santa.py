#!/usr/bin/env python3

import sys
import random
import fire
from prettytable import PrettyTable


def usage():
	print(
		"""
Flags:
	--names            *REQUIRED* List of names to use for secret santa, comma separated.
	--help			   Display help and usage message.
		"""
		)

def masterFunc(names, help=''):
	if help:
		usage()
		sys.exit(0)
	if not names:
		print('!!! Missing names !!!')
		usage()
		sys.exit(1)

	giver_list = []
	recipient_list = []

	for name in names:
		giver_list.append(name)
		recipient_list.append(name)

	final_dict = {}
	for name in names:
		giver = name
		recipient = ''
		recipient = random.choice(recipient_list)
		while recipient == name:
			recipient = random.choice(recipient_list)
		recipient_list.remove(recipient)
		final_dict[giver] = recipient

	output_table = PrettyTable(['Giver Name', 'Recipient Name'])
	for key in final_dict:
		output_table.add_row([key,final_dict[key]])
	print(output_table)


if __name__ == '__main__':
	fire.Fire(masterFunc)