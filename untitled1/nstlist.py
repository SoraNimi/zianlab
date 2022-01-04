
for j in range(1):
    output_file = open(("dnn%s.sp")%(j+1),"w")
#output_file = open("dnn_test.sp","w")

    header_file = open("dnn0.sp","r")
    line = header_file.readline()
    while (not line==""):
        output_file.write(line)
        line = header_file.readline()

    output_file.write(".include img%s.sp\n"%(j+1))
    output_file.write(".END")