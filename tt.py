import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
X = np.linspace(0, 10, 500)

std = 1
mean = 0
lognorm_distribution = scipy.stats.lognorm([std], loc=mean)
lognorm_distribution_pdf = lognorm_distribution.pdf(X)

fig, ax = plt.subplots(figsize=(8, 5))
plt.plot(X, lognorm_distribution_pdf, label="μ=0, σ=1")
ax.set_xticks(np.arange(min(X), max(X)))

# std = 0.5
# mean = 0
# lognorm_distribution = scipy.stats.lognorm([std], loc=mean)
# lognorm_distribution_pdf = lognorm_distribution.pdf(X)
# plt.plot(X, lognorm_distribution_pdf, label="μ=0, σ=0.5")
#
# std = 1.5
# mean = 1
# lognorm_distribution = scipy.stats.lognorm([std], loc=mean)
# lognorm_distribution_pdf = lognorm_distribution.pdf(X)
# plt.plot(X, lognorm_distribution_pdf, label="μ=1, σ=1.5")

plt.title("Lognormal Distribution")
plt.legend()
plt.show()

