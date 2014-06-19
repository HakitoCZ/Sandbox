#!/usr/bin/pytho3
'''
Set of examples for counting several gamedev stuff.
Origin: playlist?list=PLW3Zl3wyJwWOpdhYedlD-yCB7WQoHf-My
Used 2 space indent
'''

## TODO:
##   Put all examples into functions

# PacMan - P
# Inky the Ghost - I
# Clyde - C
# Pinky - 
# Blinky - 

# Positions
P = (0, -1)
I = (1, 1)
C = (2, -1)

# Basic vector
# IP - Inky to PacMan
# IP = I - P
# Pacman standing and Inky's distance enshortens
IP = (P[0] - I[0], P[1] - I[1]) # (-1, -2)
CP = (P[0] - C[0], P[1] - C[1]) # (-2, 0)

# Distance
# Vector length
# To compare those two isn't math.sqrt() needed
IP_dist = (IP[0]**2 + IP[1]**2) # 5
CP_dist = (CP[0]**2 + CP[1]**2) # 4

# Speed
# End of vector isn't destination point but \
#   the force by which it pulled
# NEED CHECK
## IP_twice_fast = (IP[0]*2, IP[1]*2)
## IP_half_fast = (IP[0]/2, IP[1]/2)
## IP_twice_fast2 = IP_dist * 2

# Looking direction
# vector with length == 1
# aka Normal length vectors
# IP_dir =  (IP / PI_dist)
IP_dir = (IP[0] / IP_dist, IP[1] / IP_dist)
