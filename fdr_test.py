# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import matplotlib.ticker as ticker
# import mplfinance as mpf
# from mplfinance.original_flavor import candlestick2_ohlc as candlestick

import mplfinance as mpf
import FinanceDataReader as fdr

# df = fdr.DataReader('KS11', '2020')

# mpf.plot(df, type='candle', style='charles', mav=(3,7,21), volume=True,
#          title='KOSPI200',
#          ylabel='Price',
#          show_nontrading=False)

# plt.rcParams["font.family"] = 'nanummyeongjo'
# plt.rcParams["figure.figsize"] = (14,4)
# plt.rcParams['lines.linewidth'] = 1
# plt.rcParams["axes.grid"] = True

df_krx = fdr.StockListing('KRX')
print(df_krx[df_krx.Name == '카카오'])

# KOSPI Index
# df = fdr.DataReader('KS11', '2020')
# print(df.head(5))

# data['Close'].plot()

# Samsung
# data = fdr.DataReader('005930', '2020')

# df.index = df.index.strftime("%Y-%m-%d")
# df.index = df.index.apply(strftime("%Y-%m-%d"))

# Candlestick
# fig, (ax1, ax2, ax3) = plt.subplots(1, 1, gridspec_kw={'height_ratios':[6,2,2]}, sharex=True)
# fig, ax = plt.subplots()
# candlestick(ax1, zip(mdates.date2num(data.index.to_pydatetime()), data.Open, data.High, data.Low, data.Close), width=0.2, colorup='r', colordown='b', alpha=1)
# candlestick(ax1, zip(mdates.date2num(data.index.to_pydatetime()), data.Open, data.High, data.Low, data.Close), width=0.2, colorup='g', colordown='r', alpha=1)
# ax.plot(xdate, data['Close'], label="종가",linewidth=0.7,color='k')
# ax.plot(data.index.to_pydatetime(), data['Close'].rolling(window=5).mean(), label="평균5일",linewidth=0.7)
# ax.plot(data.index.to_pydatetime(), data['Close'].rolling(window=20).mean(), label="평균20일",linewidth=0.7)
# ax.plot(data.index.to_pydatetime(), data['Close'].rolling(window=60).mean(), label="평균60일",linewidth=0.7)
# ax.plot(data.index.to_pydatetime(), data['Close'].rolling(window=120).mean(), label="평균120일",linewidth=0.7)
# candlestick(ax, data.Open, data.High, data.Low, data['Close'], width=0.5, colorup='r', colordown='b')
# fig.set_size_inches(15,30)
# ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
# ax.set_xlabel("날짜")
# ax.set_ylabel("주가(원)")
# plt.xticks(rotation=90)
# plt.legend()
# plt.grid()
# plt.autofmt_xdate()
# plt.tight_layout()
# mpf.plot(df, type='candle', style='charles', mav=(3,7,21), volume=True,
#          title='KOSPI200',
#          ylabel='Price',
#          show_nontrading=False)
# plt.show()