import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# neuron = np.sign(np.load('layer0_neuron0.npy'))
# neuron = np.random.randint(2,size=1024)

weight = np.load('weight_offline.npy', allow_pickle=True, encoding="latin1")
neuron = []
for i in range(len(weight)):
    neuron.append(np.sign(weight[i]))
# print (neuron)
# print(neuron[6][1])
# neuron = []
# for i in range(4):
#    neuron.append(-1*np.ones((2,2))

bld_len = 512
input_len = 784
## shape = (bl length, bl number)
# layer0_shape = (784,1024)
# layer0_shape = (784,2)
# layer1_shape = (2,2)
# layer2_shape = (2,2)
# layer3_shape = (2,10)
layer0_shape = neuron[0].shape
layer1_shape = neuron[2].shape
layer2_shape = neuron[4].shape
layer3_shape = neuron[6].shape
# output_file = open("dnn_mtj.sp","w")
# output_file = open("dnn_test.sp","w")
print("neuron[0].shape: ")
print(neuron[0].shape)
# 行数
print(neuron[0].shape[0])
# 列数
print(neuron[0].shape[1])
# print(neuron[0][4][0])


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

y_test_t017 = np.uint8([])
x_test_t017 = np.ones((1, 28, 28), dtype=np.uint8)

num = 0
for loop in range(2000):
    if y_test[loop] == 0:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break
num = 0
for loop in range(2000):
    if y_test[loop] == 1:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

num = 0
for loop in range(2000):
    if y_test[loop] == 2:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

num = 0
for loop in range(2000):
    if y_test[loop] == 3:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

num = 0
for loop in range(2000):
    if y_test[loop] == 4:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

num = 0
for loop in range(2000):
    if y_test[loop] == 5:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

num = 0
for loop in range(2000):
    if y_test[loop] == 6:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

num = 0
for loop in range(2000):
    if y_test[loop] == 7:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

num = 0
for loop in range(2000):
    if y_test[loop] == 8:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

num = 0
for loop in range(2000):
    if y_test[loop] == 9:
        print(loop)
        y_test_t017 = np.append(y_test_t017, y_test[loop].astype(np.uint8))
        x_test_t017 = np.append(x_test_t017, np.expand_dims(x_test[loop], 0), axis=0)
        num = num + 1
        if num == 5:
            break

x_test_t017 = np.delete(x_test_t017, 0, 0)

lm = []
ln = []
lo = []
lp = []
a = 2


for j in range(0, 512):
    nCol = 0
    m = 0
    n = 0
    o = 0
    p = 0
    for k in range(0, 28):
        for l in range(0, 28):
            if x_test_t017[a - 1][k][l] > 0:
                if neuron[0][nCol][j] == 1:
                    n = n + 1
                else:
                    m = m + 1
            else:
                if neuron[0][nCol][j] == 1:
                    o = o + 1
                else:
                    p = p + 1
            nCol = nCol + 1
    lm.append(m)
    ln.append(n)
    lo.append(o)
    lp.append(p)
# for i in range(0,layer0_shape[0]):
#     if neuron[0][i][0]==1:
#         for k in range(0, 28):
#             for l in range(0, 28):
#                 if x_test_t017[a -1][k][l] > 0:
#                     n=n+1
#                 else:
#                     m=m+1
# else:
#     for k in range(0, 28):
#         for l in range(0, 28):
#             if x_test_t017[a -1][k][l] > 0:
#                 o=o+1
#             else:
#                 p=p+1


print("---------------")
print("+1,+1num", ln[0])
print("+1,-1num", lm[0])
print("-1,+1num", lo[0])
print("-1,-1num", lp[0])

print("12121212"
      "")
print("+1,+1num", ln[1])
print("+1,-1num", lm[1])
print("-1,+1num", lo[1])
print("-1,-1num", lp[1])
# header_file = open("module_header_.sp", "r")
# output_file = open("tran.sp","w")
# output_file = open("imgall.sp","w")
# header_file = open("header_L0.sp", "r")
# line = header_file.readline()
# while (not line==""):
#     output_file.write(line)
#     line = header_file.readline()

## for all input set 1
# for i in range(0,layer0_shape[0]):
#     output_file.write("vx%d x%d 0 PWL\n+	0n		mvdd\n+	20n		mvdd\n+	25n	    mvdd\n+	200n    mvdd\n\n" % (i, i))


# # for first layer 512 output check
# for i in range(0,layer0_shape[1]):
#     output_file.write(".measure tran out20c%d AVG v(out20c%d) FROM = 199ns TO =200ns\n"
#                               %(i,i))
#     output_file.write(".measure tran bl%d AVG v(bl%d) FROM = 199ns TO =200ns\n"
#                               %(i,i))

# # for first layer 512 output check，without CMSA
# for i in range(0,layer0_shape[1]):
#     output_file.write(".measure tran bl%d AVG v(bl%d) FROM = 199ns TO =200ns\n"
#                               %(i,i))


# # for last layer 10 output check
# for i in range(0,layer3_shape[1]):
#     output_file.write(".measure tran out23c%d AVG v(out23c%d) FROM = 199ns TO =200ns\n"%(i,i))
#     output_file.write(".PROBE tran v(out23c%d)\n" % (i))


# #
# #
# # output_file.write('\n')
# #
# #input invertor ex: x0inv
# for i in range(layer0_shape[0]):
#     output_file.write("x%dinv 0 x%d x%db vdd INV1\n" %(i,i,i))
#
# output_file.write("\n.include \"img1.sp\"\n")
# output_file.write(".END\n")
#
# output_file.close()
