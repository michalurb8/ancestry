from Node import Node
from random import randint

class Family:
    def __init__(self, N):
        self.currSize = 0
        self.N = N
        self.firstGen = [Node(None) for _ in range(N)]

    def killChildren(self):
        for child in self.firstGen:
            child.children = []
        self.currSize = 0

    def populate(self, genCount):
        self.killChildren()
        self.setGray(self.firstGen)
        # for parent in self.firstGen:
        #     parent.randomize()
        currGen = []
        prevGen = self.firstGen
        for i in range(genCount - 1):
            print(i/genCount)
            currGen = []
            for _ in range(self.N):
                index = randint(0, self.N-1)
                new = Node(prevGen[index])
                prevGen[index].addChild(new)
                currGen.append(new)
            prevGen = currGen
        self.currSize = genCount

    def colorize(self, genCount):
        currGen = []
        prevGen = self.firstGen
        for _ in range(genCount - 1):
            currGen = []
            for _ in range(self.N):
                index = randint(0, self.N-1)
                new = Node(prevGen[index])
                prevGen[index].addChild(new)
                currGen.append(new)
            prevGen = currGen
        self.currSize = genCount

    def countNodes(self):
        nodes = 0
        for parent in self.firstGen:
            nodes += 1
            nodes += parent.countChildren()
        return nodes

    def countLeaves(self):
        leaves = 0
        for child in self.firstGen:
            leaves += child.countLeaves()
        return leaves

    def print(self):
        for parent in self.firstGen:
            parent.print(0)
    
    def setGray(self, generation):
        for index, node in enumerate(generation):
            g = int(255*index/self.N)
            node.color = ((g,g,g))
