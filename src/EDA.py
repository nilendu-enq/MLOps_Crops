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

    plt.figure(figsize=(12,5))
    plt.subplot(1, 2, 1)
    distplot_temperature = sns.distplot(df['temperature'],color="purple",bins=15,hist_kws={'alpha':0.2})
    save_charts(distplot_temperature,"distplot_temperature",charts_path)

    plt.subplot(1, 2, 2)
    distplot_ph= sns.distplot(df['ph'],color="green",bins=15,hist_kws={'alpha':0.2})
    save_charts(distplot_ph,"distplot_ph",charts_path)

    countplot=sns.countplot(y='label',data=df, palette="plasma_r")
    save_charts(countplot,"countplot",charts_path)

    pairplot=sns.pairplot(df, hue = 'label').savefig(f"{charts_path}/pairplot.png")
    
    jointplot_pottasium_Nitrogen=sns.jointplot(x="K",y="N",data=df[(df['N']>40)&(df['K']>40)],hue="label").savefig(f"{charts_path}/jointplot_pottasium_Nitrogen.png")

    jointplot_pottasium_humidity=sns.jointplot(x="K",y="humidity",data=df,hue='label',size=8,s=30,alpha=0.7).savefig(f"{charts_path}/jointplot_pottasium_humidity.png")

    boxplot_ph=sns.boxplot(y='label',x='ph',data=df)
    save_charts(boxplot_ph,"boxplot_ph",charts_path)

    boxplot_pottasium_rainfall=sns.boxplot(y='label',x='P',data=df[df['rainfall']>150])
    save_charts(boxplot_pottasium_rainfall,"boxplot_pottasium_rainfall",charts_path)

    lineplot_humidity_rainfall=sns.lineplot(data = df[(df['humidity']<65)], x = "K", y = "rainfall",hue="label")
    save_charts(lineplot_humidity_rainfall,"lineplot_humidity_rainfall",charts_path)

    X=df[['N','P','K','temperature','humidity','ph','rainfall']]
    heatmap_corelation=sns.heatmap(X.corr())
    save_charts(heatmap_corelation,"heatmap_corelation",charts_path)
    


    
    print("\nEDA data saved to charts folder")

if __name__=='__main__':
    plac.call(main)