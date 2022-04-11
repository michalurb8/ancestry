from typing import List
from Node import Node
from random import randint

class Family:
    def __init__(self, N):
        self.currSize = 0
        self.N = N
        self.firstGen = [Node(None) for _ in range(N)]

    def populate(self, genCount: int, sigma: int, color = "111"):
        assert color == '0' or len(color) == 3, "Wrong color choice"
        for child in self.firstGen:
            child.children = []
        self.currSize = 0
        if color=='0':
            for parent in self.firstGen:
                parent.randomize()
        else:
            r, g, b = color[0]=='1', color[1]=='1', color[2]=='1'
            self.setRGB(self.firstGen, r, g, b)
        currGen = []
        prevGen = self.firstGen
        for i in range(genCount - 1):
            print(str(i/genCount)[:4], end='\r')
            currGen = []
            for _ in range(self.N):
                index = randint(0, self.N-1)
                new = Node(prevGen[index])
                new.mutate(sigma)
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

    def setRGB(self, generation: List, useRed: bool = True, useGreen: bool = False, useBlue: bool = False) -> None:
        for index, node in enumerate(generation):
            col = int(255*index/self.N)
            node.color = ((col if useRed else 0, col if useGreen else 0, col if useBlue else 0))
