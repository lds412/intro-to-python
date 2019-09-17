# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:48:13 2019

@author: lydia
"""

#==========================================
# Purpose: 
#   Calculates the contracted distance between two objects according to 
#   Einstein's Theory of Special Relativity 
# Input Parameter(s): 
#   dist - original distance (in meters) between two objects
#   speed - speed (in meters/second) at which we are travelling relative to 
#   the two objects
# Return Value(s): 
#   The contracted distance between the two objects from our frame of 
#   reference
#==========================================

def length_contract(dist,speed):
    c=3*10**8
    L = dist*(1-(speed**2/c**2))**0.5
    return L


#==========================================
# Purpose: 
#   Calculates the time it takes for Friedrich Bessel to complete a 
#   12 parsecs long run from his perspective and from a stationary bystander's
#   perspective
# Input Parameter(s): 
#   speed - Bessel’s average speed in the run (in meters/second)
# Return Value(s): 
#   The time required to traverse the segment, as seen by Bessel, in years
#==========================================

def bessel_run(speed):
    distance = 12*3.086*10**16
    stationary_time = distance/(speed*31557600)
    print(stationary_time)
    bessel_time = length_contract(distance,speed)/(speed*31557600)
    return bessel_time


#==========================================
# Purpose: 
#   Prints out the sentence "Who needs loops?" 5 times
# Input Parameter(s): 
#   None
# Return Value(s): 
#   None
#==========================================

def print_5():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")


#==========================================
# Purpose: 
#   Prints out the sentence "Who needs loops?" 25 times
# Input Parameter(s): 
#   None
# Return Value(s): 
#   None
#==========================================
    
def print_25():
    print_5()    
    print_5() 
    print_5() 
    print_5() 
    print_5() 


#==========================================
# Purpose: 
#   Prints out the sentence "Who needs loops?" 100 times
# Input Parameter(s): 
#   None
# Return Value(s): 
#   None
#==========================================

def print_100():
    print_25()
    print_25()
    print_25()
    print_25()