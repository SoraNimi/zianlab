# -*- encoding=utf-8 -*-
import datetime
import re
import linecache
import numpy as np

import pandas as pd


def deal(listStr, i):
    # list转dataframe
    column = 'Voltage';
    df = pd.DataFrame(listStr, columns=[column])

    # 保存到本地excel
    IndexFile = 'offline-30mv-Layer2-Test6'+'.xlsx'
    df.to_excel(IndexFile, index=False)


if __name__ == '__main__':
    dataall = []
    for i in range(1, 201):
        indexFile = "dnn" + str(i) + ".mt0"
        s = linecache.getline(indexFile, 5)
        print(s)
        sub = re.sub(' +', ',', s)
        strAfter = sub
        data = strAfter.split(',')
        print(data)
        datalist = data[1:2]
        datalist = data[2:3]
        datalist = data[3:4]
        datalist = data[4:5]
        datalist = data[5:6]
        datalist = data[6:7]
        datalist = data[7:8]
        #datalist = data[1:513]

        datalist = data[513:514]
        datalist = data[514:515]
        datalist = data[515:516]
        datalist = data[516:517]
        datalist = data[517:518]
        datalist = data[518:519]
        datalist = data[519:520]


        datalist = data[1025:1026]
        datalist = data[1026:1027]
        datalist = data[1027:1028]
        datalist = data[1028:1029]
        datalist = data[1029:1030]
        datalist = data[1030:1031]
        datalist = data[1031:1032]




        #datalist = data[513:1025]
        #datalist = data[1025: 1537]
        print(datalist)
        dataall = dataall + datalist
    deal(dataall, i)
