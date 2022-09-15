from boto3.session import Session
import boto3
import os

import plac


@plac.annotations(
    out_path=("Path to save split data" , "option" , "o" , str)
)

def main(out_path='dataset'):
    data_path='crop_input_data.csv'
    ACCESS_KEY = 'XXXXX'
    SECRET_KEY = 'XXXX'
    

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY , aws_secret_access_key=SECRET_KEY)
    s3.download_file('enq-dataops-pipeline-artifacts', f'{data_path}', f'{out_path}/Crop_recommendation.csv')

    print("Data fetch from S3 sucessfull")

if __name__=='__main__':
    main()
