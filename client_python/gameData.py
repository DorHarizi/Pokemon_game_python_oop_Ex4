from My_Graph.DiGraph import DiGraph
from My_Graph.GraphAlgo import GraphAlgo
from client_python.infoGame import infoGame


class gameData:

    def __init__(self):
        self.list_of_agent = dict()
        self.sizeAgents = 0
        self.list_of_pokemon = dict()
        self.sizePokemons = 0
        self.info = infoGame()
        self.graphAlgo = GraphAlgo()
        self.averageWeight = 0.0

    """
    Return the game list_of_agent
    """

    def get_list_of_agent(self):
        return self.list_of_agent

    """
    Set the game list_of_agent 
    """

    def set_list_of_agent(self, list_of_agent):
        self.list_of_agent = list_of_agent

    """
    Return the game list_of_pokemon
    """

    def get_list_of_pokemon(self):
        return self.list_of_pokemon

    """
    Set game list_of_pokemon
    """

    def set_list_of_pokemon(self, list_of_pokemon):
        self.list_of_pokemon = list_of_pokemon

    """
    Return the game info
    """

    def get_info(self):
        return self.info

    """
    Set game info
    """

    def set_info(self, info):
        self.info = info

    """
    Return the game size of agents
    """

    def get_sizeAgents(self):
        return self.sizeAgents

    """
    Set game size of agents
    """

    def set_sizeAgents(self, sizeAgents):
        self.sizeAgents = sizeAgents

    """
    Return the game size of pokemons 
    """

    def get_sizePokemons(self):
        return self.sizePokemons

    """
    Set game size of pokemons 
    """

    def set_sizePokemons(self, sizePokemons):
        self.sizePokemons = sizePokemons


