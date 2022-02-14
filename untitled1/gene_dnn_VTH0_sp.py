import numpy as np

#neuron = np.sign(np.load('layer0_neuron0.npy'))
#neuron = np.random.randint(2,size=1024)
weight = np.load('weight_offline.npy',allow_pickle=True,encoding="latin1")
#weight = np.load('weight_512.npy',allow_pickle=True,encoding="latin1")
neuron = []
for i in range(len(weight)):
    neuron.append(np.sign(weight[i]))
print (neuron)
#neuron = []
#for i in range(4):
#    neuron.append(-1*np.ones((2,2))

bld_len = 512
input_len = 784
## shape = (bl length, bl number)
#layer0_shape = (784,1024)
#layer0_shape = (784,2)
#layer1_shape = (2,2)
#layer2_shape = (2,2)
#layer3_shape = (2,10)
layer0_shape = neuron[0].shape
layer1_shape = neuron[2].shape
layer2_shape = neuron[4].shape
layer3_shape = neuron[6].shape
output_file = open("dnn_vth.sp","w")
#output_file = open("dnn_test.sp","w")
print(neuron[0].shape)
print(neuron[2].shape)
print(neuron[4].shape)
print(neuron[6].shape)
header_file = open("module_header.sp", "r")
line = header_file.readline()
while (not line==""):
    output_file.write(line)
    line = header_file.readline()




for i in range(1600):
    output_file.write(".subckt SAVM%d bl blb dl vdd\n" %(i+2))
    output_file.write("m1 dl net19 vdd vdd P L=180e-9 W=1e-6\n")
    output_file.write("m0 net19 net19 vdd vdd P L=180e-9 W=1e-6\n")
    output_file.write("m3 dl blb 0 0 N%d L=500e-9 W=3e-6\n" % (i + 1602))
    output_file.write("m2 net19 bl 0 0 N%d L=500e-9 W=3e-6\n" % (i + 2))
    output_file.write(".ends SAVM%d\n" %(i+2))
    output_file.write("\n")


#==================layer0===================
#layer0 bl cells ex:l0bl0
for j in range(0,layer0_shape[1]):
    for i in range(0,layer0_shape[0]):
        output_file.write("xl0b%dc%d l0bl%d vdd x%s x%sb CELLD r1=%se3 r0=%se3\n"
                          %(j,i,j,i,i,((10000) if neuron[0][i][j]==1 else (900)),((900) if neuron[0][i][j]==1 else (10000))))


output_file.write('\n')
for i in range(0,2):
    output_file.write("rl0bl%dr milkjelly 0 blinresistor\n" %(i))
    #output_file.write("xl0sa%d l0bl%d bldin l0sa%da vdd SAVM%d\n" %(i,i,i,i+2))
    output_file.write("xl0sa%d milkjelly bldin l0sa%da vdd SAVM%d\n" % (i, i, i + 2))
    output_file.write("xl0sa%dinva 0 l0sa%da l0sa%db vdd INV1\n" % (i, i, i))
    output_file.write("xl0sa%dinvb 0 l0sa%db l0dl%d vdd INV1\n" %(i,i,i))
    output_file.write("xl0dl%dinv 0 l0dl%d l0dl%db vdd INV1\n" %(i,i,i))

##==================dummy bl==============
#dummy bl cells 
output_file.write('\n')
#output_file.write('xbdc0 bld vdd vref vrefb CELLDREF\n')

for i in range(1,bld_len):
    output_file.write("xbdc%d bld vdd vref vrefb CELLD r1=%se3 r0=%se3\n" %(i,((10000) if i%2==0 else (900)),((900) if i%2==0 else (10000))))
output_file.write("rbldr bld 0 blresistor\n")

#for i in range(1,68):
 #   output_file.write("xbdc%d bld vdd vref vrefb CELLD r1=10e3 r0=1e3\n")
#for i in range(1,60):
  #  output_file.write("xbdc%d bld vdd vref vrefb CELLD r1=1e3 r0=10e3\n")
#output_file.write("rbldr bld 0 blresistor\n")

#output_file.write('xbdinc0 bldin vdd vref vrefb CELLDREF\n')
for i in range(1,input_len):
    output_file.write("xbdinc%d bldin vdd vref vrefb CELLD r1=%se3 r0=%se3\n" %(i,((10000) if i%2==0 else (900)),((900) if i%2==0 else (10000))))
output_file.write("rbldinr bldin 0 blinresistor\n")

output_file.write('\n')

#input invertor ex: x0inv
for i in range(layer0_shape[0]):
    output_file.write("x%dinv 0 x%d x%db vdd INV1\n" %(i,i,i))

#output_file.write("\n.include \"/home/user4/design/sim/XORNET4/hspiceD/schematic/netlist/stimuli/xnornet4.sp\"\n")
#output_file.write("\n.include \"img1.sp\"\n")
#output_file.write(".END\n")

output_file.close()
