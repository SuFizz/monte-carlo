# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:24:11 2017

@author: sufiyans
"""

import numpy as np
def random_vector(d):
    return np.random.uniform(0,1,size=(d,1))

def BDist(vector):
    return min([min(i,1-i) for i in vector])

def CDist(vector):
    return abs(sum([ (i-0.5) for i in vector] ) )/np.sqrt(len(vector))

d = 2
iters = 100000
epsilon = 0.1
trials = [2,3,4,5,10,20]

for d in trials:
    num_inx = 0
    for i in range(iters):
        rv = random_vector(d)
        if(BDist(rv) <= epsilon and CDist(rv) <= epsilon):
            num_inx += 1
    print(num_inx/float(iters))