"""This script demonstrates how to calculate and plot rolling n-period averages"""

import datetime as dt

import matplotlib.pyplot as plt
import yfinance as yf

# download stock price data from yahoo
years = 70
tickers = ["^GSPC", "AAPL"]
now_dttm = dt.datetime.now(tz=dt.timezone.utc)
end = dt.date(now_dttm.year, now_dttm.month, 1)
start = dt.date(end.year - years, end.month, end.day)
print(start, "~", end)

df_prices = yf.download(tickers, start, end, auto_adjust=False)["Adj Close"]
df_prices.head()
df_prices.tail()

# extract SP500 daily prices as a series
sp500_daily_prices = df_prices[tickers[0]]
sp500_daily_prices

# calc its weekly averages
weekly_avgs = sp500_daily_prices.resample("W").mean()
weekly_avgs.name = "Weekly Average"
weekly_avgs

# calc its 200-week moving averages
moving_avgs_200w = weekly_avgs.rolling(200).mean()
moving_avgs_200w.name = "200-Week Moving Average"
moving_avgs_200w

# plot both series on one figure
fig, ax = plt.subplots(figsize=(10, 6))
weekly_avgs.plot(ax=ax)
moving_avgs_200w.plot(ax=ax)
ax.legend()
ax.set_title("S&P 500 Adj. Closes")
