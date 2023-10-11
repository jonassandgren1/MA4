#!/usr/bin/env python3

from person import Person
from time import perf_counter as pc
import matplotlib.pyplot as plt
import numba


@njit
def main():
	f = Person(5)
	print(f.get())

	start = pc()
	f.set(7)
	print(f.fib())
	end = pc()
	print(f'fib in python took: {end-start} sec to run')

if __name__ == '__main__':
	main()
