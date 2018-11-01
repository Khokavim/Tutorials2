#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:10:20 2018

@author: mishael
"""

import pandas as pd

data = pd.read_csv('phone.csv', delimiter=":")
print(data)