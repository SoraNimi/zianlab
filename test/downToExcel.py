# -*- encoding=utf-8 -*-
import re
import linecache
import numpy as np

import pandas as pd


def deal(listStr):
    # list转dataframe
    column = '200L0Voltage';
    df = pd.DataFrame(listStr, columns=[column])

    # 保存到本地excel
    IndexFile = 'offline-200L0Voltage' + '.xlsx'
    df.to_excel(IndexFile, index=False)


if __name__ == '__main__':
    mu, sigma = 400, 400  # mean and standard deviation
    numRH = 0
    normal_std = np.sqrt(np.log10(1 + (sigma / mu) ** 2))
    normal_mean = np.log10(mu) - normal_std ** 2 / 2
    hs = np.random.lognormal(normal_mean, normal_std, 5000)

    print(hs.max())  # some finite number
    print("mean", hs.mean())  # about 136519
    print("std", hs.std())  # about 50405
    dataall = []
    indexFile = "t1"
    data = hs
    print(data)
    deal(data)
