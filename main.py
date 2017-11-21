import math
import pygame

import joy

class Main:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 450
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))

        self.objects = []

    def setupGame(self):
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.joy = joy.Joystick()

        self.objects.append(self.joy)

    def runGame(self):
        self.gameRunning = 1

        while self.gameRunning:
            self.getInput()
            self.compute()
            self.draw()
            self.clock.tick(self.FPS)

            leftX = pygame.joystick.Joystick(0).get_axis(0)
            leftY = -1 * pygame.joystick.Joystick(0).get_axis(1)
            rightX = pygame.joystick.Joystick(1).get_axis(2)
            rightY = -1 * pygame.joystick.Joystick(1).get_axis(3)

            #handle buttons 
            for event in pygame.event.get(pygame.JOYBUTTONUP): #event handling loop
                #handle mode switching - buttons 8/9 on both sticks
                print(event)
                if (event.button == 7): #button 8 increases mode
                    if (self.mode == 3):
                        self.mode = 1
                    else:
                        self.mode = self.mode + 1
                    print("Mode is now: " + str(self.mode))
                if (event.button == 8): #button 9 decreases mode
                    if (self.mode == 1):
                        self.mode = 3
                    else:
                        self.mode = self.mode - 1
                    print("Mode is now: " + str(self.mode))


    def getInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameRunning = 0

        
        pygame.display.set_caption(str(self.joy.x) + ', ' + str(self.joy.y) + ', ' + str(self.joy.rad))

    def draw(self):
        self.screen.fill((255,255,255))

        for o in self.objects:
            o.draw(self.screen)

        pygame.display.flip()

    def compute(self):
        i = 0
        while i < len(self.objects):
            self.objects[i].compute()
            i += 1



m = Main()
m.setupGame()
m.runGame()

pygame.quit()
