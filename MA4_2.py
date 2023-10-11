#!/usr/bin/env python3

from person import Person
from time import perf_counter as pc
import matplotlib.pyplot as plt
from numba import njit

def fib(n):
	if n <= 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

@njit
def fib_numba(n):
	if n <= 1:
		return 1
	else:
		return fib_numba(n-1)+fib_numba(n-2)

def main():
	f = Person(5)
	print(f.get())
	pyTime = []
	numbaTime = []
	cppTime = []
	for i in range(47):
		# start = pc()
		# fib(i)
		# end = pc()
		# pyTime.append(end-start)
		# print(f'fib in python took: {end-start} sec to run')


		start = pc()
		fib_numba(i)
		end = pc()
		numbaTime.append(end-start)
		print(f'fib in python_numba took: {end-start} sec to run')
		
		start = pc()
		f.set(i)
		f.fib()
		end = pc()
		cppTime.append(end-start)
		print(f'fib in c++ took: {end-start} sec to run')

	plt.figure()
	plt.plot(range(20, 30), pyTime)  # Plot the chart 
	plt.plot(range(20, 30), numbaTime)  # Plot the chart
	plt.plot(range(20, 30), cppTime)  # Plot the chart
	plt.savefig("time.png") 
	plt.show()



if __name__ == '__main__':
	main()
