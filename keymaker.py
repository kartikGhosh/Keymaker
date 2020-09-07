#! python 3

# Keymaker.py -> A simple CD Key Generator, written in python knight Vi.

import random, sys

class keymaker():

	def __init__(self):
		global i
		i = int(input("How many serial codes are you looking for? \n"))
		print("")
		self.main(i)
# This allows the user to input how many iterations of a key generation they'd like.

	def main(self, count):
		""" Our main iteration function, using simple 
		capital letters, along with the numbers 0-9 """
		knight = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

		for i in range(count):
			print('-'.join(''.join(random.choice(knight) for _ in range(3)) for _ in range(5)))
# Our loop used to iterate through the range of our count parameter, and print our keys to the console
## in sequences of 5 letters/numbers.

		print("\nCreated {} serial keys for you, Knight_VI.".format(count))

# And there's our print statement.

if __name__ == '__main__':
	app = keymaker()
