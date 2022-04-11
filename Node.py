from random import randint
class Node:
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.color = self.parent.color if self.parent else (0,0,0)

    def addChild(self, child):
        self.children.append(child)

    def mutate(self, sigma):
        (r,g,b) = self.color
        r = max(0,min(255,(r + randint(-sigma, sigma))))
        g = max(0,min(255,(g + randint(-sigma, sigma))))
        b = max(0,min(255,(b + randint(-sigma, sigma))))
        self.color = (r,g,b)

    def randomize(self):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        self.color = (r,g,b)