import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import seaborn as sns

all_data = pd.read_excel("teleco_excel_file.xlsx")
all_data.head()
# pd.set_option('display.max_columns', 50)

# fd = pd.DataFrame(all_data)
# fd.head()

# df = fd.drop(['IMSI', 'IMEI','TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)', 'HTTP DL (Bytes)', 'HTTP UL (Bytes)','Nb of sec with 125000B < Vol DL', 'Nb of sec with 1250B < Vol UL < 6250B', 'Nb of sec with 31250B < Vol DL < 125000B', 'Nb of sec with 37500B < Vol UL', 'Nb of sec with 6250B < Vol DL < 31250B', 'Nb of sec with 6250B < Vol UL < 37500B'], axis=1)
# df.iloc[:5 , 0:10]
# df = df.fillna(method='ffill')


# def plot_hist(df:pd.DataFrame, column:str, color:str)->None:
#     # plt.figure(figsize=(15, 10))
#     # fig, ax = plt.subplots(1, figsize=(12, 7))
#     sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
#     plt.title(f'Distribution of {column}', size=20, fontweight='bold')
#     plt.show()
    
# def plot_count(df:pd.DataFrame, column:str) -> None:
#     plt.figure(figsize=(12, 7))
#     sns.countplot(data=df, x=column)
#     plt.title(f'Distribution of {column}', size=20, fontweight='bold')
#     plt.show()
    
# def plot_bar(df:pd.DataFrame, x_col:str, y_col:str, title:str, xlabel:str, ylabel:str)->None:
#     plt.figure(figsize=(12, 7))
#     sns.barplot(data = df, x=x_col, y=y_col)
#     plt.title(title, size=20)
#     plt.xticks(rotation=75, fontsize=14)
#     plt.yticks( fontsize=14)
#     plt.xlabel(xlabel, fontsize=16)
#     plt.ylabel(ylabel, fontsize=16)
#     plt.show()

# def plot_heatmap(df:pd.DataFrame, title:str, cbar=False)->None:
#     plt.figure(figsize=(12, 7))
#     sns.heatmap(df, annot=True, cmap='viridis', vmin=0, vmax=1, fmt='.2f', linewidths=.7, cbar=cbar )
#     plt.title(title, size=18, fontweight='bold')
#     plt.show()

# def plot_box(df:pd.DataFrame, x_col:str, title:str) -> None:
#     plt.figure(figsize=(12, 7))
#     sns.boxplot(data = df, x=x_col)
#     plt.title(title, size=20)
#     plt.xticks(rotation=75, fontsize=14)
#     plt.show()

# def plot_box_multi(df:pd.DataFrame, x_col:str, y_col:str, title:str) -> None:
#     plt.figure(figsize=(12, 7))
#     sns.boxplot(data = df, x=x_col, y=y_col)
#     plt.title(title, size=20)
#     plt.xticks(rotation=75, fontsize=14)
#     plt.yticks( fontsize=14)
#     plt.show()

# def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
#     plt.figure(figsize=(12, 7))
#     sns.scatterplot(data = df, x=x_col, y=y_col, hue=hue, style=style)
#     plt.title(title, size=20)
#     plt.xticks(fontsize=14)
#     plt.yticks( fontsize=14)
#     plt.show()


# #plot_hist(df, "Social Media DL (Bytes)", "blue")

# plot_box(df, "Social Media DL (Bytes)", "Social Media DL (Bytes) Outliers")
