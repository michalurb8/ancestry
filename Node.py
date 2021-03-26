from random import randint
class Node:
    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.color = (0,0,0)

    def addChild(self, child):
        self.children.append(child)

    def countLeaves(self):
        if len(self.children) == 0:
            return 1
        leaves = 0
        for child in self.children:
            leaves += child.countLeaves()
        return leaves

    def countChildren(self):
        children = 0
        for child in self.children:
            children += 1
            children += child.countChildren()
        return children

    def print(self, depth):
        for _ in range(depth):
            print("    ", end='')
        print(self.color)
        for child in self.children:
            child.print(depth + 1)
    
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
    
    def inherit(self):
        self.color = self.parent.color
