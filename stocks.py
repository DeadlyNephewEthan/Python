#CLASS ONE 

# Description: This program uses an artificial recurrent neural network called Long Short Term Memory (LSTM)
#              to predict the closing stock price of a corporation (Apple Inc.) using the past 60 day stock price.

#CLASS TWO

#Import the libaries
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#CLASS THREE

# Get the stock quote
df = web.DataReader('MSFT', data_source='yahoo', start='2012-01-01', end='2021-1-15')
#show the data
df

#CLASS FOUR

#visualize the closing price history
plt.figure(figsize=(16,8))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.show()


#SIDE NOTE
#please use Google Colaboratory
#   https://www.youtube.com/watch?v=agj3AxNPDWU
