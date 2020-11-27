import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import statsmodels
from statsmodels.tsa.stattools import coint
from datetime import datetime
import FinanceDataReader as fdr

start = datetime(2013,1,1)
end = datetime(2018,1,1)

df_issue = fdr.DataReader('035420', '2018')
df_kospi = fdr.DataReader('035720', '2018')

data = pd.DataFrame([df_issue.Close, df_kospi.Close]).T
data.columns = ['ISSUE', 'KOSPI']
# print(data.head())

S1 = data['ISSUE']
S2 = data['KOSPI']

ratio = S1/S2
# ratio.plot(figsize=(15,7))
# plt.axhline(ratio.mean(), color='r', linestyle='--')
# plt.show()

def zscore(series):
    return (series-series.mean())/np.std(series)

# zscore(ratio).plot(figsize=(15,7))
# plt.axhline(zscore(ratio).mean(), color='black')
# plt.axhline(1.0, color='r', linestyle='--')
# plt.axhline(-1.0, color='green', linestyle='--')
# plt.legend(['Z-score', 'Mean', '+1', '-1'])
# plt.show()
train = ratio
# train = ratio[:800]
# test = ratio[800:]

ratio_ma5 = train.rolling(window=5).mean()
ratio_ma60 = train.rolling(window=60).mean()
std_60 = train.rolling(window=60).std()
zscore = (ratio_ma5 - ratio_ma60) / std_60

zscore.plot(figsize=(15,7))
plt.autoscale(enable=True, axis='both', tight=True)
plt.axhline(0, color='black')
plt.axhline(1.0, color='r', linestyle='--')
plt.axhline(-1.0, color='green', linestyle='--')
plt.legend(['Z-score', 'Mean', '+1', '-1'])
# plt.imshow(zscore, aspect='auto')
# ax = plt.gca() # gets the active axis
# ax.set_aspect(10)
plt.show()