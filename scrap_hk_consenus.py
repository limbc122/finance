import datetime
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
import FinanceDataReader as fdr

today = datetime.date.today()
str_today = today.strftime("%Y-%m-%d")

def getPrevDate(date=today):
    prev_date = date - datetime.timedelta(days=1)
    if prev_date.weekday() > 4:
        return getPrevDate(prev_date)
    
    return prev_date


url = f'http://consensus.hankyung.com/apps.analysis/analysis.list?skinType=stock_good&pagenum=80&sdate={str_today}&edate={str_today}'
headers = {'Upgrade-Insecure-Requests': '1',
           'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
           'Accept-Encoding' : 'gzip, deflate',
           'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
r = requests.get(url, headers=headers)
r.encoding = None

soup = BeautifulSoup(r.text, 'html.parser')
trs = soup.select("tbody > tr")

# Date, Title, (Issue, ShortCode), Price, Position, Writer, Firm, CompanyInfo, Chart, Attachment
df = pd.DataFrame(columns=['Date', 'Title', 'Issue', 'ShortCode', 'Writer', 'Firm', 'Target Price', 'Prev Price'])
for tr in trs:
    row = []
    for i, td in enumerate(tr.select("td")):
        if i in (0, 2, 3, 4, 5):
            row.append(td.text.strip())
        elif i == 1:
            row.append(td.select_one("strong").text)
            row.append(re.sub(r'([^(]+)\([0-9]+\).*', r'\1', row[1])) # Issue Name
            row.append(re.sub(r'[^(]+\(([0-9]+)\).*', r'\1', row[1])) # Short Code
        else:
            row.append("")

    df = df.append(pd.Series(row, index=df.columns), ignore_index=True)
    price = fdr.DataReader(row[3], getPrevDate(datetime.datetime.strptime(row[0],"%Y-%m-%d")))
    print(price)


print(df)