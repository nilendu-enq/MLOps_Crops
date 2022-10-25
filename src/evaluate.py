import pandas as pd
import pickle
import plac
import os

@plac.annotations(
    data_path =("Path to source data" , "option" , "i" , str),
    model_path=("Path to saved model" , "option" , "m" , str)
)


def main(data_path='../dataset/split' , model_path='models'):
    df_X_test=pd.read_csv(f'{data_path}/X_test.csv')
    df_y_test=pd.read_csv(f'{data_path}/y_test.csv')
    y_test = df_y_test['target'].squeeze(0)
    loaded_scaler = pickle.load(open(model_path+"/scaler.sav", 'rb'))
    X_test_scaled = loaded_scaler.transform(df_X_test)

    loaded_model = pickle.load(open(model_path+"/model.sav", 'rb'))
    result = loaded_model.score(X_test_scaled , y_test)

    print(result)
    pickle.dump(result, open(f'{model_path}/score.sav', 'wb'))
    print("\nModel evaluation sucessfull")

if __name__=='__main__':
    plac.call(main)