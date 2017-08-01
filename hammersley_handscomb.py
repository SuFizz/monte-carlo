# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 23:34:20 2017

@author: sufiyans
"""
import numpy as np
import matplotlib.pyplot as plt
num_comets = 100000
x0 = -1
new_x = x0
sigma = 1
mean = 0
Time = 0
times = []

for i in range(num_comets):
    print(i)
    while new_x<=0:
        Time += (-new_x)**(-3/2)
        new_x = new_x + np.random.normal(mean,sigma)
    times.append(Time)
    new_x = x0
    Time = 0
log_times = np.log10(times)
plt.hist(log_times)