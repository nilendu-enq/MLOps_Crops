#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 23:39:09 2022

@author: 703296118NG
"""

import os
import numpy as np
import pandas as pd
import plac


from sklearn.model_selection import train_test_split

@plac.annotations(
    data_path =("Path to source data" , "option" , "i" , str),
    out_path=("Path to save split data" , "option" , "o" , str)
)

def main(data_path='../dataset/split' , out_path='../dataset/split'):
    df=pd.read_csv(data_path)
    train, test = train_test_split(df,random_state=1)

    if not os.path.isdir(out_path):
        os.mkdir(out_path)
    train.to_csv(f'{out_path}/train.csv' , index=False)
    test.to_csv(f'{out_path}/test.csv' , index=False)
    print("Split data set finished sucessfully")

if __name__=='__main__':
    plac.call(main)
