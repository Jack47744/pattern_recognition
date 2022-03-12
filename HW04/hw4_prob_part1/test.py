import numpy as np
a = np.zeros((4, 2))
b = np.array([0.1, 0.2, 0.11, 0.22])
b = b.reshape((len(b), -1))
print(a+b)