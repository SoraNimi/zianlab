import math

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

lognormal_mean = 3
lognormal_std = 5
normal_std = np.sqrt(np.log10(1 + (lognormal_std/lognormal_mean)**2))
normal_mean = np.log10(lognormal_mean) - normal_std**2 / 2

print("normal_std", normal_std)
print("normal_mean", normal_mean)


hs = np.random.lognormal(normal_mean, normal_std, 300000)

print(hs.max())   # some finite number
print("hs.mean()", hs.mean())  # about 136519
print("hs.std()", hs.std())  # about 50405

plt.hist(hs, bins=200, color='steelblue', density=True)
plt.show()


