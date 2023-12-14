import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as plts
import seaborn as sns


def fix_outlier(df, column):
    df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])    
    return df[column]

################ Plot Functions ########################
def plot_hist(df:pd.DataFrame, column:str, color:str)->None:
    # plt.figure(figsize=(15, 10))
    # fig, ax = plt.subplots(1, figsize=(12, 7))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()
    
def plot_count(df:pd.DataFrame, column:str) -> None:
    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, x=column)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()
    
def plot_bar(df:pd.DataFrame, x_col:str, y_col:str, title:str, xlabel:str, ylabel:str)->None:
    plt.figure(figsize=(12, 7))
    sns.barplot(data = df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks( fontsize=14)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.show()

def plot_heatmap(df:pd.DataFrame, title:str, cbar=False)->None:
    plt.figure(figsize=(12, 7))
    sns.heatmap(df, annot=True, cmap='viridis', vmin=0, vmax=1, fmt='.2f', linewidths=.7, cbar=cbar )
    plt.title(title, size=18, fontweight='bold')
    plt.show()

def plot_box(df:pd.DataFrame, x_col:str, title:str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data = df, x=x_col,showfliers = False)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.show()

def plot_box_multi(df:pd.DataFrame, x_col:str, y_col:str, title:str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data = df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks( fontsize=14)
    plt.show()

def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data = df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(fontsize=14)
    plt.yticks( fontsize=14)
    plt.show()

def plot_scat(df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data = df, x=x_col, y=y_col, hue=hue, style=style)
    plt.title(title, size=20)
    plt.xticks(fontsize=14)
    plt.yticks( fontsize=14)
    plt.show()

def kmeans_plot(df: pd.DataFrame) -> None:
    # Plot the k-means clusters
    plt.scatter(df['Normalized Session Duration'], df['Normalized Sessions Total Traffic'], c=df['Engagement Group'])
    plt.xlabel('Normalized Session Duration')
    plt.ylabel('Normalized Sessions Total Traffic')
    plt.title('K-means Clustering of Customer Engagement')

    # Add color legend
    # legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Group 0'),
    #                 plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Group 1'),
    #                 plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Group 2')]
    # plt.legend()

    plt.show()

def kmeans_minmaxavgclustering(df: pd.DataFrame, cluster_metrics) -> None:
    # Plot the clusters
    plt.scatter(df['Session Duration'], df['Sessions Total Traffic'], c=df['Engagement Group'])
    plt.xlabel('Session Duration')
    plt.ylabel('Sessions Total Traffic')
    plt.title('Clustering of Customer Engagement')

    # Display the cluster metrics
    for i, row in cluster_metrics.iterrows():
        plt.text(row[('Session Duration', 'mean')],
                row[('Sessions Total Traffic', 'mean')],
                f'Cluster {i}\nMin: {row[("Session Duration", "min")]:.2f}\nMax: {row[("Session Duration", "max")]:.2f}\n'
                f'Avg: {row[("Session Duration", "mean")]:.2f}\nSum: {row[("Session Duration", "sum")]:.2f}',
                ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black'))

    plt.show()