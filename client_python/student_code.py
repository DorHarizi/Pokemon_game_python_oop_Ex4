from types import SimpleNamespace
from My_Graph.EdgeData import EdgeData
from My_Graph.NodeData import NodeData
from client_python.agentData import agentData
from client_python.pokemonData import pokemonData
from client_python import gameData
from client import Client
from pygame import gfxdraw
from pygame import *
import random
import pygame
import json


class Button:
    def __init__(self, rect: pygame.Rect, text: str, color, func=None):
        self.rect = rect
        self.text = text
        self.color = color
        self.func = func
        self.is_pressed = False

    def press(self):
        self.is_pressed = not self.is_pressed


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


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Blue = (2, 55, 55)

# init pygame
WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
pygame.init()

screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
fontTime = pygame.font.SysFont('Arial', 20)

client = Client()
client.start_connection(HOST, PORT)

pokemons = client.get_pokemons()
pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))

# load the json string into SimpleNamespace Object
graph_json = client.get_graph()
graph = json.loads(
    graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

# create the object game
myGame = gameData.gameData()

# get the graph of the game
# Referral to our function load for Graph object
myGame.graphAlgo.load_from_json(graph_json)

# Referral to our function load for Pokemon object
myGame.loadPockemonsGame(pokemons)

# get all the Agents
strInfo = client.get_info()
info_json = json.loads(strInfo)
# Referral to our function load for Agents object
myGame.loadInfoGame(info_json)

for n in graph.Nodes:
    x, y, _ = n.pos.split(',')
    n.pos = SimpleNamespace(x=float(x), y=float(y))

# get data proportions
min_x = min(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
min_y = min(list(graph.Nodes), key=lambda n: n.pos.y).pos.y
max_x = max(list(graph.Nodes), key=lambda n: n.pos.x).pos.x
max_y = max(list(graph.Nodes), key=lambda n: n.pos.y).pos.y


# get the scaled data with proportions min_data, max_data
# relative to min and max screen dimentions
def scale(data, min_screen, max_screen, min_data, max_data):
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


# decorate scale with the correct values
def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


def highestPoint(destIndex:int) -> int:
    listTmp = myGame.graphAlgo.graph.all_out_edges_of_node(destIndex)
    listKeyTmp = listTmp.keys()
    maxhighest = -float('inf')
    tmpIndex = 0
    for num in listKeyTmp:
        pos = NodeData.get_pos(myGame.graphAlgo.graph.get_node(num))
        if maxhighest < pos[1]:
            maxhighest = pos[1]
            tmpIndex = num
    return tmpIndex


def lowestPoint(destIndex:int) -> int:
    listTmp = myGame.graphAlgo.graph.all_in_edges_of_node(destIndex)
    listKeyTmp = listTmp.keys()
    minlowest = float('inf')
    tmpIndex = 0
    for num in listKeyTmp:
        pos = NodeData.get_pos(myGame.graphAlgo.graph.get_node(num))
        if minlowest > pos[1]:
            minlowest = pos[1]
            tmpIndex = num
    return tmpIndex


def checkPos(pokemonTmp: pokemonData) -> int:
    for currentEdge in myGame.graphAlgo.graph.list_of_Edges.values():
        destNode = myGame.graphAlgo.graph.list_Of_Nodes.get(EdgeData.get_dest(currentEdge))
        srcNode = myGame.graphAlgo.graph.list_Of_Nodes.get(EdgeData.get_src(currentEdge))
        pos = pokemonData.get_pos(pokemonTmp)
        xSrc = NodeData.get_pos(srcNode)[0]
        ySrc = NodeData.get_pos(srcNode)[1]
        xDest = NodeData.get_pos(destNode)[0]
        yDest = NodeData.get_pos(destNode)[1]
        keyDest = NodeData.get_key(destNode)
        keySrc = NodeData.get_key(srcNode)

        num1 = (xSrc - xDest) ** 2
        num2 = (ySrc - yDest) ** 2
        disRoot = (num1 + num2) ** 0.5

        num1Check1 = (xSrc - pos[0]) ** 2
        num2Check1 = (ySrc - pos[1]) ** 2
        disRootCheck1 = (num1Check1 + num2Check1) ** 0.5

        num1Check2 = (pos[0] - xDest) ** 2
        num2Check2 = (pos[1] - yDest) ** 2
        disRootCheck2 = (num1Check2 + num2Check2) ** 0.5

        if xSrc == pos[0] and ySrc == pos[1]:
            return keySrc

        if xDest == pos[0] and yDest == pos[1]:
            return keyDest

        if pokemonData.get_type(pokemonTmp) > 0:
            if disRootCheck2 + disRootCheck1 == disRoot:
                tmp = min(disRootCheck1, disRootCheck2)
                if tmp == disRootCheck1:
                    return keySrc
                if tmp == disRootCheck2:
                    result = highestPoint(keyDest)
                    return result

        if pokemonData.get_type(pokemonTmp) < 0:
            if disRootCheck2 + disRootCheck1 == disRoot:
                tmp = min(disRootCheck1, disRootCheck2)
                if tmp == disRootCheck1:
                    result = lowestPoint(keySrc)
                    return result
                if tmp == disRootCheck2:
                    return keyDest
    return random.choice(range(len(myGame.graphAlgo.graph.list_Of_Nodes)))


radius = 15

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

# this command starts the server - the game is running now
client.start()
# from this point the game start
tmpMin = 0
tmpSec = 0

# create button stop
button = Button(pygame.Rect((50, 20), (150, 50)), "Stop", (255, 255, 0))

while client.is_running() == 'true':

    minGame = int(float(client.time_to_end()) / 1000) / 60
    secGame = int(float(client.time_to_end()) / 1000) % 60

    # update button pash
    button.func = pause
    pygame.draw.rect(screen, button.color, button.rect)
    if button.is_pressed:
        button_text = FONT.render(button.text, True, (0, 250, 250))
    else:
        button_text = FONT.render(button.text, True, (0, 0, 0))
    screen.blit(button_text, (button.rect.x + 37, button.rect.y))

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(event.pos):
                button.press()
                if button.is_pressed:
                    client.stop_connection()
                    on_click(button.func)

    pokemons = json.loads(client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    pokemons = [p.Pokemon for p in pokemons]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))
    agents = json.loads(client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = [agent.Agent for agent in agents]
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=my_scale(float(x), x=True), y=my_scale(float(y), y=True))

        # load all the current list pf Pokémons
        count = myGame.sizePokemons
        myGame.loadPockemonsGame(client.get_pokemons())

        # load all the current list pf Agents
        myGame.loadAgentsGame(client.get_agents())
        # create all the rout list for every agent
        if count != myGame.sizeAgents:
            myGame.routAgents[count + 1] = []
            count = count + 1

    # refresh surface
    screen.fill(Color(0, 0, 0))

    # draw nodes
    for n in graph.Nodes:
        x = my_scale(n.pos.x, x=True)
        y = my_scale(n.pos.y, y=True)

        # It's just to get a nice antialiasing circle
        gfxdraw.filled_circle(screen, int(x), int(y), radius, Color(64, 80, 174))
        gfxdraw.aacircle(screen, int(x), int(y), radius, Color(255, 255, 255))

        # draw the node id
        id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(x, y))
        screen.blit(id_srf, rect)

    # draw edges
    for e in graph.Edges:
        # find the edge nodes
        src = next(n for n in graph.Nodes if n.id == e.src)
        dest = next(n for n in graph.Nodes if n.id == e.dest)

        # scaled positions
        src_x = my_scale(src.pos.x, x=True)
        src_y = my_scale(src.pos.y, y=True)
        dest_x = my_scale(dest.pos.x, x=True)
        dest_y = my_scale(dest.pos.y, y=True)

        # draw the line
        pygame.draw.line(screen, WHITE, (src_x, src_y), (dest_x, dest_y))

    # draw agents
    for agent in agents:
        pygame.draw.circle(screen, Color(122, 61, 23), (int(agent.pos.x), int(agent.pos.y)), 10)

    # draw pokemons
    for p in pokemons:
        if int(p.type) > 0:
            pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)
        else:
            pygame.draw.circle(screen, Color(2, 55, 55), (int(p.pos.x), int(p.pos.y)), 10)

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

    # update screen changes
    display.update()

    # refresh rate
    clock.tick(60)

    # choose next edge
    for agent in myGame.list_of_agent.values():
        idTmp = agentData.get_id(agent)
        for pokemonIndex in myGame.list_of_pokemon.keys():
            if myGame.tagPokemons[pokemonIndex] == 0:
                pokemonNow = myGame.list_of_pokemon.get(pokemonIndex)
                if len(myGame.routAgents[idTmp]) == 0:
                    destAgent = checkPos(pokemonNow)
                    if destAgent != -1:
                        listRoute = myGame.graphAlgo.shortest_path(agentData.get_src(agent), destAgent)[1]
                        if len(listRoute) != 0:
                            myGame.routAgents[idTmp] = listRoute
                            listTmp = myGame.routAgents[idTmp]
                            agentData.set_dest(agent, listTmp[0])
                            agent.pokemon = pokemonNow
                            myGame.tagPokemons[pokemonIndex] = 1
                            next_node_id = listTmp[0]
                            listTmp.pop(0)
                            myGame.routAgents[idTmp] = listTmp
                            client.choose_next_edge(
                                '{"agent_id":' + str(idTmp) + ', "next_node_id":' + str(next_node_id) + '}')
                else:
                    if agent.pokemon == pokemonNow:
                        listTmp = myGame.routAgents[idTmp]
                        destAgent = listTmp[0]
                        agentData.set_src(agent, agentData.get_dest(agent))
                        indexDest = listTmp[len(listTmp) - 1]
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
            ttl = client.time_to_end()
            print(ttl, client.get_info())

    client.move()
# game over:
