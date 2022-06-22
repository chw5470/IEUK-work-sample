#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 01:46:35 2022

@author: chialin5470
"""


import numpy as np
import pandas as pd


class Grid:
    
    def __init__(self):
        #setting up the grid(dataframe), including the wall
        #the wall noted with obstacles to avoid index out of bounds
        self.df = pd.DataFrame(np.zeros((12, 12)))
        self.df.index = ['Wall', '0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'Wall']
        self.df.columns = ['Wall', '0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'Wall']
        self.df['Wall'] = "|"
        self.df.loc['Wall'] = "--"
        
        #starting position(in index)
        self.x = 1
        self.y = 1
        self.plist = []
        
    def set_obstacles(self):
        #1 for obstacle 0 for empty block
        #these are the known positions of the obstacles
        self.df.iloc[8,8] = 1
        self.df.iloc[8,9] = 1
        self.df.iloc[8,10] = 1
        self.df.iloc[9,8] = 1
        print(self.df)
    
    def random(self):
        nplist = np.random.random_integers(9, size=(20,2))
        for i in nplist:
            self.df.iloc[i] = 1            
        print(nplist)
        print(self.df)
        
        
    def moving(self):
        while (self.x != 10 or self.y != 10):
            #mark as 'x' to note it's walked before
            self.df.iloc[self.y, self.x] = 'x'
            #list to record path
            tuplist = [self.x-1, self.y-1]
            self.plist.append(tuplist.copy())
            
            #my testing sequence
            if self.df.iloc[self.y + 1, self.x +1] == 0:
                self.x = self.x + 1
                self.y = self.y +1
            elif self.df.iloc[self.y + 1, self.x] == 0:
                self.y = self.y + 1
            elif self.df.iloc[self.y, self.x +1] == 0:
                self.x = self.x +1
            elif self.df.iloc[self.y + 1, self.x - 1] == 0:
                self.x = self.x - 1
                self.y = self.y + 1
            elif self.df.iloc[self.y - 1, self.x + 1] == 0:
                self.x = self.x + 1
                self.y = self.y - 1
            elif self.df.iloc[self.y, self.x-1] == 0:
                self.x = self.x - 1
            elif self.df.iloc[self.y - 1, self.x] == 0:
                self.y = self.y - 1            
            elif self.df.iloc[self.y - 1, self.x - 1] == 0:
                self.x = self.x - 1
                self.y = self.y - 1
            else:
                print("Unable to reach delivery point")
        #destination marked as *
        self.plist.append([9,9])
        self.df.iloc[10,10] = '*'
        print(self.plist)
        print(self.df)
                
                    
        
def main():

    thisgrid = Grid()
    thisgrid.set_obstacles()
    #thisgrid.random()
    thisgrid.moving()
    
        
    
main()
    

    
    
