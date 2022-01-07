# Pokemon_game_python_oop_Ex4:                                                                
## Dor Harizi
## Bar Nahmias [[GitHub](https://github.com/BarNahmias)]

# Design and implementation of directed and weighted graphs 

![This is an image](https://user-images.githubusercontent.com/92825016/145035678-cd125e45-64d7-4055-91bb-646ddfbf99ba.png)  

## Getting Started
**libraries:** 
1. import heapq
2. import json
3. import math
4. import sys
5. from abc import ABC
6. from typing import List, Dict, Any
7. from matplotlib import pyplot as pt

8. from src.Graph_Interface.GraphAlgoInterface import GraphAlgoInterface
9. from src.My_Graph.DiGraph import DiGraph
10. from src.My_Graph.NodeData import NodeData as n

## class
1. DiGraph - this class create object from type graph.
2. NodeData - this class create object from type node.
3. EdgeData - this class create object from type edge.
4. Main -  this class the linked to class MyGui,my_Algo and create DirectedWeightedGraph  .
5. GeaphAlgo - this class include  function that we use on graph.
7. MyGui - graphic interface.


## uml :
![image](src/uml.png)  


## GeaphAlgo - function:
#### **init()**
Inits the graph on which this set of algorithms operates on.


#### **shortestPath()**
Computes the length of the shortest path between src to dest
Note: if no such path --> returns -1.
 - this function based on **Diastra** algorithm. 
0. For each vertex, it is marked whether they visited it or not and what is the distance from the vertex of the source, which we will mark in S. At first all the codes are marked as not visited, and distance is defined as infinity.
Algorithm loop:
1. As long as there are codes we did not visit:
2. Mark X (the current vertex. In this first iteration the vertex of the source S) as the vertex visited.
3. For any code that is X and we have not yet visited it:
Y is updated so that its distance is equal to the minimum value between two values: between the current distance, the weight of the arc connecting X and Y and the distance between S and X.
4. Make a new vertex X according to a code that this distance from the source node S is the shortest of all the vertices in the graph that we have not yet visited.
* This site was built using [Wikipedia Pages](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

#### **centerpoint()**
 Finds the NodeData which minimizes the max distance to all the other nodes.
 Assuming the graph isConnected, elese return null. 
 return the Node data to which the max shortest path to all the other nodes is minimized
1. for all node in the graph we find the biggest **shortestPathDist()**.
2. we find the node that the smaller  biggest **shortestPathDist()** .
3. this node is the center node. 
* This site was built using [Wikipedia Pages]( https://en.wikipedia.org/wiki/Graph_center).

#### **tsp()**
Computes a list of consecutive nodes which go over all the nodes in cities.
the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution -
the lower the better.
  - this function based on **greedy** algorithm. 
1. we choosing start node and we find the next node  with the shorter distans .
2. for the node that we found (1) we found agen the next node  with the shorter distans and repeating .
3. from the last node we found the shorter distans to start node. 
* This site was built using [Wikipedia Pages]( https://en.wikipedia.org/wiki/Travelling_salesman_problem).

#### **save()**
 Saves this weighted (directed) graph to the given
 file name - in JSON format.
#### **load()**
This method loads a graph to this graph algorithm.
param file - file name of JSON file

## Run times  :
### Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz   2.30 GHz 12.0 GB RAM 64x

**Building large graphs:**
- 10 Vertices 20 Edges : 0.002 sec
- 1,000 Vertices 10,000 Edges: 0.046 sec
- 10,000 Vertices 100,000 Edges: 0.446 sec
- 100,000 Vertices 1,000,000 Edges: 9.615 sec

**Running Algorithms:**

**centerpoint**:

- 10 Vertices 20 Edges : 0.002 sec
- 1,000 Vertices 10,000 Edges: 5.987 sec
- 10,000 Vertices 100,000 Edges: timeout
- 100,000 Vertices 2,000,000 Edges: timeout

**shortestpath + load file**:

- 10 Vertices 20 Edges : 0.002 sec
- 1,000 Vertices 10,000 Edges: 0.05 sec
- 10,000 Vertices 100,000 Edges: 0.587 sec
- 100,000 Vertices 1,000,000 Edges: 13.385 sec


**tsp  + load file**:

- 10 Vertices 20 Edges : 0.02 sec
- 1,000 Vertices 10,000 Edges: 0.45 sec
- 10,000 Vertices 100,000 Edges: 2.544 sec
- 100,000 Vertices 1,000,000 Edges: timeout

**load + save file**:

- 10 Vertices 20 Edges : 0.01 sec
- 1,000 Vertices 10,000 Edges: 0.3 sec
- 10,000 Vertices 100,000 Edges: 1.64 sec
- 100,000 Vertices 1,000,000 Edges: 4.55

## Performance comparison 
-  java vs python check Performanc of getgraph func  for 10/1000/10000 nodes (in ms) :
![image](https://user-images.githubusercontent.com/92825016/147482950-224c6975-9e99-4c3f-813d-c31ffed29fa1.png)
![image](https://user-images.githubusercontent.com/92825016/147550984-73bbffcd-6115-4bb5-916f-17d4a075bfe1.png)



## GUI - graphic interface :
### When you open 'GUI' from Main class will open panel thet creat the graph from the json file thet you laod:
![image](https://user-images.githubusercontent.com/92825016/147589337-0bbf9e4c-e997-4c37-aa0f-7973c5424a76.png)

### you can chose to operate the functuion(from GraphAlgo) on the graph from menu bar.
![image](https://user-images.githubusercontent.com/92825016/147589388-adda5f37-62ad-4201-8b83-b50e9023cd39.png)

#### you can chose to laod other graph or to save the graph after you  operate the functuion - main menu .
![image](https://user-images.githubusercontent.com/92825016/147589415-415c1557-fa31-4d87-a333-e236294c924c.png)

![image](https://user-images.githubusercontent.com/92825016/147589439-0d0d8b65-d136-452f-9f64-33f5daca8aef.png)

### you can chose to operate the functuion(from DiGraph) on the graph from menu bar. 
![image](https://user-images.githubusercontent.com/92825016/147589465-dae6b9ce-e00a-467d-b23a-8adc86abe7ee.png)

### you can get graph data's , edges and nodes  .
![image](https://user-images.githubusercontent.com/92825016/147589494-9ccd3ea8-bbd0-4cc1-b27c-f1bafab3932d.png)

### When you finish you can to save the graph or to exit from 'GUI'.
![image](https://user-images.githubusercontent.com/92825016/147473376-3886c907-eca3-4b27-a87f-70bcc1b06bba.png)
