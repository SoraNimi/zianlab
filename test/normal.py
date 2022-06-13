import math

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import datetime
import re
import linecache
import numpy as np
import pandas as pd

lognormal_mean = 457
lognormal_std = 2.323


normal_std = np.sqrt(np.log(1 + (lognormal_std/lognormal_mean)**2))
normal_mean = np.log(lognormal_mean) - normal_std**2 / 2

hs = np.random.normal(2.6, 0.366, 300000)


print("hs.max()", hs.max())  # some finite number
print("hs.mean()", hs.mean())  # about 136519
print("hs.std()", hs.std())  # about 50405

plt.hist(hs, bins=200, color='steelblue', density=True)
plt.show()

