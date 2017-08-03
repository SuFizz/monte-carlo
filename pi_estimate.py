# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 00:16:09 2017

@author: sufiyans
"""

import numpy as np

counter = 0
for jj in range(1000):
    n = 1000
    l = np.random.uniform(0,1,n)
    r = np.random.uniform(0,1,n)
    X = [(l[i],r[i]) for i in range(n)]
    Y = [1 if l[i]**2 + r[i]**2 <=1 else 0 for i in range(n)]
    Mu = np.mean(Y)
    S = np.std(Y)*len(Y)/(len(Y)-1)
    counter = counter + (np.pi >= 4*(Mu-1.96*S/np.sqrt(n)) and np.pi <= 4*(Mu+1.96*S/np.sqrt(n)))

print (counter)