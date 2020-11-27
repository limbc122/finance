import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import talib as ta

# Technical Analysis Static Variables
SMA_FAST = 5
SMA_SLOW = 10

RSI_PERIOD = 14
RSI_AVG_PERIOD = 15

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

STOCH_K = 14
STOCH_D = 3

SIGNAL_TOL = 3
Y_AXIS_SIZE = 12

def analyze(context, data):  
    data['sma_f'] = data.CLS_PRC.rolling(window=SMA_FAST,center=False).mean()
    data['sma_s'] = data.CLS_PRC.rolling(window=SMA_SLOW,center=False).mean()
    data['rsi'] = ta.RSI(data.CLS_PRC.values, RSI_PERIOD)
    data['macd'], data['macdSignal'], data['macdHist'] = ta.MACD(data.CLS_PRC.as_matrix(), fastperiod=MACD_FAST, slowperiod=MACD_SLOW, signalperiod=MACD_SIGNAL)

    # Price peak and valley
    # indices = peakutils.indexes(data['price'], valley=False, thres=0.3, min_dist=1, thres_abs=False)
    peaks, valleys = indic.get_peaknvalley(data.CLS_PRC, edge=None, valley=False, threshold=0.3)
    data['price_pnv'] = 0
    data['price_pnv'].iloc[peaks].value = 1
    data['price_pnv'].iloc[valleys].value = -1
    data['zigzag'] = zigzag.peak_valley_pivots(np.array(data['CLS_PRC']), 0.01, -0.01)

    # Related to stoch
    data['stoch_k'], data['stoch_d'] = ta.STOCH(data.HIGH_PRC.values, data.LOW_PRC.values, data.CLS_PRC.values, fastk_period=14, slowk_period=3, slowd_period=3)
    # data['stoch_k'], data['stoch_d'] = indic.STO(data.HIGH_PRC, data.LOW_PRC, data.CLS_PRC, nK=14, nD=3, nS=3)
    peaks, valleys = indic.get_peaknvalley(data.stoch_k, edge=None, valley=False, threshold=0.3)
    data['stoch_pnv'] = 0
    data['stoch_pnv'].iloc[peaks] = 1
    data['stoch_pnv'].iloc[valleys] = -1
    data['stoch_zigzag'] = zigzag.peak_valley_pivots(np.array(data['stoch_k']), 0.01, -0.01)

    data['vol_chg'] = data['VOLUME'].pct_change(fill_method='ffill')
    data['CDL3INSIDE'] = ta.CDL3INSIDE(data.OPEN_PRC, data.HIGH_PRC, data.LOW_PRC, data.CLS_PRC)
    
    
    #data['sma'] = np.where(data.sma_f > data.sma_s, 1, 0)
    #data['macd_test'] = np.where((data.macd > data.macdSignal), 1, 0)
    #data['stoch_k_test'] = np.where((data.stoch_k < 50) & (data.stoch_k > data.stoch_k.shift(1)), 1, 0)
    #data['rsi_test'] = np.where((data.rsi < 50) & (data.rsi > data.rsi.shift(1)), 1, 0)

    return data