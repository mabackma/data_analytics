import numpy as np

years = np.random.randint(low=2010, high=2020, size=10)
prices = np.random.randint(low=2000, high=60000, size=10)

sorter = np.argsort(years)
print(f'sorted years: {years[sorter]}')
print(f'sorted prices: {prices[sorter]}')