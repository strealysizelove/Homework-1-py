# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:30:55 2022

@author: Strealy Sizelove
"""

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np 

import statsmodels.formula.api as sm # module for stats models
from statsmodels.iolib.summary2 import summary_col # module for presenting stats models outputs nicely


# %%
def price2ret(prices,retType='simple'):
    if retType == 'simple':
        ret = (prices/prices.shift(1))-1
    else:
        ret = np.log(prices/prices.shift(1))
    return ret

# %%
from pathlib import Path
import sys
import os

home = str(Path.home())
print(home)


# %% 
if sys.platform == 'linux':
    inputDir = '/datasets/stocks/' 
elif sys.platform == 'win32':
    inputDir = 'C:\\Users\\Strealy Sizelove\\datasets\\stocks' 
else :
    inputDir = '/datasets/stocks/'
    
fullDir= home+inputDir
print(fullDir)

# %%
stkName = 'LULU'
fileName = 'stk_' + stkName + '.csv'
readFile = fileName 

df_stk = pd.read_csv(readFile,index_col='Date',parse_dates=True)
df_stk.head()


# %%
stkName = 'TGT'
fileName = 'stk_' + stkName + '.csv'
readFile = fileName 

df_stk1 = pd.read_csv(readFile,index_col='Date',parse_dates=True)
df_stk.head()

# %%
stkName = 'SBUX'
fileName = 'stk_' + stkName + '.csv'
readFile = fileName 

df_stk2 = pd.read_csv(readFile,index_col='Date',parse_dates=True)
df_stk.head()

# %%
stkName = 'wLULU'
fileName = 'stk_' + stkName + '.csv'
readFile = fileName 

df_stk3 = pd.read_csv(readFile,index_col='Date',parse_dates=True)
df_stk.head()

# %%
stkName = 'wTGT'
fileName = 'stk_' + stkName + '.csv'
readFile = fileName 

df_stk4 = pd.read_csv(readFile,index_col='Date',parse_dates=True)
df_stk.head()

# %%
stkName = 'wSBUX'
fileName = 'stk_' + stkName + '.csv'
readFile = fileName 

df_stk5 = pd.read_csv(readFile,index_col='Date',parse_dates=True)
df_stk.head()

plt.plot(df["Date"],df["TGT"], label="TGT")
plt.plot(df["Date"],df["wTGT"], label="wTGT")
plt.plot(df["Date"],df["LULU"], label="LULU")
plt.plot(df["Date"],df["wLULU"], label="wLULU")
plt.plot(df["Date"],df["SBUX"], label="SBUX")
plt.plot(df["Date"],df["wSBUX"], label="wSBUX")


#This is pretty much the design of the plot
plt.tight_layout()
plt.title("YF & BB Data LULU, TGT, & SBUX Stock Returns", size = 20)
plt.legend() 
plt.show()
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
%config InlineBackend.figure_format = 'svg'
print (df) 
