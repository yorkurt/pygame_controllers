import math
import pygame

import joy

class Main:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 450
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))

        self.objects = []
        self.mode = 1

        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(),32)

    def setupGame(self):
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.joy = joy.Joystick_L()
        self.joy2 = joy.Joystick_R()

        self.objects.append(self.joy)
        self.objects.append(self.joy2)

    def runGame(self):
        self.gameRunning = 1

        while self.gameRunning:
            self.getInput()
            self.compute()
            self.draw(self.screen)
            self.clock.tick(self.FPS)
            leftX = pygame.joystick.Joystick(0).get_axis(0)
            leftY = -1 * pygame.joystick.Joystick(0).get_axis(1)
            #rightX = pygame.joystick.Joystick(1).get_axis(0)
            #rightY = -1 * pygame.joystick.Joystick(1).get_axis(1)

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

        #if(self.joy.joyInitL == True):
            pygame.display.set_caption(str(self.joy.x) + ', ' + str(self.joy.y) + ', ' + str(self.joy.rad) + ', ' + str(self.joy.throttle))

    def draw(self,surface):
        self.screen.fill((255,255,255))

        #for o in self.objects:
        #    o.draw(self.screen)

        
        r = 200
        w = surface.get_width()
        h = surface.get_height()

        for i in xrange(self.joy.numButtons):
            if self.joy.buttons[i]:
                col = (0,255,0)
            else:
                col = (64,0,64)
            
            text = self.font.render(str(i),1,col)
            surface.blit(text,text.get_rect(centerx=w*(i+1)/(self.joy.numButtons+1),centery=h/2-30))

        x = int(round(w/2+self.joy.x*r))
        y = int(round(h/2+self.joy.y*r))
        pygame.draw.aaline(surface,(128,128,128),(w/2,h/2),(x,y),1)
        pygame.draw.circle(surface,(0,0,0),(x,y),8,4)
        #pygame.draw.circle(surface,(0,255,255),(w/2,h/2),r,2)

        for i in xrange(self.joy2.numButtons):
            if self.joy2.buttons[i]:
                col = (0,255,0)
            else:
                col = (64,0,64)
            
            text = self.font.render(str(i),1,col)
            surface.blit(text,text.get_rect(centerx=w*(i+1)/(self.joy2.numButtons+1),centery=h/2+30))
        
        x1 = int(round(w/2+self.joy2.x*r))
        y1 = int(round(h/2+self.joy2.y*r))
        pygame.draw.aaline(surface,(128,0,0),(w/2,h/2),(x1,y1),1)
        pygame.draw.circle(surface,(0,0,0),(x1,y1),8,4)
        pygame.draw.circle(surface,(0,255,255),(w/2,h/2),r,2)

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
