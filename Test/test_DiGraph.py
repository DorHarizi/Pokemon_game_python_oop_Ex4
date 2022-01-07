from random import uniform, randrange
from unittest import TestCase
# from networkx.generators.random_graphs import erdos_renyi_graph
from My_Graph.DiGraph import DiGraph as d

class TestDiGraph(TestCase):


    graph = d()
    for i in range(1000):
        x = uniform(0.0, 10.0)
        y = uniform(0.0, 10.00)
        z = 0.0
        pos = (x, y, z)
        graph.add_node(i, pos)
    for j in range (100):
        src = randrange(0, 101, 2)
        dest = randrange(0, 101, 2)
        w = uniform(0.0, 10.00)
        graph.add_edge(src, dest, w)


    def test_v_size(self):
        self.fail()

    def test_e_size(self):
        self.fail()

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()