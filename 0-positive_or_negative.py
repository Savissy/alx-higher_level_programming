#!/usr/bin/pyton3
import random
number = random.randit(-10, 10)
if number > 0:
	print(f"{number:d} is positive")
elif number == 0:
	print(f"{number:d} is zero")
else:
	print(f"{number:d} is negative")
