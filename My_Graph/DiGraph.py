from abc import ABC
from My_Graph.NodeData import NodeData
from Graph_Interface.GraphInterface import GraphInterface
from My_Graph.EdgeData import EdgeData


class DiGraph(GraphInterface, ABC):

    def __init__(self):
        self.list_Of_Nodes = dict()
        self.list_of_Edge_Dest = dict()
        self.list_of_Edge_Src = dict()
        self.list_of_Edges = dict()
        self.size_Of_Edge = 0
        self.xMax = -float('inf')
        self.xMin = float('inf')
        self.yMax = -float('inf')
        self.yMin = float('inf')
        self.mC = 0

    def __repr__(self):
        return 'Nodes:(%s)' % self.list_Of_Nodes + \
               '\nEdges:(%s)' % self.list_of_Edge_Src

    """
    Return the node with this key of vertices in this graph.
    """

    def get_node(self, key) -> NodeData:
        return self.list_Of_Nodes.get(key)

    """
    Returns the number of vertices in this graph.
    """

    def v_size(self) -> int:
        return len(self.list_Of_Nodes)

    """
    Returns the number of edges in this graph.
    """

    def e_size(self) -> int:
        return self.size_Of_Edge

    """
    Return a dictionary of all the nodes in the Graph, each node is represented using a pair
    """

    def get_all_v(self) -> dict:
        return self.list_Of_Nodes

    """
    Return a dictionary of all the nodes connected to (into) node_id,
    each node is represented using a pair (other_node_id, weight)
    """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.list_Of_Nodes.get(id1) is not None:
            if self.list_of_Edge_Dest[id1] is not None:
                return self.list_of_Edge_Dest[id1]

    """
    Return a dictionary of all the nodes connected from node_id , 
    each node is represented using a pair (other_node_id, weight)
    """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.list_Of_Nodes.get(id1) is not None:
            if self.list_of_Edge_Src[id1] is not None:
                return self.list_of_Edge_Src[id1]

    """
    Returns the current version of this graph.
    """

    def get_mc(self) -> int:
        return self.mC

    """
    Adds an edge to the graph.
    Apply the with if the edge already exist
    """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.list_Of_Nodes is not None:
            if self.list_Of_Nodes.get(id1) is not None and self.list_Of_Nodes.get(id2) is not None and weight >= 0:
                if not self.list_of_Edge_Src.get(id1).__contains__(id2) \
                        and not self.list_of_Edge_Dest.get(id2).__contains__(id1):
                    self.list_of_Edge_Src[id1][id2] = weight
                    self.list_of_Edge_Dest[id2][id1] = weight
                    edge_tmp = EdgeData(id1, id2, weight)
                    self.list_of_Edges[(id1, id2)] = edge_tmp
                    self.mC += 1
                    self.size_Of_Edge += 1
                    return True
                else:
                    self.list_of_Edge_Src[id1][id2] = weight
                    self.list_of_Edge_Dest[id2][id1] = weight
                    self.mC += 1
                    return True
        return False

    """
    Adds a node to the graph.
    """

    def add_node(self, node_id: int, pos: tuple) -> bool:
        if self.list_Of_Nodes.get(node_id) is None:
            self.list_Of_Nodes[node_id] = NodeData(node_id, "", 0.0, pos, 0.0)
            self.list_of_Edge_Src[node_id] = dict()
            self.list_of_Edge_Dest[node_id] = dict()
            self.mC += 1
            return True
        return False

    """
    Removes a node from the graph.
    """

    def remove_node(self, node_id: int) -> bool:
        if not self.list_Of_Nodes.get(node_id) is None:
            if self.list_of_Edge_Src.__contains__(node_id):
                src_tmp_list = [] = self.list_of_Edge_Src[node_id]
                for key in src_tmp_list:
                    if self.list_of_Edge_Dest[key].__contains__(node_id):
                        del self.list_of_Edge_Dest[key][node_id]
            if self.list_of_Edge_Dest.__contains__(node_id):
                dest_tmp_list = [] = self.list_of_Edge_Src[node_id]
                for key in dest_tmp_list:
                    if self.list_of_Edge_Src[key].__contains__(node_id):
                        del self.list_of_Edge_Src[key][node_id]
            del self.list_Of_Nodes[node_id]
            return True
        return False

    """
    Removes an edge from the graph.
    """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.list_Of_Nodes.get(node_id1) is not None:
            if self.list_Of_Nodes.get(node_id2) is not None:
                if self.list_of_Edge_Src.get(node_id1).__contains__(node_id2):
                    if self.list_of_Edge_Dest.get(node_id2).__contains__(node_id1):
                        del self.list_of_Edge_Src[node_id1][node_id2]
                        del self.list_of_Edge_Dest[node_id2][node_id1]
                        self.size_Of_Edge -= 1
                        return True
        return False
