import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from mplfinance.original_flavor import candlestick_ohlc
import FinanceDataReader as fdr

# KOSPI200
df = fdr.DataReader('KS11', '2020')

# Set graph attributes
fig, ax = plt.subplots()
fig.suptitle('KOSPI200')
fig.autofmt_xdate()
fig.tight_layout()

ax.set_xlabel('Date')
ax.set_ylabel('Price')

candlestick_ohlc(ax, zip(mdates.date2num(df.index.to_pydatetime()), df.Open, df.High, df.Low, df.Close), width=0.5, colorup='r', colordown='b', alpha=0.8)
ax.plot(df.index.to_pydatetime(), df['Close'].rolling(window=3).mean(), label="3days",linewidth=0.7)
ax.plot(df.index.to_pydatetime(), df['Close'].rolling(window=7).mean(), label="7days",linewidth=0.7)
ax.plot(df.index.to_pydatetime(), df['Close'].rolling(window=21).mean(), label="60days",linewidth=0.7)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))

plt.style.use('ggplot')
plt.legend()
plt.show()