# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:36:30 2018

@author: BenG
"""

import random

class Passenger():
    def __init__ (self, environment, passengers):
            self.speed = 0.5 + (random.random() / 2)
            self.ease = random.random()
            self.y = 280 - round(random.random()*10)
            self.x = 1
            self.environment = environment
            self.passengers = passengers
            self.cleared = False
            if self.ease < 0.5:
                self.wait_time = 2
            elif self.ease < 0.8:
                self.wait_time = 5
            elif self.ease < 0.9:
                self.wait_time = 8
            else:
                self.wait_time = 12

    def move(self):
        if self.cleared == False:
            if self.y <= 50:
                if self.wait_time > 0:    
                    self.wait_time -= 1
                else: 
                    self.y = 10
                    self.cleared = True
            else:
            
                if self.x == 30:
                    self.queue = False
                    for passenger in self.passengers:
                        self.queue = self.check_queue(passenger)
                    if self.queue == False:
                        self.y = self.y - (self.speed * 4)
                        if self.y < 50:
                            self.y = 50
         
                else:
                   self.x = (self.x + (self.speed * 4))
                   if self.x > 30:
                       self.x = 30
             
   
    #This checks to see is there is another passenger within 2 steps of them
    def check_queue(self, passenger):
        if self.queue == False:
            if self.x != passenger.x:
                return(False)
            elif 0 < self.y - passenger.y <= 6:
                return(True)
            else:
                return(False)
                
        else:
            return(True)