#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 16:23:00 2017

@author: sinjonbartel
"""
import pandas as pd

with open("soc15.csv","r") as f:
    df = pd.read_csv(f)
    
frame = df.groupby(['DIV','FRAME']).WEIGHT.sum()

               
SQFS = df.groupby(['DIV']).SQFS*df.groupby(['DIV']).SQFS.WEIGHT