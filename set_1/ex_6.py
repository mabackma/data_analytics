import numpy as np

dataset = np.arange(1, 37).reshape(6, 6)
print(f'dataset matrix:\n{dataset}\n')

lower_right = dataset[3:, 2:]
print(f'slice of the matrix:\n{lower_right}\n')

column_slice = dataset[:4, 3:4]
print(f'column slice from the matrix:\n{column_slice}\n')

row_slice = dataset[2:3].transpose()
print(f'row slice from the matrix:\n{row_slice}\n')

lower_half = dataset[3:]
print(f'lower half of matrix:\n{lower_half}\n')