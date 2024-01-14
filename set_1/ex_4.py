import numpy as np

np.set_printoptions(suppress=True)

linear_vector = np.linspace(0, 1, 10)
print(f'linearly spaced vector: {linear_vector}\n')

linear_matrix = np.linspace(0, 5, 100).reshape(10, 10)
print(f'linearly spaced 10x10 matrix:\n{linear_matrix}\n')

increment = 5 / 99
linear_list = []
linear_linear_list = []
for x in range(0, 10):
	for y in range(1, 11):
		linear_list.append(((x * 10) + y - 1) * increment)
		if y % 10 == 0:
			linear_linear_list.append(linear_list)
			linear_list = []
			break
print(f'linearly spaced 10x10 list:\n{linear_linear_list}')