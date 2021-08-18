
'''
Purpose: find the spots where participants (or students) sitting in a meeting room will be at the maximum distance from each other
Assumption: participants are sitting in a rectangular room, with no obstructions
Two criteria have been used: first maximizes the minimum distance between the participants; the second maximizes the average distance between participants
The code does take time to run as you increase the number of available positions and participants. As such, I use a random sample if the number of combinations exceeds 100k.

Author: Manish Jha
'''


#### user defined
nrows = 4 #number of rows
ncols = 12 #number of seats per rows
nseats = 14 #number of students 

################

## get a list of seats as coordinates
coords = [(x,y) for x in range(0,ncols) for y in range(0,nrows)] 

## find distances
from itertools import combinations
from scipy.spatial import distance

mindist = 0 ## a random small number
sumdist = 0 ## a random small number
minsumdist = 0 ## a random small number

### total number of combinations we need to run
from math import factorial
totalcombs = factorial(nrows*ncols)/factorial(nrows*ncols - nseats)/factorial(nseats)
# print(totalcombs)

## it takes lot of time above 100k combinations, so we cap it 
allcombs = combinations(coords, nseats)

import random  
if totalcombs > 1000000:
    allcombs = [random.choices(coords,k=nseats) for rcount in range(1000000)]
    allcombs = [x for x in allcombs if len(set(x)) == nseats] #keep unique
    print("Got ", len(allcombs)/1000, "k random sample")

counter = 0
for combs in allcombs: #combination of nseats   

    counter = counter + 1 ### printing in between to keep tab of time
    if counter%10000 == 0:
        print(counter/1000, "k of combinations done")
    
    combs = list(combs)
    # print(combs)
    
    dists = []
    for coord in combs: #coordinate of a point in the combination
        
        opoints = combs.copy()
        opoints.remove(coord) ## otherpoints for distance
        dists.extend([distance.euclidean(coord, opoint) for opoint in opoints])
        
    if min(dists) > mindist or (min(dists) == mindist and sum(dists) > minsumdist): ## maximize the minimum distance, also reduce average distance for minimum
        mindistcomb = combs
        mindist = min(dists)
        minsumdist = sum(dists)
        print("min and avg distance", mindist, minsumdist)
        
    if sum(dists) > sumdist: ## maximize the sum of distance
        sumdistcomb = combs
        sumdist = sum(dists)
        
        
        
## print best results
print("Combination that maximize minimum distance: ", mindistcomb)
print(".. with minimum distance: ", mindist)
print(".. and average distance: ", minsumdist)
print("\n")
print("Combination that maximize average distance: ", sumdistcomb)
print(".. with average distance: ", sumdist/nseats)

## plot best results
import numpy as np
import matplotlib.pyplot as plt
colors = np.random.rand(nseats)

x = [a_tuple[0] for a_tuple in mindistcomb]
y = [a_tuple[1] for a_tuple in mindistcomb]
plt.scatter(x, y, s=nrows*ncols*60/nseats, c=colors, alpha=0.7)
plt.title("Maximize minimum distance")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(min(y), max(y)+1, 1.0))
plt.grid(alpha=0.3)
plt.savefig('maxmin.png')
plt.show()

x = [a_tuple[0] for a_tuple in sumdistcomb]
y = [a_tuple[1] for a_tuple in sumdistcomb]
plt.scatter(x, y, s=nrows*ncols*60/nseats, c=colors, alpha=0.7)
plt.title("Maximize average distance")
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(min(y), max(y)+1, 1.0))
plt.grid(alpha=0.3)
plt.savefig('maxavg.png')
plt.show()






