import numpy as np

numbers = [23, 34, 54, 31, 75]
data1 = np.array(numbers)
numbers = [33, 56, 78, 65, 97]
data2 = np.array(numbers)
numbers = [41, 32, 11, 39, 51]
data3 = np.array(numbers)
three_by_three = np.array([data1, data2, data3])
print(f'3x5 matrix:\n{three_by_three}\n')

eight_by_sixteen = np.arange(128, 256).reshape(8, 16)
print(f'8x16 array:\n{eight_by_sixteen}\n')

ten_by_ten = np.arange(1, 101).reshape(10, 10) * 0.05
print(f'10x10 array:\n{ten_by_ten}')