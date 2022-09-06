import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
import pickle
import plac
import os

@plac.annotations(
    data_path =("Path to source data" , "option" , "i" , str),
    out_path=("Path to save split data" , "option" , "o" , str)
)


def main(data_path='../dataset/split' , out_path='models'):
    df_X_train=pd.read_csv(f'{data_path}/X_train.csv')
    df_y_train=pd.read_csv(f'{data_path}/y_train.csv')
    y_train = df_y_train['target'].squeeze(0)
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(df_X_train)

    if not os.path.isdir(out_path):
        os.mkdir(out_path)

    pickle.dump(scaler, open(f'{out_path}/scaler.sav', 'wb'))

    knn = KNeighborsClassifier()
    knn.fit(X_train_scaled, y_train)

    pickle.dump(knn, open(f'{out_path}/model.sav', 'wb'))

    print("Model KNN building finished sucessfully")

if __name__=='__main__':
    plac.call(main)