from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility
import h5py
import datetime
import numpy as np
import keras.backend as K
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Layer, Activation, BatchNormalization
from tensorflow.keras.optimizers import SGD, Adam, RMSprop
from keras.callbacks import LearningRateScheduler
from keras.utils import np_utils
import keras
import tensorflow as tf
import time

from b import binary_tanh as binary_tanh_op
from b import binary_tanh1
from c import BinaryDense, BinaryDense1, BinaryDense2, BinaryDense3, Clip, BinaryConv2D
#############################################################################################
from keras.models import load_model










class DropoutNoScale(Dropout):
    '''Keras Dropout does scale the input in training phase, which is undesirable here.
    '''
    def call(self, inputs, training=None):
        if 0. < self.rate < 1.:
            noise_shape = self._get_noise_shape(inputs)

            def dropped_inputs():
                return K.dropout(inputs, self.rate, noise_shape,
                                 seed=self.seed) * (1 - self.rate)
            return K.in_train_phase(dropped_inputs, inputs,
                                    training=training)
        return inputs





def binary_tanh(x):
    return binary_tanh_op(x)




batch_size = 128
#batch_size = 12
epochs = 200
#epochs = 1
#epochs = 1
nb_classes = 10

#H = 'Glorot'
#kernel_lr_multiplier = 'Glorot'
#H = 0.5
#kernel_lr_multiplier = 5
H = 0.25

kernel_lr_multiplier = 2.5

# network
num_unit = 512
#num_hidden = 200
use_bias = True
stddev = 8000
bias_initializer = 'zeros'
#bias_initializer =keras.initializers.TruncatedNormal(mean=100, stddev=100, seed=None)
#bias_initializer = keras.initializers.random_normal(mean=0,stddev=stddev,seed=None)

#bias=keras.initializers.RandomNormal
#print(bias_initializer)
#bias_initializer=
# learning rate schedule 4 5   5 6
lr_start = 1e-3
lr_end = 2.5e-4
lr_decay = (lr_end / lr_start)**(1. / epochs)

# BN 6 9
epsilon = 1e-7
momentum = 0.9

# dropout
drop_in = 0.15
drop_hidden = 0.25


start_time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S");

# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
X_train[X_train>0]=1
X_train[X_train==0]=-1
X_test[X_test>0]=1
X_test[X_test==0]=-1
#print(X_train[0])
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes) * 2 - 1 # -1 or 1 for hinge loss
Y_test = np_utils.to_categorical(y_test, nb_classes) * 2 - 1

model = Sequential()
model.add(DropoutNoScale(drop_in, input_shape=(784,), name='drop0'))
model.add(BinaryDense1(num_unit, H=H, kernel_lr_multiplier=kernel_lr_multiplier, use_bias=True,
        name='dense{}'.format(1),bias_initializer=bias_initializer))
#model.add(BatchNormalization(epsilon=epsilon, momentum=momentum, name='bn{}'.format(1)))
model.add(Activation(binary_tanh1, name='act{}'.format(1)))
model.add(DropoutNoScale(drop_hidden, name='drop{}'.format(1)))


model.add(BinaryDense2(num_unit, H=H, kernel_lr_multiplier=kernel_lr_multiplier, use_bias=True,
        name='dense{}'.format(2),bias_initializer=bias_initializer))
#model.add(BatchNormalization(epsilon=epsilon, momentum=momentum, name='bn{}'.format(2)))
model.add(Activation(binary_tanh1, name='act{}'.format(2)))
model.add(DropoutNoScale(drop_hidden, name='drop{}'.format(2)))

model.add(BinaryDense3(num_unit, H=H, kernel_lr_multiplier=kernel_lr_multiplier, use_bias=True,
        name='dense{}'.format(3),bias_initializer=bias_initializer))
#model.add(BatchNormalization(epsilon=epsilon, momentum=momentum, name='bn{}'.format(3)))
model.add(Activation(binary_tanh1, name='act{}'.format(3)))
model.add(DropoutNoScale(drop_hidden, name='drop{}'.format(3)))

model.add(BinaryDense(10, H=H, kernel_lr_multiplier=kernel_lr_multiplier, use_bias=True,
          name='dense',bias_initializer=bias_initializer))
#model.add(BatchNormalization(epsilon=epsilon, momentum=momentum, name='bn'))

model.summary()
#model.load_weights('m512retrain30mv.h5')
#model.load_weights('m512bias0nol.h5')
#model.load_weights('m512retrain30mv.h5')
model.load_weights('m512xinco-5mv.h5')

weights_list = model.get_weights()
result6= np.random.normal(0, 0, 512)

result1= np.random.normal(0, 0, 512)

result2= np.random.normal(0, 0, 512)
result8= np.random.normal(0, 0, 512)
result0= np.random.normal(0, 0, 512)
result3= np.random.normal(0, 0, 512)
result4= np.random.normal(0, 0, 10)

neuron1 = []
for i in range(len(weights_list)):
    neuron1.append(np.sign(weights_list[i]))
#print(weights_list[0])

#for i in range(784):
#    for j in range (512):
#        r=i*j
#        neuron1[0][i][j]=neuron1[0][i][j]+result1[r]
#for i in range(512):
#    for j in range (512):
#        a=i*j
#        neuron1[2][i][j]=neuron1[2][i][j]+result1[a]
#for i in range(512):
#    for j in range (512):
#        r=i*j
#        neuron1[4][i][j]=neuron1[4][i][j]+result1[r]
#for i in range(512):
#    for j in range (10):
#        r=i*j
#        neuron1[6][i][j]=neuron1[6][i][j]+result1[r]
#array1=np.vstack((weights_list[0],result1))
#array2=np.vstack((weights_list[2],result2))
#array3=np.vstack((weights_list[4],result3))
#array4=np.vstack((weights_list[6],result4))
a1=[0,0]
a2=[0,0]
a3=[0,0]
a4=[0,0]





a1[0]=neuron1[0]
a1[1]=result2
a2[0]=neuron1[2]
a2[1]=result2
a3[0]=neuron1[4]
a3[1]=result2
a4[0]=neuron1[6]
a4[1]=result4







#for i, weights in enumerate(weights_list[0:9]):
model.layers[1].set_weights(a1)
model.layers[4].set_weights(a2)
model.layers[7].set_weights(a3)

model.layers[10].set_weights(a4)


opt = Adam(lr=lr_start, epsilon = 1e-6)
model.compile(loss='squared_hinge',optimizer= opt,  metrics=['acc'])
lr_scheduler = LearningRateScheduler(lambda e: lr_start * lr_decay ** e)
history = model.fit(X_train, Y_train,
                    batch_size=batch_size, epochs=epochs,
                    verbose=1, validation_data=(X_test, Y_test),
                    callbacks=[lr_scheduler])
score = model.evaluate(X_test, Y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])

#score = model.evaluate(X_test, Y_test, verbose=1)
#print('Test score:', score[0])
#print('Test accuracy:', score[1])
#(a1[0])
################save weight########################################################
model.save_weights('weight_insitu-5mv.h5')
#model.save_weights('m512retrain15nol.h5')
#model.save('m512xinco-5mv.h5')
#weights_list = model.get_weights()
#weight1=model.get_weights()[0]
#weight2=model.get_weights()[6]
#weight3=model.get_weights()[12]
#weight4=model.get_weights()[18]
#np.save('shiyanling10500.npy',(weight1,weight2,weight3,weight4))
weight=model.get_weights()
np.save('weight_insitu-5mv.npy',weight)
##########################################
o0=[3
,10
,13
,25
,28
,55
,69
,71
,101
,126
,136
,148
,157
,183
,188
,192
,194
,215
,246
,269]
o1=[1004
,1008
,1011
,1019
,1025
,1027
,1030
,1037
,1038
,1040
,1054
,1075
,1083
,1097
,1129
,1136
,1137
,1139
,1179
,1180
]
o2=[2044
,2055
,2058
,2082
,2085
,2092
,2098
,2101
,2108
,2110
,2112
,2122
,2126
,2133
,2138
,2157
,2158
,2176
,2184
,2186]
o3=[3010
,3015
,3045
,3049
,3074
,3078
,3080
,3082
,3083
,3085
,3094
,3104
,3108
,3110
,3120
,3129
,3131
,3138
,3146
,3150]
o4=[4001
,4012
,4017
,4024
,4029
,4042
,4046
,4060
,4071
,4172
,4192
,4194
,4197
,4217
,4221
,4223
,4229
,4258
,4265
,4266]
o5=[5020
,5021
,5056
,5083
,5098
,5102
,5111
,5134
,5152
,5160
,5170
,5174
,5187
,5194
,5196
,5197
,5206
,5207
,5222
,5223
]
o6=[6002
,6020
,6029
,6031
,6033
,6038
,6068
,6078
,6088
,6094
,6104
,6113
,6122
,6128
,6130
,6134
,6167
,6179
,6187
,6197
]
o7=[7021
,7028
,7030
,7032
,7041
,7059
,7069
,7079
,7082
,7088
,7098
,7111
,7124
,7141
,7144
,7145
,7149
,7180
,7189
,7197
]
o8=[8009
,8012
,8015
,8027
,8037
,8046
,8065
,8075
,8097
,8105
,8125
,8135
,8145
,8147
,8157
,8183
,8209
,8216
,8217
,8223]
o9=[9023
,9026
,9028
,9054
,9057
,9069
,9079
,9089
,9093
,9094
,9142
,9144
,9153
,9165
,9170
,9188
,9198
,9206
,9214
,9216]













############middle layer output#################
inp = model.input                                           # input placeholder
outputs = [layer.output for layer in model.layers]          # all layer outputs
#functor = K.function([inp]+ [K.learning_phase()], outputs ) # evaluation function
functor1 = K.function([inp], outputs )



## Testing 1

#for i in range(10):
#    test = np.random.random(X_test[1].shape)[np.newaxis,...]
#layer_outs = functor([X_test[0], 1.]) #with dropout
#    layer_outs = functor([X_test[1][np.newaxis,...], 0.]) #without dropout
#    print("###################")
#print
 #   h=layer_outs[o1[i]][0][0]
 #   for j in range(10):
  #      diff=h-layer_outs[1][0][j]
  #      print(h)

#########################################################################33
#import matplotlib.pyplot as plt
#plt.plot()
#plt.plot(history.history['val_acc'])
#plt.title('model accuracy')
#plt.ylabel('accuracy')
#plt.xlabel('epoch')
#plt.legend(['test'], loc='upper left')
#plt.show()

#plt.plot(history.history['val_loss'])
#plt.title('model loss')
#plt.xlabel('epoch')
#plt.legend(['test'], loc='upper left')
#plt.show()

#####################################################################################
import pickle

#with open ('ret_25mv.txt','wb') as file_pi:
 #   pickle.dump(history.history,file_pi)

#####################################################################################
#print(layer_outs)
for i in range (20):
## Testing 1
    test = np.random.random(X_test[o0[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs1 = functor1([X_test[o0[i]][np.newaxis,...], 0.]) #without dropout
    print(0)
    print(layer_outs1[10])

for i in range (20):
## Testing 1
    test = np.random.random(X_test[o1[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs1 = functor1([X_test[o1[i]][np.newaxis,...], 0.]) #without dropout
    print(1)

    print(layer_outs1[10])

for i in range (20):
    test2 = np.random.random(X_test[o2[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs2 = functor1([X_test[o2[i]][np.newaxis,...], 0.]) #without dropout
    print(2)
    print(layer_outs2[10])

for i in range (20):
    test3 = np.random.random(X_test[o3[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs3 = functor1([X_test[o3[i]][np.newaxis,...], 0.]) #without dropout
    print(3)
    print(layer_outs3[10])

for i in range(20):
    test4 = np.random.random(X_test[o4[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs4 = functor1([X_test[o4[i]][np.newaxis,...], 0.]) #without dropout
    print(4)
    print(layer_outs4[10])

for i in range(20):
    test5 = np.random.random(X_test[o5[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs5 = functor1([X_test[o5[i]][np.newaxis,...], 0.]) #without dropout
    print(5)
    print(layer_outs5[10])

for i in range(20):
    test6 = np.random.random(X_test[o6[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs6 = functor1([X_test[o6[i]][np.newaxis,...], 0.]) #without dropout
    print(6)
    print(layer_outs6[10])

for i in range(20):
    test7 = np.random.random(X_test[o7[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs7 = functor1([X_test[o7[i]][np.newaxis,...], 0.]) #without dropout
    print(7)
    print(layer_outs7[10])

for i in range(20):
    test8 = np.random.random(X_test[o8[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs8 = functor1([X_test[o8[i]][np.newaxis,...], 0.]) #without dropout
    print(8)
    print(layer_outs8[10])

for i in range(20):
    test9 = np.random.random(X_test[o9[i]].shape)
##layer_outs = functor([X_test[0], 1.]) #with dropout
    layer_outs9 = functor1([X_test[o9[i]][np.newaxis,...], 0.]) #without dropout
    print(9)
    print(layer_outs9[10])



#print(layer_outs2)
#print(layer_outs[10][0][1])
#print(layer_outs[3][0])
#print(layer_outs[4][0])