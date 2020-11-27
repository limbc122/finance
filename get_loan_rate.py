import datetime
import requests
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

today = datetime.date.today()

url = 'https://www.standardchartered.co.kr/np/kr/bs/et/selectLoanBaseRate/'
headers = {'Content-type':'application/json', 'Accept':'application/json'}
payload = {"serviceID":"HP_FP_PL_LoanBaseRate.selectLoanBaseRate",
        "task":"com.scfirstbank.web.fp.pl.task.HP_FP_PL_LoanBaseRateTask",
        "action":"selectLoanBaseRate",
        "BASE_DT":str(today)}
r = requests.post(url, headers=headers, json=payload)
data = r.json()
print(data['vector'][0])

# Make dataframe from json data

#       Call기준금리    금융채1년물     금융채3년물     금융채5년물
# Date

# ['CALL_BASE_INT', 'FNANCL_BOND_1_YR_EXPIRE', 'FNANCL_BOND_3_YR_EXPIRE', 'FNANCL_BOND_5_YR_EXPIRE']
df = json_normalize(data['vector'])
df.set_index("LOAN_BASE.BASE_DT", inplace=True)
df.sort_index(axis=0, ascending=True, inplace=True)
df.rename_axis("Date", inplace=True)
df.columns = [name[10:] for name in df.columns]

for column in df.columns:
	df[column] = pd.to_numeric(df[column])

print(df.head(5))
df = df.loc[df.index > '2018-01-01']
df['CALL_BASE_INT'].plot()
df['FNANCL_BOND_1_YR_EXPIRE'].plot()

fig, ax = plt.subplots(1, 1)
ax.xaxis.set_major_locator(ticker.MultipleLocator(30))

plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()