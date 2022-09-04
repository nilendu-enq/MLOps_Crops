import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plac
import os

def save_charts(chart, chart_name ,path):
    fig = chart.get_figure()   
    fig.savefig(f"{path}/{chart_name}.png")
   
@plac.annotations(
    data_path =("Path to source data" , "option" , "i" , str),
    charts_path=("Path to save split data" , "option" , "o" , str)
)

def main(data_path='../dataset/Crop_recommendation.csv' , charts_path='charts'):
    if not os.path.isdir(charts_path):
        os.mkdir(charts_path)
    
    df=pd.read_csv(data_path)
    heatmap = sns.heatmap(df.isnull(),cmap="coolwarm")
    save_charts(heatmap,"heatmap",charts_path)


    
    print("\nEDA DATA SAVED")

if __name__=='__main__':
    plac.call(main)