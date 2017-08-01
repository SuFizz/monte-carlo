# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 23:49:30 2017

@author: sufiyans
"""
import numpy as np
import matplotlib.pyplot as plt
total = 10000
e = np.random.geometric(0.001,total)

r = [sum(e==j) for j in range(2*total)]
f = [i/float(total) for i in r]

plt.plot(f)
final = [i*r[i]/float(total) for i in range(len(r))]
plt.plot(final)