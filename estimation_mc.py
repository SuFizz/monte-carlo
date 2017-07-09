# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 22:47:40 2017

@author: sufiyans
"""

import random
import math

X = 1
Y = 3/5

distance = 0.0
times = 100000

for i in range(times):
    pt_Xx = random.uniform(0,X)
    pt_Xy = random.uniform(0,Y)
    
    pt_Yx = random.uniform(0,X)
    pt_Yy = random.uniform(0,Y)
    
    distance += math.sqrt( (pt_Xx - pt_Yx)**2 + (pt_Xy - pt_Yy)**2 )
    
print(distance/times)