
from curses import keyname
import os
import pandas as pd
import boto3

import plac


@plac.annotations(
    out_path=("Path to save cleaned s3 data" , "option" , "o" , str)
)

def main(out_path='dataset/Crop_recommendation.csv'):
    boto_session = boto3.Session(profile_name="enq_ci_gitops")
    s3_client = boto_session.client(service_name="s3")

    bucket_name="enq-dataops-pipeline-artifacts"
    key="crop_input_data.csv"
    s3_client.download_file(bucket_name,key,out_path)

if __name__=='__main__':
    plac.call(main)