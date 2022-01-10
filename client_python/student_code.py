import random
import sys

from My_Graph import DiGraph
from My_Graph.EdgeData import EdgeData
from My_Graph.NodeData import NodeData
from client_python.agentData import agentData
from client_python.infoGame import infoGame
from client_python.pokemonData import pokemonData
from client_python import gameData
import pygame
import json
from client import Client
from pygame import gfxdraw
from pygame import *
from math import dist


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Blue = (2,55,55)


class Button:
    def __init__(self, rect: pygame.Rect, text: str, color, func=None):
        self.rect = rect
        self.text = text
        self.color = color
        self.func = func
        self.is_pressed = False

    def press(self):
        self.is_pressed = not self.is_pressed


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
                    myGame.tagPokemons.append(0)
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
                    myGame.routAgents[myGame.sizeAgents] = []
                    myGame.sizeAgents = myGame.sizeAgents + 1
                else:
                    continue


def loadInfoGame(info_json):
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
                else:
                    continue






def checkPos(pokemonTmp: pokemonData) -> int:
    eps = 0.00000001

    for currentEdge in myGame.graphAlgo.graph.list_of_Edges.values():
        destNode = myGame.graphAlgo.graph.list_Of_Nodes.get(EdgeData.get_dest(currentEdge))
        srcNode = myGame.graphAlgo.graph.list_Of_Nodes.get(EdgeData.get_src(currentEdge))
        pos1 = pokemonData.get_pos(pokemonTmp)
        pos=(pos1[0],pos1[1])

        temp1 = NodeData.get_pos(srcNode)
        posSrc=(temp1[0],temp1[1])

        temp2 = NodeData.get_pos(destNode)
        posDest=(temp2[0],temp2[1])


        keyDest = NodeData.get_key(destNode)
        keySrc = NodeData.get_key(srcNode)

        disRoot = dist(posSrc , posDest)
        disRootCheck1 = dist(pos,posSrc)
        disRootCheck2 = dist(pos , posDest)

        if posSrc[0] == pos[0] and posSrc[1]== pos[1]:
            return keySrc

        if posDest[0] == pos[0] and posDest[1] == pos[1]:
            return keyDest

        if pokemonData.get_type(pokemonTmp) > 0:
            if abs((disRootCheck2 + disRootCheck1)-disRoot) <= eps:
                tmp = min(disRootCheck1, disRootCheck2)
                if tmp == disRootCheck1:
                    return keySrc

        if pokemonData.get_type(pokemonTmp) < 0:
            if abs((disRootCheck2 + disRootCheck1)-disRoot) <= eps:
                tmp = min(disRootCheck1, disRootCheck2)

                if tmp == disRootCheck2:
                    return keyDest





result = []
node_screens = []


def on_click(func):
    global result
    result = func()
    print(result)


def pause():
    loop = 1
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                loop = 0


# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
fontTime = pygame.font.SysFont('Arial', 20)

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

# get all the Pokémon
strPokemon = client.get_pokemons()
pokemon_json = json.loads(strPokemon)
# Referral to our function load for Pokemon object
loadPockemonsGame(pokemon_json)

# get all the Agents
strInfo = client.get_info()
info_json = json.loads(strInfo)
# Referral to our function load for Agents object
loadInfoGame(info_json)



back=pygame.image.load('pock.png')
back = pygame.transform.scale(back, (screen.get_width(), screen.get_width()))
screen.blit(back, (0, 0))

# send the agents in the beginning to the start pos that were the Pokemon's with the max value
numberOfAgents = myGame.info.get_agents()
for i in myGame.list_of_pokemon.values():
    if numberOfAgents > 0:
        startNodeId = checkPos(i)
        if startNodeId != -1:
            client.add_agent("{\"id\":%d}" % startNodeId)
            numberOfAgents = numberOfAgents - 1
    else:
        break

# size of circle in the graph
radius = 15

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
    pygame.draw.line(screen, Color(255, 200, 255), (x_src, y_src), (x_dest, y_dest))

# this command starts the server - the game is running now
client.start()
# from this point the game start
tmpMin = 0
tmpSec = 0

# button pash
button = Button(pygame.Rect((50, 20), (150, 50)), "Pause", (255, 255, 0))

# button pash
button.func = pause
pygame.draw.rect(screen, button.color, button.rect)
if button.is_pressed:
    button_text = FONT.render(button.text, True, (0, 250, 250))
else:
    button_text = FONT.render(button.text, True, (0, 0, 0))
screen.blit(button_text, (button.rect.x + 37, button.rect.y))



while client.is_running() == 'true':



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos):
                button.press()
                if button.is_pressed:
                    on_click(button.func)

    minGame = int(float(client.time_to_end()) / 1000) / 60
    secGame = int(float(client.time_to_end()) / 1000) % 60
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # load all the current list pf Pokémons
    pokemons = json.loads(client.get_pokemons())
    loadPockemonsGame(pokemons)

    # load all the current list pf Agents
    agents = json.loads(client.get_agents())
    loadAgentsGame(agents)

    # draw agents
    for currentAgent in myGame.list_of_agent.values():
        posAgentTmp = agentData.get_pos(currentAgent)
        x = my_scale(posAgentTmp[0], x=True)
        y = my_scale(posAgentTmp[1], y=True)
        pygame.draw.circle(screen, Color(100, 00, 23), (int(x), int(y)), 8)

    # # draw Pokemon
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
            id_srf = FONT.render("->", True, Color(100, 0, 0))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)


    if tmpMin != minGame and tmpSec != secGame:
        if tmpMin == 0 and tmpSec == 0:
            tmpMin = minGame
            tmpSec = secGame
        timer = '%d:%d' % (minGame, secGame)
        timer2 = '%d:%d' % (tmpMin, tmpSec)
        imageTimer = fontTime.render(timer, False, Color(0, 255, 255))
        rect = imageTimer.get_rect(center=(1030 - imageTimer.get_width(), imageTimer.get_width()))
        imageTimer2 = fontTime.render(timer2, False, Color(0, 0, 0))
        rectTmp2 = imageTimer2.get_rect(center=(1030 - imageTimer2.get_width(), imageTimer2.get_width()))
        pygame.draw.rect(screen, Color(0, 0, 0), rectTmp2)
        screen.blit(imageTimer2, rectTmp2)
        screen.blit(imageTimer, rect)
        if tmpMin != minGame and tmpSec != secGame:
            tmpMin = minGame
            tmpSec = secGame
        print(timer)
    display.update()
    # refresh rate
    clock.tick(60)

    # choose next edge

    for pokemonIndex in myGame.list_of_pokemon.keys():
        if myGame.tagPokemons[pokemonIndex] == 0:
            pokemonNow = myGame.list_of_pokemon.get(pokemonIndex)
            for agent in myGame.list_of_agent.values():
                idTmp = agentData.get_id(agent)
                if len(myGame.routAgents[idTmp]) == 0:
                    destAgent = checkPos(pokemonNow)
                    if destAgent != -1:
                        listRoute = myGame.graphAlgo.shortest_path(agentData.get_src(agent), destAgent)[1]
                        if len(listRoute) != 0:
                            myGame.routAgents[idTmp] = listRoute
                            listTmp = myGame.routAgents[idTmp]
                            agentData.set_dest(agent, listTmp[0])
                            myGame.tagPokemons[pokemonIndex] = 1
                            next_node_id = listTmp[0]
                            listTmp.pop(0)
                            myGame.routAgents[idTmp] = listTmp
                            client.choose_next_edge(
                               '{"agent_id":' + str(idTmp) + ', "next_node_id":' + str(next_node_id) + '}')
                    else:
                        continue
                else:
                    listTmp = myGame.routAgents[idTmp]
                    destAgent = listTmp[0]
                    agentData.set_src(agent, agentData.get_dest(agent))
                    indexDest = listTmp[len(listTmp)-1]
                    if indexDest != destAgent:
                        agentData.set_dest(agent, listTmp[0])
                        next_node_id = listTmp[0]
                        listTmp.pop(0)
                        myGame.routAgents[idTmp] = listTmp
                        client.choose_next_edge(
                            '{"agent_id":' + str(idTmp) + ', "next_node_id":' + str(next_node_id) + '}')
                    else:
                        agentData.set_dest(agent, listTmp[0])
                        next_node_id = listTmp[0]
                        listTmp.pop(0)
                        myGame.routAgents[idTmp] = listTmp
                        client.choose_next_edge(
                            '{"agent_id":' + str(idTmp) + ', "next_node_id":' + str(next_node_id) + '}')
        else:
            continue
        # ttl = client.time_to_end()
        # print(ttl, client.get_info())
    client.move()


# game over:


