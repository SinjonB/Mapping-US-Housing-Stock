# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:03:52 2017

@author: sbartel
"""

def sortRegion(df, region):
    sortDF = df[df.apply(lambda x: x['CENDIV'] == region, axis = 1)]
    return sortDF