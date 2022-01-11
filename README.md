# Pokemon_game_python_oop_Ex4:                                                                
## Dor Harizi
## Bar Nahmias [[GitHub](https://github.com/BarNahmias)]



![This is an image](https://user-images.githubusercontent.com/92825016/148682775-bad02aa0-6a70-494b-abc6-d19409849c50.png)  

## Getting Started
**libraries:** 
1. from My_Graph.EdgeData import EdgeData
2. from My_Graph.NodeData import NodeData
3. from client_python.agentData import agentData
4. from client_python.infoGame import infoGame
5. from client_python.pokemonData import pokemonData
6. from client_python import gameData
7. import numpy as np
8. import pygame
9. import json
10. from client import Client
11. from pygame import gfxdraw
12. from pygame import *

## class in mygraph:
1. DiGraph - this class create object from type graph.
2. NodeData - this class create object from type node.
3. EdgeData - this class create object from type edge.
4. Main -  this class the linked to class MyGui,my_Algo and create DirectedWeightedGraph  .
5. GeaphAlgo - this class include  function that we use on graph.


## class in client:
1. agentData - this class create object from type agent.
2. pokemonData - this class create object from type pokemon.
3. client - this class as it communicating with the "server".
4. student -  in this class the algorthem and the functiom are available  .
5. gameData -  -this class create object from type gameData.

## game vedio clip : 

[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://user-images.githubusercontent.com/92825016/148840391-9837ef43-1d55-4368-8788-5122e5c54453.mp4)



## uml :
![image](https://github.com/DorHarizi/Pokemon_game_python_oop_Ex4/blob/main/uml.png)  


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

## client - function:

#### **loadPockemonsGame()**
This method loads pockemons to this gmae.

#### **loadAgentsGame()**
This method loads Agents to this gmae.

#### **loadInfoGame()**
This method loads "Info" to this gmae.

#### **loadGraphGame()**
This method loads graph to this gmae.

#### **checkPos()**
This method check  if Is the Pokemon on the graph gmae.

#### **pause()**
This method pauses the game.



## pygame- graphic interface :
### When you open 'pygame' from CMD class will open panel thet creat the graph game from the json file thet you laod and the play will run:
![image](https://user-images.githubusercontent.com/92825016/148841035-450d768c-097c-4826-9ece-9a78980043d1.png)

### you can chose to pause the game through the "pause-button" .
![image](https://user-images.githubusercontent.com/92825016/148685635-863993e4-7972-487c-8296-ac7ee4cbcf65.png)

#### You can see the time left for the game.
![image](https://user-images.githubusercontent.com/92825016/148685687-d41b5895-dfb6-4f74-bc3f-ebb84bfd92cd.png)


