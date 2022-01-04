from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

import numpy as np

fl1=np.zeros(shape=(512))
fl2=np.zeros(shape=(512))
diff1 = np.zeros(shape=(512))
bias1 = np.zeros(shape=(512))
array=np.load('fluctuation30_1mV.npy',allow_pickle=True,encoding="latin1")

for i in range(512):

    diff1[i]=array[i]-array[i+1600]
    fl1[i]=array[i]
    fl2[i]=array[i+1600]
np.save('fluctuationbl1',fl1)
np.save('fluctuationdbl1',fl2)

diff2 = np.zeros(shape=(512))
bias2 = np.zeros(shape=(512))
fl3=np.zeros(shape=(512))
fl4=np.zeros(shape=(512))
for i in range(512):
    diff2[i]=array[i+512]-array[i+1600+512]
    fl3[i] = array[i+512]
    fl4[i] = array[i + 1600+512]
print (diff2[0])
np.save('fluctuationbl2',fl3)
np.save('fluctuationdbl2',fl4)
#print(bias2)

fl5=np.zeros(shape=(512))
fl6=np.zeros(shape=(512))
diff3 = np.zeros(shape=(512))
bias3 = np.zeros(shape=(512))
for i in range(512):
    diff3[i]=array[i+512+512]-array[i+1600+512+512]
    fl5[i] = array[i + 512+512]
    fl6[i] = array[i + 1600 + 512+512]
np.save('fluctuationbl3',fl5)
np.save('fluctuationdbl3',fl6)
