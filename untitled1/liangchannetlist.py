for j in range(100):
    output_file = open(("dnn%d.sp")%(j+1),"w")
#output_file = open("dnn_test.sp","w")
    header_file = open("dnn512retrain30.sp","r")
    line = header_file.readline()
    while (not line==""):
        output_file.write(line)
        line = header_file.readline()
    output_file.write(("\n.include \"img%d.sp\"\n")%(j+1))
    output_file.write(".END\n")

    output_file.close()

