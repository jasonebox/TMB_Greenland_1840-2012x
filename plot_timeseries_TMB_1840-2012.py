#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:14:38 2021

@author: jeb@geus.dk

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/Users/jason/Dropbox/TMB_Greenland_1840-2012/')

font_size=16
plt.style.use('default')
# plt.rcParams['font.sans-serif'] = ['Georgia']
plt.rcParams["font.size"] = font_size 
plt.rcParams["mathtext.default"]='regular'
fig=plt.figure(figsize=(16,10))

df=pd.read_csv('./Greenland_mass_balance_totals_1840-2012_ver_20141130_with_uncert_via_Kjeldsen_et_al_2015.csv')

dfBC=pd.read_csv('./Greenland_mass_balance_1840-2011_Box_and_Colgan_2013.txt',delim_whitespace=True)
print(dfBC.columns)

plt.title('Greenland land ice total mass balance reconstruction 1840-2012')
plt.plot(dfBC.Year,dfBC.TMB,c='b',label='Box and Colgan 2013')
plt.plot(df.year,df.TMB,c='r',label='via Kjeldsen et al (2015)')
plt.axhline(y=0,linestyle='--',c='grey',)
plt.ylabel('Gt')
plt.xlim(1838,2014)
plt.legend(loc=3)

ly='p'

if ly =='x':plt.show()

if ly =='p':
    plt.savefig('./plot_timeseries_TMB_1840-2012.png', dpi=100, bbox_inches='tight')