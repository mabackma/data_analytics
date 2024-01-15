import numpy as np
import random
import numpy.ma as ma

numbers = np.arange(1, 51)

faulty_indexes = []
while True:
    rand = random.randint(0, len(numbers) - 1)
    if rand not in faulty_indexes:
        faulty_indexes.append(rand)
    if len(faulty_indexes) >= 10:
        break

for i in range(len(numbers)):
    if i in faulty_indexes:
        numbers[i] = -100

five_by_ten = numbers.reshape(10, 5)

# Create a masked array 
masked_array = ma.masked_equal(five_by_ten, -100)
print(f'masked array:\n{masked_array}')
