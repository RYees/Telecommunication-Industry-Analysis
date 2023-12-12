import os
import sys
import re
import glob
import json
import datetime
from collections import Counter
from collections import Counter

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from wordcloud import WordCloud
import numpy as np

def load_json_data(path):
    """load tele data"""
    combined = []

    for json_file in glob.glob(f"{path}*.json"):
        with open(json_file, 'r') as slack_data:
            combined.append(json.load(slack_data))
    return combined

def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    return "The telco dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values."

def repalce_missing_values(df):
  df["Bearer Id"] = df["Bearer Id"].fillna(df["Bearer Id"].mode()[0])
  df["Start"] = df["Start"].fillna(method='ffill')
  df["Start ms"] = df["Start ms"].fillna(method='ffill')
  df["End"] = df["End"].fillna(method='ffill')
  df["End ms"] = df["End ms"].fillna(method='ffill')
  df["Dur. (ms)"] = df["Dur. (ms)"].fillna(method='ffill')
  df["TCP DL Retrans. Vol (Bytes)"] = df["TCP DL Retrans. Vol (Bytes)"].fillna(df["TCP DL Retrans. Vol (Bytes)"].mean())
  df["TCP UL Retrans. Vol (Bytes)"] = df["TCP UL Retrans. Vol (Bytes)"].fillna(df["TCP UL Retrans. Vol (Bytes)"].mean())
  df["Total UL (Bytes)"] = df["Total UL (Bytes)"].fillna(df["Total UL (Bytes)"].mode()[0])
  df["Total DL (Bytes)"] = df["Total UL (Bytes)"].fillna(df["Total DL (Bytes)"].mode()[0])
  df["Nb of sec with Vol DL < 6250B"] = df["Nb of sec with Vol DL < 6250B"].fillna(df["Nb of sec with Vol DL < 6250B"].mode()[0]) 
  df["Nb of sec with Vol UL < 1250B"] = df["Nb of sec with Vol UL < 1250B"].fillna(df["Nb of sec with Vol UL < 1250B"].mode()[0])
  df["MSISDN/Number"] = df["MSISDN/Number"].fillna(df["MSISDN/Number"].mode()[0])
  df["Avg RTT DL (ms)"] = df["Avg RTT DL (ms)"].fillna(df["Avg RTT DL (ms)"].mode()[0])
  df["Avg RTT UL (ms)"] = df["Avg RTT UL (ms)"].fillna(df["Avg RTT UL (ms)"].mode()[0])
  df["Avg Bearer TP DL (kbps)"] = df["Avg Bearer TP DL (kbps)"].fillna(df["Avg Bearer TP DL (kbps)"].mode()[0])
  df["Avg Bearer TP UL (kbps)"] = df["Avg Bearer TP UL (kbps)"].fillna(df["Avg Bearer TP UL (kbps)"].mode()[0])
  df["Activity Duration DL (ms)"] = df["Activity Duration DL (ms)"].fillna(df["Activity Duration DL (ms)"].mode()[0])
  df["Activity Duration UL (ms)"] = df["Activity Duration UL (ms)"].fillna(df["Activity Duration UL (ms)"].mode()[0])
  df["Dur. (ms).1"] = df["Dur. (ms).1"].fillna(df["Dur. (ms).1"].mode()[0])
  df["Handset Manufacturer"] = df["Handset Manufacturer"].fillna(value='undefined')
  df["Handset Type"] = df["Handset Type"].fillna(value='undefined')
  df["Last Location Name"] = df["Last Location Name"].fillna(value='undefined')
  
  df = df.fillna(value=0)
  return df

