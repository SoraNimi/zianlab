import math

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import datetime
import re
import linecache
import numpy as np
import pandas as pd

def deal(listStr):
    # list转dataframe
    column = 'RH';
    df = pd.DataFrame(listStr, columns=[column])

    # 保存到本地excel
    IndexFile = 'RH-LogNormalDirstribution-3' + '.xlsx'
    df.to_excel(IndexFile, index=False)


log10normal_mean = 2.66
log10normal_std = 0.366

lognormal_mean = 10 ** (log10normal_mean + log10normal_std**2 / 2)
lognormal_std = np.sqrt(10 ** (log10normal_std**2) - 1) * (10 ** (log10normal_mean + log10normal_std**2 / 2))

print(lognormal_mean)
print(lognormal_std)

normal_std = np.sqrt(np.log(1 + (lognormal_std/lognormal_mean)**2))
normal_mean = np.log(lognormal_mean) - normal_std**2 / 2

hs = np.random.lognormal(normal_mean, normal_std, 300000)

print("hs.max()", hs.max())  # some finite number
print("hs.mean()", hs.mean())  # about 136519
print("hs.std()", hs.std())  # about 50405

plt.hist(hs, bins=2000, color='steelblue', density=True)
plt.show()
deal(hs)

