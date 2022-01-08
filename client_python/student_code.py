import random
from My_Graph.EdgeData import EdgeData
from My_Graph.NodeData import NodeData
from client_python.agentData import agentData
from client_python.infoGame import infoGame
from client_python.pokemonData import pokemonData
from client_python import gameData
import time
import numpy as np
import pygame
import json
from client import Client
from pygame import gfxdraw
from pygame import *

# get the scaled data with proportions min_data, max_data
# relative to min and max screen dimentions
def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values
def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, myGame.graphAlgo.graph.xMin, myGame.graphAlgo.graph.xMax)
    if y:
        return scale(data, 50, screen.get_height() - 50, myGame.graphAlgo.graph.yMin, myGame.graphAlgo.graph.yMax)


def loadPockemonsGame(pokemons_json):
    if pokemons_json is not None:
        pokemons = pokemons_json["Pokemons"]
        for p in pokemons:
            if p["Pokemon"] is not None:
                valueTmp = float(p["Pokemon"]["value"])
                typeTmp = int(p["Pokemon"]["type"])
                pos = p["Pokemon"]["pos"]
                posTmp = tuple(float(s) for s in pos.split(","))
                pokemonTmp = pokemonData(valueTmp, typeTmp, posTmp)
                if myGame.list_of_pokemon.__contains__(pokemonTmp) is not True:
                    myGame.list_of_pokemon[myGame.sizePokemons] = pokemonTmp
                    myGame.sizePokemons = myGame.sizePokemons + 1
                else:
                    continue


def loadAgentsGame(agents_json):
    if agents_json is not None:
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
                if myGame.list_of_agent.__contains__(agentTmp) is not True:
                    myGame.list_of_agent[myGame.sizeAgents] = agentTmp
                    myGame.sizeAgents = myGame.sizeAgents + 1
                else:
                    continue


def loadInfoGame(info_json):
    if info_json is not None:
        info = info_json["GameServer"]
        if info is not None:
            pokemonsTmp = int(info["GameServer"]["pokemons"])
            if info["GameServer"]["is_logged_in"] == "True":
                is_logged_inTmp = bool(True)
            else:
                is_logged_inTmp = bool(False)
            movesTmp = int(info["GameServer"]["moves"])
            gradeTmp = int(info["GameServer"]["grade"])
            game_levelTmp = int(info["GameServer"]["game_level"])
            max_user_levelTmp = int(info["GameServer"]["max_user_level"])
            idTmp = int(info["GameServer"]["id"])
            agentsTmp = int(info["GameServer"]["agents"])
            infoTmp = infoGame(pokemonsTmp, is_logged_inTmp, movesTmp, gradeTmp, game_levelTmp,
                               max_user_levelTmp, idTmp, agentsTmp)
            myGame.info = infoTmp


def loadGraphGame(graph_json):
    if graph_json is not None:
        new_Vertices = graph_json["Nodes"]
        new_Edges = graph_json["Edges"]
        for v in new_Vertices:
            if v["id"] is not None:
                key = v["id"]
                pos = v["pos"]
                posTmp = tuple(float(s) for s in pos.strip("()").split(","))
                node = NodeData(key, "", 0.0, pos, 0.0)
                if myGame.graphAlgo.graph.list_Of_Nodes.__contains__(node) is not True:
                    myGame.graphAlgo.graph.add_node(key, posTmp)
                    if myGame.graphAlgo.graph.xMax < posTmp[0]:
                        myGame.graphAlgo.graph.xMax = posTmp[0]
                    if posTmp[0] < myGame.graphAlgo.graph.xMin:
                        myGame.graphAlgo.graph.xMin = posTmp[0]
                    if myGame.graphAlgo.graph.yMax < posTmp[1]:
                        myGame.graphAlgo.graph.yMax = posTmp[1]
                    if posTmp[1] < myGame.graphAlgo.graph.yMin:
                        myGame.graphAlgo.graph.yMin = posTmp[1]
                    else:
                        continue
        for v in new_Edges:
            if v["src"] is not None and v["dest"] is not None and v["w"] is not None:
                edge = EdgeData(int(v["src"]), int(v["dest"]), float(v["w"]))
                if myGame.graphAlgo.graph.list_of_Edges.__contains__(edge) is not True:
                    myGame.graphAlgo.graph.add_edge(int(v["src"]), int(v["dest"]), float(v["w"]))
                    myGame.averageWeight = myGame.averageWeight + float(v["w"])
                else:
                    continue


def checkPos(pos: tuple) -> int:
    for currenNode in myGame.graphAlgo.graph.list_Of_Nodes.values():
        currentPos = NodeData.get_pos(currenNode)
        eps = np.finfo(np.float32).eps
        if currentPos[0] - eps <= pos[0] <= currentPos[0] + eps:
            if currentPos[1] - eps <= pos[1] <= currentPos[1] + eps:
                return NodeData.get_key(currenNode)
    return -1


# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
HOST = '192.168.1.45'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)

client = Client()
# create the object game
myGame = gameData.gameData()
client.start_connection(HOST, PORT)

# get data proportions
# get the graph of the game
strGraph = client.get_graph()
graph_json = json.loads(strGraph)
# Referral to our function load for Graph object
loadGraphGame(graph_json)
# Check if the function loadGraphGame work
print(myGame.graphAlgo.graph.__repr__())

# get all the Pokémon
strPokemon = client.get_pokemons()
pokemon_json = json.loads(strPokemon)
# Referral to our function load for Pokemon object
loadPockemonsGame(pokemon_json)
# Check if the function loadPockemonsGame work
print(myGame.list_of_pokemon)

# # get all the Agents
# strinfo = client.get_info()
# info_json = json.loads(strinfo)
# # Referral to our function load for Agents object
# loadInfoGame(info_json)
# # Check if the function loadAgentsGame work
# print(myGame.info)

client.add_agent("{\"id\":0}")
# # send the agents in the beginning to the start pos
# numberOfAgents = myGame.info.get_agents()
# for i in range(numberOfAgents):
#     startNodeId = checkPos(agentData.get_pos(i))
#     if startNodeId != -1:
#         client.add_agent("{\"id\":startNodeId")
#     else:
#         num = random.choice(myGame.graphAlgo.graph.list_Of_Nodes)
#         client.add_agent("{\"id\":num")

# size of circle in the graph
radius = 15

# this command starts the server - the game is running now
client.start()

# from this point the game start
while client.is_running() == 'true':

    # load all the current list pf Pokémons
    pokemons = json.loads(client.get_pokemons())
    loadPockemonsGame(pokemons)

    # load all the current list pf Agents
    agents = json.loads(client.get_agents())
    loadAgentsGame(agents)

    # timer
    # def draw_text(text, font, text_col, x, y):
    #     imageTimer = font.render(text, True, text_col)
    #     xTmp = scale(x, 50, screen.get_width() - 50, myGame.graphAlgo.graph.xMin, myGame.graphAlgo.graph.xMax)
    #     yTmp = scale(y, 50, screen.get_height() - 50, myGame.graphAlgo.graph.yMin, myGame.graphAlgo.graph.yMax)
    #     screen.blit(imageTimer, (int(xTmp), int(yTmp)))

    minGame = int(float(client.time_to_end()) / 1000) / 60
    secGame = int(float(client.time_to_end()) / 1000) % 60
    timer = '%d:%d' % (minGame, secGame)
    # gfxdraw.filled_circle(screen, int(x), int(y), radius, Color(64, 80, 174))
    # gfxdraw.aacircle(screen, int(x), int(y), radius, Color(255, 255, 255))
    id_srf = FONT.render(str(timer), True, Color(255, 255, 255))
    rect = id_srf.get_rect(topright=(0, 0))
    screen.blit(id_srf, rect)
    print(timer)
    # draw_text(timer, FONT, Color(255, 255, 255), screen.get_width()-25, screen.get_height()-25)

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # refresh surface
    screen.fill(Color(0, 0, 0))

    # draw nodes
    for currentNode in myGame.graphAlgo.graph.list_Of_Nodes.values():
        posNodeTmp = NodeData.get_pos(currentNode)
        x = my_scale(posNodeTmp[0], x=True)
        y = my_scale(posNodeTmp[1], y=True)
        # It's just to get a nice antialiasing circle
        gfxdraw.filled_circle(screen, int(x), int(y), radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y), radius, Color(255, 255, 255))
        # draw the node id
        id_srf = FONT.render(str(NodeData.get_key(currentNode)), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for currentEdge in myGame.graphAlgo.graph.list_of_Edges.values():
        # find the edge nodes position
        src = EdgeData.get_src(currentEdge)
        dest = EdgeData.get_dest(currentEdge)
        srcNode = myGame.graphAlgo.graph.list_Of_Nodes.get(src)
        destNode = myGame.graphAlgo.graph.list_Of_Nodes.get(dest)
        srcPos = NodeData.get_pos(srcNode)
        destPos = NodeData.get_pos(destNode)
        x_src = my_scale(srcPos[0], x=True)
        y_src = my_scale(srcPos[1], y=True)
        x_dest = my_scale(destPos[0], x=True)
        y_dest = my_scale(destPos[1], y=True)
        # draw the line
        pygame.draw.line(screen, Color(255, 255, 255), (x_src, y_src), (x_dest, y_dest))

    # draw agents
    for currentAgent in myGame.list_of_agent.values():
        posAgentTmp = agentData.get_pos(currentAgent)
        x = my_scale(posAgentTmp[0], x=True)
        y = my_scale(posAgentTmp[1], y=True)
        pygame.draw.circle(screen, Color(122, 61, 23), (int(x), int(y)), 15)
    # draw Pokemon
    for currentPokemon in myGame.list_of_pokemon.values():
        posPokemonTmp = pokemonData.get_pos(currentPokemon)
        x = my_scale(posPokemonTmp[0], x=True)
        y = my_scale(posPokemonTmp[1], y=True)
        if pokemonData.get_type(currentPokemon) < 0:
            pygame.draw.circle(screen, Color(0, 255, 255), (int(x), int(y)), 15)
            id_srf = FONT.render("<-", True, Color(0, 0, 0))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)
        else:
            pygame.draw.circle(screen, Color(0, 255, 255), (int(x), int(y)), 15)
            id_srf = FONT.render("->", True, Color(0, 0, 0))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    for agent in myGame.list_of_agent.values():
        if agentData.get_dest(agent) == -1:
            next_node = (agentData.get_src(agent) - 1) % myGame.graphAlgo.graph.v_size()
            client.choose_next_edge(
                '{"agent_id":' + str(agentData.get_id(agent)) + ', "next_node_id":' + str(next_node) + '}')
            ttl = client.time_to_end()
            # print(ttl, client.get_info())
    # send the agent catch the Pokemon's
    client.move()
# game over:
