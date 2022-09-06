from boto3.session import Session
import boto3
import os

import plac


def main(data_path='crop_input_data.csv' , out_path='dataset/Crop_recommendation.csv'):
    ACCESS_KEY = 'AKIAWATRK4TZJTQ4BA2I'
    SECRET_KEY = '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'
    

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY , aws_secret_access_key=SECRET_KEY)
    s3.download_file('enq-dataops-pipeline-artifacts', 'Crop_input_data2.csv', 'dataset/Crop_recommendation.csv')

    print("Data fetch from S3 sucessfull")

if __name__=='__main__':
    main()
