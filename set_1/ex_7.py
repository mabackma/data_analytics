import numpy as np

np.set_printoptions(suppress=True)

dataset = np.arange(1, 50).reshape(7, 7)
print(f'dataset:\n{dataset}\n')

added_fifty = dataset + 50
print(f'added 50 to all values:\n{added_fifty}\n')

dataset_sum = np.sum(dataset)
print(f'sum of dataset: {dataset_sum}')

odd_sum = np.sum(dataset[dataset % 2 == 1])
print(f'sum of odd values from dataset: {odd_sum}')

deviation = np.std(dataset)
print(f'standard deviation of dataset: {deviation}')

row_total = np.sum(dataset, axis=1)
print(f'sum of values by row: {row_total}')

column_total = np.sum(dataset, axis=0)
print(f'sum of values by column: {column_total}\n')

list_dataset = dataset.tolist()
list_total = 0
for nested_list in list_dataset:
	for x in nested_list:
		list_total += x
print(f'sum from list: {list_total}')

list_row_total = []
for nested_list in list_dataset:
	total = 0
	for x in nested_list:
		total += x
	list_row_total.append(total)
print(f'sum by row from list: {list_row_total}')

list_column_total = []
list_transposed_dataset = dataset.transpose().tolist()
for nested_list in list_transposed_dataset:
	total = 0
	for x in nested_list:
		total += x
	list_column_total.append(total)
print(f'sum by column from list: {list_column_total}')