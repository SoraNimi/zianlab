import numpy as np
diff1=[]
diff2=[]
diff3=[]
bias1=[]
bias2=[]
bias3=[]
diff1 = np.zeros(shape=(512))
bias1 = np.zeros(shape=(512))
array=np.random.lognormal(0, 0.025, 3300)
print(array)
import matplotlib.pyplot as plt
np.save('fluctuation30_1mV.npy',array)
