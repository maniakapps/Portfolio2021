import numpy as np
x = np.arange(100)
x2 = x.reshape(100, 1)
y = np.ones(50)
z = np.ones((100, 100))

r = x2 * z
print(r)