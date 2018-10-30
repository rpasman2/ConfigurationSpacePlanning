# geometry.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains geometry functions that relate with Part1 in MP2.
"""

import math
import numpy as np
from const import *

def computeCoordinate(start, length, angle):
    """Compute the end cooridinate based on the given start position, length and angle.

        Args:
            start (tuple): base of the arm link. (x-coordinate, y-coordinate)
            length (int): length of the arm link
            angle (int): degree of the arm link from x-axis to couter-clockwise

        Return:
            End position of the arm link, (x-coordinate, y-coordinate)
    """
    new_angle = angle * math.pi/180
    x = start[0] + length*math.cos(new_angle)
    y = start[1] - length*math.sin(new_angle)
    return (math.trunc(x),math.trunc(y))

def doesArmTouchObstacles(armPos, obstacles):
    """Determine whether the given arm links touch obstacles

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            obstacles (list): x-, y- coordinate and radius of obstacles [(x, y, r)]

        Return:
            True if touched. False it not.
    """  
    
    for obstacle in obstacles:
        for arm in armPos:
            x = arm[0]
            y = arm[1]
            dist = abs((y[1] - x[1])*(obstacle[0]) - (y[0] - x[0])*(obstacle[1]) + (x[1]*y[0]) - (y[1]*x[0]))/math.sqrt((y[1] - x[1])**2 + (y[0] - x[0])**2)
            dist_x = math.sqrt((x[0] - obstacle[0])**2 + (x[1] - obstacle[1])**2)
            dist_y = math.sqrt((y[0] - obstacle[0])**2 + (y[1] - obstacle[1])**2)
            if y[0] == x[0]:
                i = x[0]
                j = obstacle[1]
            else:  
                m = (y[1] - x[1]) / (y[0] - x[0])
                k = x[1] - m*x[0]
                i = (obstacle[0] + m*obstacle[1] - m*k) / (m**2 + 1)
                j = m*(i) + k
            if y[0] > x[0]:
                test_i = i >= x[0] and i <= y[0]
            else:
                test_i = i >= y[0] and i <= x[0]
            if y[1] > x[1]:
                test_j = j >= x[1] and j <= y[1]
            else:
                test_j = j >= y[1] and j <= x[1]
            if (dist <= obstacle[2] and test_i and test_j) or dist_x <= obstacle[2] or dist_y <= obstacle[2]:
                return True       
    return False

def doesArmTouchGoals(armEnd, goals):
    """Determine whether the given arm links touch goals

        Args:
            armEnd (tuple): the arm tick position, (x-coordinate, y-coordinate)
            goals (list): x-, y- coordinate and radius of goals [(x, y, r)]

        Return:
            True if touched. False it not.
    """
    
    for goal in goals:
        dist = math.sqrt((armEnd[0] - goal[0])**2 + (armEnd[1] - goal[1])**2)
        if dist <= goal[2]:
            return True
    return False


def isArmWithinWindow(armPos, window):
    """Determine whether the given arm stays in the window

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            window (tuple): (width, height) of the window

        Return:
            True if all parts are in the window. False it not.
    """
    width = window[0]
    height = window[1]
    for arm in armPos:
        x = arm[0]
        y = arm[1]
        if x[0] < 0 or x[0] > width or y[0] < 0 or y[0] > width or x[1] < 0 or x[1] > height or y[1] < 0 or y[1] > height:
            return False  
    return True