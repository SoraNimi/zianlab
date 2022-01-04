import numpy as np
    output_file = open("bu40n3.mdl","w")
#output_file = open("dnn_test.sp","w")

    header_file = open("bu40n2.mdl","r")
    line = header_file.readline()
    for line in  header_file.readlines()[0:53]:
            output_file.write(line)



    output_file.write(".MODEL N%d NMOS\n" %(i+1))
