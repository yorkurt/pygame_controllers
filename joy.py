import math
import pygame

import helpers

class Joystick:
    def __init__(self):
        pygame.joystick.init()
        numJoys = pygame.joystick.get_count()
        joyI = input('There are ' + str(numJoys) + ' joysticks on the system. Input index for your joystick choice (starts at 0). ')
        self.joystick = pygame.joystick.Joystick(joyI)
        self.joystick.init()

        self.numButtons = self.joystick.get_numbuttons()
        self.buttons = [0]*self.numButtons

        self.x = 0
        self.y = 0
        self.rad = 0

        pygame.font.init()
        self.font = pygame.font.Font('CRYSRG__.TTF',32)

    def compute(self):
        self.x = self.joystick.get_axis(0)
        self.y = self.joystick.get_axis(1)
        self.x1 = self.joystick.get_axis(2)
        self.y1 = self.joystick.get_axis(3)
        self.rad = math.hypot(self.x,self.y)
        self.rad = helpers.limitToRange(self.rad,0,1)
        self.rad1 = math.hypot(self.x1,self.y1)
        self.rad1 = helpers.limitToRange(self.rad1,0,1)
        self.ang = math.atan2(self.y,self.x)
        self.ang1 = math.atan2(self.y1,self.x1)
        self.x = self.rad*math.cos(self.ang)
        self.y = self.rad*math.sin(self.ang)
        #'clicks' to middle
        tab = .12
        if -tab < self.x < tab:
            self.x = 0
        if -tab < self.y < tab:
            self.y = 0

        if -tab < self.x1 < tab:
            self.x1 = 0
        if -tab < self.y1 < tab:
            self.y1 = 0

        for i in xrange(self.numButtons):
            self.buttons[i] = self.joystick.get_button(i)

    def draw(self,surface):
        r = 200
        w = surface.get_width()
        h = surface.get_height()

        for i in xrange(self.numButtons):
            if self.buttons[i]:
                col = (0,255,0)
            else:
                col = (64,0,64)
            text = self.font.render(str(i),1,col)
            surface.blit(text,text.get_rect(centerx=w*(i+1)/(self.numButtons+1),centery=h/2))
        
        x = int(round(w/2+self.x*r))
        y = int(round(h/2+self.y*r))
        pygame.draw.aaline(surface,(128,128,128),(w/2,h/2),(x,y),1)
        pygame.draw.circle(surface,(0,0,0),(x,y),8,4)

        x1 = int(round(w/2+self.x1*r))
        y1 = int(round(h/2+self.y1*r))
        pygame.draw.aaline(surface,(128,0,128),(w/2,h/2),(x1,y1),1)
        pygame.draw.circle(surface,(0,128,0),(x1,y1),8,4)   

        pygame.draw.circle(surface,(0,255,255),(w/2,h/2),r,2)

        
            
        
        
