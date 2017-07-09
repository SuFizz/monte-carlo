# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 19:51:47 2017

@author: sufiyans
"""
import random
#import numpy as np
#import matplotlib.pyplot as plt

total_distance = 1000

def advance_cars(posn, vel, time):
    dist_travel = 0
    for i in range(total_distance):
        if(posn[time-1][i]):
            temp_vel = min(vel[time-1][i]+1, vmax)

            for j in range(1,temp_vel+1):
                if posn[time-1][(i+j)%total_distance]:
                    temp_vel = j-1
                    break

            if(random.randint(0,10000) >= p):
                temp_vel = max(temp_vel-1, 0)

            if(posn[time][(i+temp_vel)%total_distance] == 1):
                print(time,(i+temp_vel)%total_distance,temp_vel)
                exit()

            posn[time][(i+temp_vel)%total_distance] = 1
            vel[time][(i+temp_vel)%total_distance] = temp_vel
            dist_travel += abs( temp_vel )
    return dist_travel

p = 3333

vmax = 5
burnin = 1000
time = 1000

distances = [[] for il in range(5)]
for iteration in range(5):
    for cars in range(50,501,5):
        print(cars)
        vel = [[0 for ab in range(total_distance)] for jk in range(time+burnin)]
        posn = [[0 for ab in range(total_distance)] for jk in range(time+burnin)]
    
        for i in range(cars):
            while 1:
                idx = random.randint(0,total_distance-1)
                if not posn[0][idx]:
                    posn[0][idx] = 1
                    break
        
        distance_travelled = 0
        for timers in range(1,burnin):
            xyz = advance_cars(posn, vel, timers)
        
        for timers in range(burnin,burnin + time):
            distance_travelled += advance_cars(posn, vel, timers)
    
        distances[iteration].append(distance_travelled)

#np_pos = np.array(posn)

#G = np.zeros((time+burnin, total_distance, 3))
#G[np_pos == 1]  = [1,1,1]
#G[np_pos == 0]  = [0,0,0]

#plt.imshow(G)