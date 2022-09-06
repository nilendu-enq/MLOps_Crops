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
import boto3

from sklearn.model_selection import train_test_split

@plac.annotations(
    data_path =("Path to source data" , "option" , "i" , str),
    out_path=("Path to save split data" , "option" , "o" , str)
)

def main(data_path='../dataset/Crop_recommendation.csv' , out_path='../dataset/split'):
    if not os.path.isdir(out_path):
        os.mkdir(out_path)
    
    df=pd.read_csv(data_path)

    c=df.label.astype('category')
    targets = dict(enumerate(c.cat.categories))
    y_cat_label = pd.Series(targets).to_frame()
    y_cat_label.to_csv(f'{out_path}/y_label.csv' , index=False)
    print('############')
    print(f'{out_path}/y_label.csv')
    print('############')
    df['target']=c.cat.codes
    y=df.target
    X=df[['N','P','K','temperature','humidity','ph','rainfall']]

    X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=1)

    X_train.to_csv(f'{out_path}/X_train.csv' , index=False)
    X_test.to_csv(f'{out_path}/X_test.csv' , index=False)
    y_train.to_csv(f'{out_path}/y_train.csv' , index=False)
    y_test.to_csv(f'{out_path}/y_test.csv' , index=False)

    ACCESS_KEY = 'AKIAWATRK4TZJTQ4BA2I'
    SECRET_KEY = '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'
    

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY , aws_secret_access_key=SECRET_KEY)
    s3.upload_file(f'{out_path}/y_label.csv' , 'enq-dataops-pipeline-artifacts', 'y_label.csv')
    print("Split data set finished sucessfully")

if __name__=='__main__':
    plac.call(main)
