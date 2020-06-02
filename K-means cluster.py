#K-means Cluster algotithm, written by Peter Clark
#Given a set of co-ordinates and clusters, this program should be able to group data via the K-means Cluster algorithm.

import math

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = {}
        self.lastCluster = None
        self.thisCluster = None
    def __str__(self):
        string = "(" + str(self.x) + "," + str(self.y) + ")"
        for v in self.distance.values():
            string = string + " " + (str(round(v,1)))
        string = string + " " + str(self.thisCluster)
        return string

class Cluster:
    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.coords = []

    def __str__(self):
        return(self.name)

def checkEqual(coords):
    #Checks if we need another iteration
    equal = True
    for coord in coords:
        if not(coord.lastCluster == coord.thisCluster) or coord.thisCluster is None:
            equal = False
    return equal

def average(coords):
    #Calculates the average of a list of co-ordinates
    x = 0
    y = 0
    for coord in coords:
        x = x + coord.x
        y = y + coord.y
    x = round(x / len(coords),1)
    y = round(y / len(coords),1)
    return x,y
        

print("K-means Cluster calculator")
num = int(input("How many co-ordinates are there?"))
coords = []
for i in range(num):
    x = float(input("What is the x value of co-ordinate "  + str(i) + "? "))
    y = float(input("What is the y value of co-ordinate "  + str(i) + "? "))
    coords.append(Coordinate(x,y))

#User input (via shell)
clusters = []
num = int(input("How many clusters are there?"))
for i in range(num):
    x = float(input("What is the x value of clusters "  + str(i) + "? "))
    y = float(input("What is the y value of clusters "  + str(i) + "? "))
    clusters.append(Cluster("A" + str(i),x,y))

while not checkEqual(coords):
    for cluster in clusters:
        cluster.coords = []
    for coord in coords:
        coord.distance = {}
        coord.lastCluster = coord.thisCluster
        for cluster in clusters:
            #Finds Euclidean distance
            eucl = math.sqrt((cluster.x - coord.x)**2 + (cluster.y - coord.y)**2)
            coord.distance[cluster] = eucl
        min_val = min(coord.distance.values())
        coord.thisCluster = [k for k, v in coord.distance.items() if v == min_val][0]
        coord.thisCluster.coords.append(coord)
        print(str(coord))
    for cluster in clusters:
        cluster.x, cluster.y = average(cluster.coords)
        print(str(cluster) + " Average = (" + str(cluster.x) + "," + str(cluster.y) + ")")

        
