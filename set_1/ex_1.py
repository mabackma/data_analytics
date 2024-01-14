ones = []
sevens = []
for x in range(0, 15):
	ones.append(1)
	sevens.append(7)

high_numbers = []
for x in range(100, 151):
	high_numbers.append(x)

even_numbers = []
for x in range(0, 101):
	if x % 2 == 0:
		even_numbers.append(x)

years = []
for x in range(1950, 2021):
	if x % 4 == 0:
		years.append(x)

print(f'list of ones: {ones}\n')
print(f'list of sevens: {sevens}\n')
print(f'numbers from 100 to 150: {high_numbers}\n')
print(f'even numbers: {even_numbers}\n')
print(f'years divisible by 4: {years}')