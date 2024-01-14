import numpy as np

zeros = np.zeros(15).astype(int)
ones = np.ones(15).astype(int)
sevens = np.ones(15).astype(int) * 7
numbers = np.arange(100, 151)
high_numbers = np.arange(1900, 2022)
even_numbers = np.arange(0, 101, 2)
years = np.arange(1950, 2021)
years = years[years % 4 == 0]

print(f'array of zeros: {zeros}\n')
print(f'array of ones: {ones}\n')
print(f'array of sevens: {sevens}\n')
print(f'numbers from 100 to 150: {numbers}\n')
print(f'numbers from 1900 to 2021: {high_numbers}\n')
print(f'even numbers: {even_numbers}\n')
print(f'years divisible by 4: {years}')