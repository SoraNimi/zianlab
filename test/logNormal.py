import math

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

mu, sigma = 400, 400  # mean and standard deviation

normal_std = np.sqrt(np.log(1 + (sigma / mu) ** 2))
normal_mean = np.log(mu) - normal_std ** 2 / 2
hs = np.random.lognormal(normal_mean, normal_std, 100000)

print(hs.max())  # some finite number
print(hs.mean())  # about 136519
print(hs.std())  # about 50405


print(hs)

