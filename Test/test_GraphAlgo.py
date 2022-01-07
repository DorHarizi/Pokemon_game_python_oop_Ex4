import copy
import time
import unittest
from math import inf
from unittest import TestCase
# from src.DiGraph import DiGraph
# from src.GraphAlgo import GraphAlgo

from My_Graph.DiGraph import DiGraph
from My_Graph.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
            g1_algo = GraphAlgo()
            g1_algo.load_from_json("../data/A1.json")

            A0 = g1_algo.get_graph()

            self.assertEqual(A0, g1_algo.get_graph())



    def test_shortest_path(self):
        g1_algo = GraphAlgo()
        g1_algo.load_from_json("../data/A0.json")
        A0=(4.3086815935816, [0, 1, 2, 3])
        A1_not=(inf, [])
        A1_0_4= 5.350731924801653, [0, 1, 2, 3, 4]

        self.assertTupleEqual(A0, g1_algo.shortest_path(0,3))
        # self.assertTupleEqual(A1_not, g1_algo.shortest_path(3,5))
        # self.assertTupleEqual(A1_0_4, g1_algo.shortest_path(0,4))


    def test_tsp(self):

        g1_algo = GraphAlgo()
        g1_algo.load_from_json("../data/A1.json")
        A1=([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16], 9.223372036854776e+18)

        self.assertTupleEqual(A1,g1_algo.TSPT(g1_algo.graph.get_all_v()))

        #
        # self.fail()

    def test_center_point(self):
        g1_algo = GraphAlgo()
        g1_algo.load_from_json("../data/A0.json")
        g5_algo = GraphAlgo()
        g5_algo.load_from_json("../data/A5.json")
        A0 = (7, 6.806805834715163)
        A1 = 8, 9.925289024973141
        A2 = 0, 7.819910602212574
        A3 = 2, 8.182236568942237
        A4 = 6, 8.071366078651435
        A5 = 40, 9.291743173960954
        self.assertTupleEqual(A0 , g1_algo.centerPoint())
        self.assertTupleEqual(A5 , g5_algo.centerPoint())
        # self.assertTupleEqual(A3 , g1_algo.centerPoint())
        # self.assertTupleEqual(A4 , g1_algo.centerPoint())
        # self.assertTupleEqual(A5 , g1_algo.centerPoint())

        # self.fail()


