#Dijkstra's Algorithm, written by Peter Clark
#This is an implementation of Dijkstra's algorithm which aims to find the distance from a source to all destination nodes.

import operator
from operator import itemgetter

class Node:
    def __init__ (self, name):
        self.name = name
        self.distance = 9999999
        self.links = []
        self.predecessor = None

nodes = []

def identifyNodeByName(name):
    targetNode = None
    for node in nodes:
        if node.name == name:
            targetNode = node
    return targetNode
    

numNodes = int(input("How many nodes are there? "))
#Adds basic nodes to list
for i in range(numNodes):
    name = input("What is the name of node " + str(i + 1) + "? ")
    nodes.append(Node(name))

#Establishes links between nodes
for i in range(numNodes):
    links = []
    numLinks = int(input("How many links does node " + nodes[i].name + " have?"))
    for j in range(numLinks):
        link = input("What node is link " + str(j + 1) + " with? ")
        cost = float(input("What is the cost of this link? "))
        links.append([link,cost])
    nodes[i].links = links

rootNode = identifyNodeByName(input("Which node is the root node? "))
rootNode.distance = 0
fringe = []
notFringe = nodes[:]

#The algorithm
step = 1
while len(fringe) < numNodes:
    #Adding the least-distance value to the fringe
    notFringe = sorted(notFringe,key=lambda node : node.distance)
    links = notFringe[0].links
    dist = notFringe[0].distance
    fringe.append(notFringe[0])
    notFringe.pop(0)
    #Updating the shortest distances
    for i in range(len(links)):
        node = identifyNodeByName(links[i][0])
        if node in notFringe:
            if node.distance > dist + links[i][1]:
                node.distance = dist + links[i][1]
                node.predecessor = fringe[len(fringe) - 1]
    #Printing the result of the iteration
    print ("Step " + str(step) + "\n N' = ", end = "")
    for i in range(len(fringe)):
        print(fringe[i].name, end = "")
    print("\n")
    for node in notFringe:
        if node.predecessor is None:
            print(node.name + " " + str(node.distance))
        else:
            print(node.name + " " + str(node.distance) + " " + str(node.predecessor.name))
    step = step + 1
    input()
