import numpy as np

fifteen_by_fifteen = np.arange(1, 226).reshape(15, 15)

with open("matrix.txt", 'w') as f:
    f.write(str(fifteen_by_fifteen))
f.close()