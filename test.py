from random import seed
from random import random
import numpy as np
import matplotlib.pyplot as plt

plt.plot([1, 2, 4, 8, 16])

plt.savefig('plot.png')

# seed random number generator
seed(1)
# generate some random numbers
print(random(), random(), random())
seed(1)
print(random(), random(), random())
print(random(), random(), random())
a = 1
b = 3
c = a + b
print(c)
array1 = np.array([1, 2, 3, 4, 5])
print(array1, array1[0])
