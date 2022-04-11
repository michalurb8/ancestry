import pygame
import time
from Family import Family

def generate(N: int, generations: int, sigma: int, radius: int = 1, color: str = "111") -> None:
    assert color == '0' or len(color) == 3, "Wrong color choice"
    fam = Family(N)
    fam.populate(generations, sigma, color)
    pygame.init()
    screen = pygame.display.set_mode((radius*generations, radius*N))
    screen.fill((0,0,0))
    DONE = False
    DRAWN = False
    while not DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DONE = True
        if(DRAWN): continue
        
        currGen = fam.firstGen
        for index, parent in enumerate(currGen):
            parentPos = (0, index*radius)
            pygame.draw.rect(screen, parent.color, (parentPos[0], parentPos[1], radius, radius))
        for gen in range(1, fam.currSize):
            pygame.display.flip()
            nextGen = []
            childIndex = 0
            for index,parent in enumerate(currGen):
                parentPos = ((gen-1)*radius, + index*radius)

                for child in parent.children:
                    childPos = (gen*radius, childIndex*radius)
                    pygame.draw.rect(screen, child.color, (childPos[0], childPos[1], radius, radius))
                    childIndex += 1
                    nextGen.append(child)
            currGen = nextGen
        name = "output/result_" + str(time.time()) + ".png"
        pygame.image.save(screen, name)
        print("DONE")

        DRAWN = True


        pygame.display.flip()