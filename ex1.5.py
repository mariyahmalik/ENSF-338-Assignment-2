import timeit 
import matplotlib.pyplot as plt
import numpy as np

#original code
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
elapsed_time = timeit.timeit(lambda : func(35), number = 1)
print(f'Elapsed time for original code: {elapsed_time} seconds')

fib_list = [func(n) for n in range(36)]

plt.plot(fib_list, label = "Fibonacci Numbers")
plt.xlabel("n")
plt.ylabel("fib(n)")
plt.title("Fibonacci Numbers Plot for Original Code")
plt.legend()
plt.show()

#improved code
def func(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n 
        return n
    else:
        memo[n] = func(n-1, memo) + func(n-2, memo)
        return memo[n]

elapsed_time = timeit.timeit(lambda : func(35), number = 1)
print(f'Elapsed time for improved code: {elapsed_time} seconds')

fib_list = [func(n) for n in range(36)]

plt.plot(fib_list, label = "Fibonacci Numbers")
plt.xlabel("n")
plt.ylabel("fib(n)")
plt.title("Fibonacci Numbers Plot for Improved Code")
plt.legend()
plt.show()