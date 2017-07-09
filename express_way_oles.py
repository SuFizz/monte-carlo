# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 23:32:20 2017

@author: sufiyans
"""

import math

def ole_cord(m,n):
    return m/math.sqrt(m**2 + n**2), n/math.sqrt(m**2 + n**2)
    

def Ddist(a1, a2, b1, b2):
    return math.sqrt( (a1-b1)**2 + (a2-b2)**2 )

def Edist(a1, a2, b1, b2):
    _a1,_a2 = ole_cord(a1,a2)
    _b1,_b2 = ole_cord(b1,b2)
    return Ddist(a1, a2, _a1, _a2) + Ddist(b1, b2, _b1, _b2)

def find_dist(a1, a2, b1, b2):
    return min(Ddist(a1, a2, b1, b2), Edist(a1, a2, b1, b2))

print(find_dist(0.45,0.05,0.05,0.45))