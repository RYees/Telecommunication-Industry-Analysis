import pandas as pd
import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import seaborn as sns


def removing_missing_values(df):
    df = fd.drop(['IMSI', 'IMEI','TCP DL Retrans. Vol (Bytes)', 'TCP UL Retrans. Vol (Bytes)', 'HTTP DL (Bytes)', 'HTTP UL (Bytes)','Nb of sec with 125000B < Vol DL', 'Nb of sec with 1250B < Vol UL < 6250B', 'Nb of sec with 31250B < Vol DL < 125000B', 'Nb of sec with 37500B < Vol UL', 'Nb of sec with 6250B < Vol DL < 31250B', 'Nb of sec with 6250B < Vol UL < 37500B'], axis=1)
    df["Bearer Id"] = df["Bearer Id"].fillna(df["Bearer Id"].mode()[0])
    df["Start"] = df["Start"].fillna(method='ffill')
    df["Start ms"] = df["Start ms"].fillna(method='ffill')
    df["End"] = df["End"].fillna(method='ffill')
    df["End ms"] = df["End ms"].fillna(method='ffill')
    df["Dur. (ms)"] = df["Dur. (ms)"].fillna(method='ffill')
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
    # print(df)
    return df

    # sns.countplot(df["Last Location Name"])
    # plt.show()


if __name__ == "__main__":
    all_data = pd.read_excel("teleco_excel_file.xlsx")
    fd = pd.DataFrame(all_data)
    removing_missing_values(fd)


