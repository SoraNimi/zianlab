import math

import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import datetime
import re
import linecache
import numpy as np
import pandas as pd

hs = np.random.normal(1.2628, 0.8325, 33000)

print("hs.max()", hs.max())  # some finite number
print("hs.mean()", hs.mean())  # about 136519
print("hs.std()", hs.std())  # about 50405

plt.hist(hs, bins=200, color='steelblue', density=True)
plt.show()

