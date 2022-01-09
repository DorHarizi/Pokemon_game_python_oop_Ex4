import pygame
import os
from graph3 import *
from algo import *
from pygame.constants import RESIZABLE
import math
pygame.font.init()
FONT=pygame.font.SysFont('comicsans',35)

screen=pygame.display.set_mode((800,600))
def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen
min_x=min_y=max_x=max_y=0
def min_max(graph):
    global min_x,min_y,max_x,max_y
    min_x = min(list(graph.nodes.values()), key=lambda n: n.pos[0]).pos[0]
    min_y = min(list(graph.nodes.values()), key=lambda n: n.pos[1]).pos[1]
    max_x = max(list(graph.nodes.values()), key=lambda n: n.pos[0]).pos[0]
    max_y = max(list(graph.nodes.values()), key=lambda n: n.pos[1]).pos[1]
def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)

def arrow(start, end, d, h, color):
    """
    קרדיט לדביר על הפונקציה
    """

    dx =(end[0] - start[0])
    dy =(end[1] - start[1])
    D = (math.sqrt(dx * dx + dy * dy))
    xm =(D - d)
    xn =(xm)
    ym =(h)
    yn = -h
    sin = dy / D
    cos = dx / D
    x = xm * cos - ym * sin + start[0]
    ym = xm * sin + ym * cos + start[1]
    xm = x
    x = xn * cos - yn * sin + start[0]
    yn = xn * sin + yn * cos + start[1]
    xn = x
    points = [(end[0], end[1]), (int(xm), int(ym)), (int(xn), int(yn))]

    pygame.draw.line(screen, color, start, end, width=4)
    pygame.draw.polygon(screen, color, points)
class Button:
    def __init__(self,rect:pygame.Rect,text:str,color,func=None):
        self.rect=rect
        self.text=text
        self.color=color
        self.func=func
        self.is_pressed=False
    def press(self):
        self.is_pressed = not self.is_pressed
class NodeScreen:
    def __init__(self,rect:pygame.Rect,id):
        self.rect=rect
        self.id=id

button =Button(pygame.Rect((50,20),(150,50)),"Algo",(255,255,0))
result=[]
node_screens=[]
def on_click(func):
    global result
    result=func()
    print(result)

def draw(algo:Algo,src_=-1):
    if src_ !=-1:
        src_text=FONT.render(str(src_),True,(0,0,0))
        screen.blit(src_text, (300,20))
    pygame.draw.rect(screen,button.color,button.rect)
    if button.is_pressed:
        button_text=FONT.render(button.text,True,(0,250,250))
    else:
        button_text = FONT.render(button.text, True, (0, 0, 0))
    screen.blit(button_text,(button.rect.x+37,button.rect.y))
    for src in algo.graph.nodes.values():
        x=my_scale(src.pos[0],x=True)
        y = my_scale(src.pos[1], y=True)
        pygame.draw.circle(screen,(0,0,0),(x,y),radius=10)
        src_text = FONT.render(str(src.id), True, (0, 0, 250))
        screen.blit(src_text, (x,y))
        node_screens.append(NodeScreen(pygame.Rect((x,y),(20,20)),src.id))

        for dest in algo.graph.edges[src.id]:
            dest=algo.graph.nodes[dest]
            his_x=my_scale(dest.pos[0],x=True)
            his_y = my_scale(dest.pos[1], y=True)
            if (src.id,dest.id) in result:
                arrow((x,y), (his_x,his_y), 17, 7, color=(0,250,0))
            else:
                arrow((x, y), (his_x, his_y), 17, 7, color=(0, 0, 250))
            # pygame.draw.line(screen,(250,0,0),start_pos=(x,y),end_pos=(his_x,his_y),width=3)


def display(algo:Algo=None):
    button.func=algo.my_algo
    min_max(algo.graph)
    run=True
    src=-1
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    button.press()
                    if button.is_pressed:
                        on_click(button.func)
                    else:
                        result.clear()
                for n in node_screens:
                    if n.rect.collidepoint(event.pos):
                        src=n.id

        screen.fill((250,250,250))
        draw(algo,src)
        pygame.display.update()

if __name__ == '__main__':
    g=from_json("graph3.json")
    a=Algo()
    a.init_graph(g)
    display(a)
