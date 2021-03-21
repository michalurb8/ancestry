import pygame
from Family import Family

radius = 1
linewidth = 1
linecolor = (0,0,128)

N = 200
generations = 4000
resettime = int(generations / 10)

fam = Family(N)
fam.populate(generations)
pygame.init()
screen = pygame.display.set_mode((radius*generations,radius*N))
screen.fill((30,0,0))
DONE = False
DRAWN = False
while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True

    if(DRAWN):
        continue
    currGen = fam.firstGen
    for index, parent in enumerate(currGen):
        parentPos = (0, index*radius)
        pygame.draw.rect(screen, parent.color, (parentPos[0], parentPos[1], radius, radius))
    for gen in range(1, fam.currSize):
        SAMECOLOR = True
        nextGen = []
        childIndex = 0
        samplecolor = currGen[0].color
        for index,parent in enumerate(currGen):
            parentPos = (gen-1, + index)

            for child in parent.children:
                if(child.color != samplecolor):
                    SAMECOLOR = False
                childPos = (gen*radius, childIndex*radius)
                child.inherit()
#                pygame.draw.circle(screen, child.color, childPos, radius)
                pygame.draw.rect(screen, child.color, (childPos[0], childPos[1], radius, radius))
#                pygame.draw.line(screen, linecolor, parentPos, childPos, linewidth)
                childIndex += 1
                nextGen.append(child)
        currGen = nextGen
        if not SAMECOLOR:
            fam.setGray(nextGen)

    DRAWN = True


    pygame.display.flip()
