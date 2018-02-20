#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 23:37:25 2018
CMPLXSYS 530 | Winter 2018
HW 3: Langton's Ants
@author: lixi
Model 1 - single ant, wrapped boundary 
"""
# setup
import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import scipy as SP

width = 100          # uses x, always config[y,x], index starts from 0 # 50
height = 100         # uses y, always config[y,x] 50, index starts from 0 # 50
# max_time = 15000    # min 10,000 steps for HW, use Step Once

# initialize
def init():
    global time, max_time, A, config, nextConfig # two config placeholders for synchronous updates
    # first config is for looking up states, next config is for updating next states

    time = 0
    
    config = SP.zeros([height, width]) #numpy array full of zero's
    # assign ants' starting position
    A = {                   # set of x,y-positions and deg orientation of all ants
      'ant1':[width/2, height/2, 90]    # deg orientation: 0=North, 90=East -90=West 
      }

    nextConfig = SP.zeros([height, width]) #numpy array full of zero's

# display
def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary) #color according to states
    PL.plot(A['ant1'][0]+0.5,A['ant1'][1]+0.5, marker='o', markersize=200/width, color='red')
    PL.axis('image')
    PL.title('t = ' + str(time) + ' | Ant: ' + str(A['ant1']))
  
# run
def step():
    global time, max_time, A, config, nextConfig
    
    # while time < max_time:
    # advance step counter
    time += 1

    # Change agent states
    for ant in A:
        ant_x = A[ant][0]
        ant_y = A[ant][1]
        orientation = A[ant][2]
        
        for y in xrange(height):
            for x in xrange(width):
                state = config[y,x]
                change = 0
            
                if x == ant_x and y == ant_y:
                    change = 1 # change = yes
            
                #State-transition func: change states according to observations
                if state == 0 and change == 1:      # if cell is white
                    state = 1                       # change cell to black
                    orientation -= 90               # turn left
                elif state == 1 and change == 1:    # if cell is black
                    state = 0                       # change cell to white
                    orientation += 90               # turn right
                
                nextConfig[y,x] = state
                
        # Change patch states
        config, nextConfig = nextConfig, config
                    
        # Step func:
        if abs(orientation+360)%360 == 0:     # filter for North
            orientation = 0
            ant_y = (ant_y+1)%height      # step up 1 & wrap around
        elif abs(orientation+360)%360 == 90:  # filter for East
            orientation = 90
            ant_x = (ant_x+1)%width       # step right 1 & wrap around 
        elif abs(orientation+360)%360 == 180: # filter for South
            orientation = 180
            ant_y = (ant_y-1)%height      # step down 1 & wrap around
        else:                             # filter for West
            orientation = 270
            ant_x = (ant_x-1)%width       # step left 1 & wrap around
        
        # Change agent states            
        A[ant]= [ant_x, ant_y, orientation]    

import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])


