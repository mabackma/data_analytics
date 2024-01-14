import numpy as np

np.set_printoptions(suppress=True)

numbers = [5, 16, 9, 2, 19, 18, 11, 7]
data = np.array(numbers)
index = data.argmax()
print(f'index of largest value: {index}\n')

seven_seven_matrix = np.arange(1, 50).reshape(7, 7)
print(f'7x7 matrix:\n{seven_seven_matrix}\n')

seven_list = []
seven_seven_list = []
for x in range(0, 7):
	for y in range(1, 8):
		seven_list.append((x * 7) + y)
		if y % 7 == 0:
			seven_seven_list.append(seven_list)
			seven_list = []
			break
print(f'7x7 list:\n{seven_seven_list}\n')

random_matrix = np.random.rand(8, 8) * 5
print(f'random matrix:\n{random_matrix}\n')

random_normal_matrix = np.random.randn(8, 8)
print(f'random matrix with standard normal distribution:\n{random_normal_matrix}')