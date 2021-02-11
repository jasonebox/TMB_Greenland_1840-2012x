#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:14:38 2021

@author: jeb
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('/Users/jason/Dropbox/TMB_1840-2010_Box_and_Colgan_2013/Greenland_mass_balance_totals_1840-2012_ver_20141130_with_uncert.csv')

print(df.columns)

plt.plot(df.year,df.TMB)
plt.ylabel('Gt')