#!/usr/bin/pytho3
'''
Set of examples for counting several gamedev stuff.
Origin: playlist?list=PLW3Zl3wyJwWOpdhYedlD-yCB7WQoHf-My
Used 2 space indent
'''


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
# Pacman standing and Inky's distance enshortens
IP = (P[0] - I[0], P[1] - I[1]) # (-1, -2)
CP = (P[0] - C[0], P[1] - C[1]) # (-2, 0)

# Distance
# Vector length
# no need to math.sqrt() - only to compare
IP_dist = (IP[0]**2 + IP[1]**2) # 5
CP_dist = (CP[0]**2 + CP[1]**2) # 4

# Speed
# End of vector isn't destination point but \
#   the force by which it pulled
IP_twice_fast = (IP[0]*2, IP[1]*2)
IP_half_fast = (IP[0]/2, IP[1]/2)

