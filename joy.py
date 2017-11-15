import math
import pygame

import helpers

class Joystick_L:

    def __init__(self):
        pygame.joystick.init()
        numJoys = pygame.joystick.get_count()
        self.joyInitL = False
        if (numJoys > 0):
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.joyInitL = True
        else:
            print("No left joystick found")
            self.joyInitL = False
            return

        self.numButtons = self.joystick.get_numbuttons()
        self.buttons = [0]*self.numButtons
        self.x = 0
        self.y = 0
        self.rad = 0
     
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(),32)

    def compute(self):
        self.x = self.joystick.get_axis(0)
        self.y = self.joystick.get_axis(1)
        self.throttle = ((-1 * self.joystick.get_axis(2)) + 1) / 2
        self.rad = math.hypot(self.x,self.y)
        self.rad = helpers.limitToRange(self.rad,0,1)
        self.ang = math.atan2(self.y,self.x)
        self.x = self.rad*math.cos(self.ang)
        self.y = self.rad*math.sin(self.ang)
        #'clicks' to middle
        tab = .12
        if -tab < self.x < tab:
            self.x = 0
        if -tab < self.y < tab:
            self.y = 0

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
        pygame.draw.circle(surface,(0,255,255),(w/2,h/2),r,2)

class Joystick_R:

    def __init__(self):
        pygame.joystick.init()
        numJoys = pygame.joystick.get_count()
        self.joyInitR = False
        if (numJoys > 1):
            self.joystick = pygame.joystick.Joystick(1)
            self.joystick.init()
            self.joyInitR = True
        else:
            print("No right joystick found")
            self.joyInitR = False
            return

        self.numButtons = self.joystick.get_numbuttons()
        self.buttons = [0]*self.numButtons
        self.x = 0
        self.y = 0
        self.rad = 0
     
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(),32)

    def compute(self):
        self.x = self.joystick.get_axis(0)
        self.y = self.joystick.get_axis(1)
        self.throttle = ((-1 * self.joystick.get_axis(2)) + 1) / 2
        self.rad = math.hypot(self.x,self.y)
        self.rad = helpers.limitToRange(self.rad,0,1)
        self.ang = math.atan2(self.y,self.x)
        self.x = self.rad*math.cos(self.ang)
        self.y = self.rad*math.sin(self.ang)
        #'clicks' to middle
        tab = .12
        if -tab < self.x < tab:
            self.x = 0
        if -tab < self.y < tab:
            self.y = 0

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
            surface.blit(text,text.get_rect(centerx=w*(i+1)/(self.numButtons+1),centery=(h/2)-60)
        
        x = int(round(w/2+self.x*r))
        y = int(round(h/2+self.y*r))
        pygame.draw.aaline(surface,(128,0,0),(w/2,h/2),(x,y),1)
        pygame.draw.circle(surface,(0,0,0),(x,y),8,4)
        pygame.draw.circle(surface,(0,255,255),(w/2,h/2),r,2)