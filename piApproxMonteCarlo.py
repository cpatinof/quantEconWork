
## 2. pi approximation with MonteCarlo

import numpy as np

def approxPi(reps):
    U = [np.random.uniform(0,1,2) for item in range(reps)]
    D = [np.sqrt(((item[0]-0.5)**2)+((item[1]-0.5)**2)) for item in U]
    C = [item <= 0.5 for item in D]
    return (sum(C)/reps)/(1/4)

mcpi = [approxPi(1000) for item in range(10000)]

import matplotlib.pyplot as plt

plt.hist(mcpi, bins=50)
plt.show()