import math

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 136519, 50405  # mean and standard deviation

normal_std = np.sqrt(np.log(1 + (sigma / mu) ** 2))
normal_mean = np.log(mu) - normal_std ** 2 / 2
hs = np.random.lognormal(normal_mean, normal_std, 1000)
print(hs.max())  # some finite number
print(hs.mean())  # about 136519
print(hs.std())  # about 50405

#    hs = np.random.lognormal(mu, sigma, 1000) #mean, s dev , Size
#
count, bins, ignored = plt.hist(hs, 100, normed=True)

x = np.linspace(min(bins), max(bins), 10000)
pdfT = [];
for el in range(len(x)):
    pdfTmp = (math.exp(-(np.log(x[el]) - mu) ** 2 / (2 * sigma ** 2)))
    pdfT += [pdfTmp]

# plt.axis('tight')
pdf = np.asarray(pdfT)
plt.plot(x, pdf, linewidth=2, color='r')
