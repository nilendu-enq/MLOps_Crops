import pandas as pd
import pickle
import plac
import os

@plac.annotations(
    data_path =("Path to source data" , "option" , "i" , str),
    model_path=("Path to save split data" , "option" , "i" , str)
)


def main(data_path='../dataset/split' , model_path='models'):
    df_X_test=pd.read_csv(f'{data_path}/X_test.csv')
    df_y_test=pd.read_csv(f'{data_path}/y_test.csv')
    y_test = df_y_test['target'].squeeze(0)
    
    loaded_scaler = pickle.load(open("f{model_path}/scaler.sav", 'rb'))
    X_test_scaled = loaded_scaler.transform(X_test)

    loaded_model = pickle.load(open("f{model_path}/knn.sav", 'rb'))
    result = loaded_model.score(X_test_scaled , y_test)

    print("Model evaluation sucessfull")

if __name__=='__main__':
    plac.call(main)