import json
from operator import attrgetter
from My_Graph.GraphAlgo import GraphAlgo
from client_python.agentData import agentData
from client_python.infoGame import infoGame
from client_python.pokemonData import pokemonData


class gameData:
    def __init__(self):
        self.list_of_agent = dict()
        self.sizeAgents = 0
        self.list_of_pokemon = dict()
        self.sizePokemons = 0
        self.info = infoGame()
        self.graphAlgo = GraphAlgo()
        self.tagPokemons = []
        self.routAgents = dict()
        self.maxValue()

    def loadPockemonsGame(self, pokemons):
        if self.list_of_pokemon.values() is not None:
            self.list_of_pokemon.clear()
            self.sizePokemons = 0
        if pokemons is not None:
            pokemons_json = json.loads(pokemons)
            pokemons = pokemons_json["Pokemons"]
            for p in pokemons:
                if p["Pokemon"] is not None:
                    valueTmp = float(p["Pokemon"]["value"])
                    typeTmp = int(p["Pokemon"]["type"])
                    pos = p["Pokemon"]["pos"]
                    posTmp = tuple(float(s) for s in pos.split(","))
                    pokemonTmp = pokemonData(valueTmp, typeTmp, posTmp)
                    if self.list_of_pokemon.__contains__(pokemonTmp) is not True:
                        self.list_of_pokemon[self.sizePokemons] = pokemonTmp
                        self.tagPokemons.append(0)
                        self.sizePokemons = self.sizePokemons + 1
                    else:
                        continue
            self.maxValue()

    def loadAgentsGame(self, agents):
        if self.list_of_agent.values() is not None:
            self.list_of_agent.clear()
            self.sizeAgents = 0
        if agents is not None:
            agents_json = json.loads(agents)
            Agents = agents_json["Agents"]
            for a in Agents:
                if a["Agent"] is not None:
                    idTmp = int(a["Agent"]["id"])
                    valueTmp = float(a["Agent"]["value"])
                    srcTmp = int(a["Agent"]["src"])
                    destTmp = int(a["Agent"]["dest"])
                    speedTmp = float(a["Agent"]["speed"])
                    pos = a["Agent"]["pos"]
                    posTmp = tuple(float(s) for s in pos.split(","))
                    agentTmp = agentData(idTmp, valueTmp, srcTmp, destTmp, speedTmp, posTmp)
                    self.list_of_agent[self.sizeAgents] = agentTmp
                    self.sizeAgents = self.sizeAgents + 1
            self.funcAgent()

    def funcAgent(self):
        num = len(self.routAgents)
        tmp = self.sizeAgents - num
        if tmp > 0:
            tmp = tmp + num
            while num < tmp:
                self.routAgents[num] = []
                tmp = tmp - 1

    def loadInfoGame(self, info_json):
        if info_json is not None:
            info = info_json["GameServer"]
            if info is not None:
                pokemonsTmp = int(info["pokemons"])
                if info["is_logged_in"] == "True":
                    is_logged_inTmp = bool(True)
                else:
                    is_logged_inTmp = bool(False)
                movesTmp = int(info["moves"])
                gradeTmp = int(info["grade"])
                game_levelTmp = int(info["game_level"])
                max_user_levelTmp = int(info["max_user_level"])
                idTmp = int(info["id"])
                agentsTmp = int(info["agents"])
                infoTmp = infoGame(pokemonsTmp, is_logged_inTmp, movesTmp, gradeTmp, game_levelTmp,
                                   max_user_levelTmp, idTmp, agentsTmp)
                self.info = infoTmp

    def maxValue(self):
        listTmp = []
        for i in self.list_of_pokemon.values():
            listTmp.append(i)
        sorted(listTmp, key=attrgetter('value'), reverse=True)
        self.list_of_pokemon.clear()
        count = 0
        for p in listTmp:
            self.list_of_pokemon[count] = p
            count = count + 1

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


