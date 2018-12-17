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
            self.y = 180 - round(random.random()*10)
            self.x = 0
            self.environment = environment
            self.passengers = passengers
            self.cleared = False
            self.add_queue = False
            self.gate_choice = 1
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
            if self.y <= 36:
                if self.wait_time > 0:    
                    self.wait_time -= 1
                else: 
                    self.y = 0
                    self.cleared = True
            else:
                
                if self.gate_choice == 1:
                    if self.x == 30:
                        if self.add_queue == False:
                            self.environment[30][30] += 1
                            self.add_queue = True
                        else:
                            self.queue = False
                            for passenger in self.passengers:
                                self.queue = self.check_queue(passenger)
                            if self.queue == False:
                                self.y = self.y - (self.speed * 3)
                                if self.y < 36:
                                    self.y = 36
             
                    else:
                       self.x = (self.x + (self.speed * 3))
                       if self.x > 30:
                           self.x = 30
             
                elif self.gate_choice ==2:
                    if self.x == 60:
                        if self.add_queue == False:
                            self.environment[30][60] += 1
                            self.add_queue = True
                        else:                       
                            self.queue = False
                            for passenger in self.passengers:
                                self.queue = self.check_queue(passenger)
                            if self.queue == False:
                                self.y = self.y - (self.speed * 3)
                                if self.y < 36:
                                    self.y = 36
             
                    else:
                        self.x = (self.x + (self.speed * 3))
                        if self.x > 60:  
                            self.x = 60
                 
                elif self.gate_choice ==3:
                    if self.x == 90:
                        if self.add_queue == False:
                            self.environment[30][90] += 1
                            self.add_queue = True
                        else:
                            
                            self.queue = False
                            for passenger in self.passengers:
                                self.queue = self.check_queue(passenger)
                            if self.queue == False:
                                self.y = self.y - (self.speed * 3)
                                if self.y < 36:
                                    self.y = 36
             
                    else:
                        self.x = (self.x + (self.speed * 3))
                        if self.x > 90:  
                               self.x = 90
                else:
                    if self.x == 120:
                        if self.add_queue == False:
                            self.environment[30][120] += 1
                            self.add_queue = True
                        else:
                            self.queue = False
                            for passenger in self.passengers:
                                self.queue = self.check_queue(passenger)
                            if self.queue == False:
                                self.y = self.y - (self.speed * 3)
                                if self.y < 36:
                                    self.y = 36
                 
                    else:
                            self.x = (self.x + (self.speed * 3))
                            if self.x > 120:  
                                   self.x = 120
   
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
   
    def judge_queue(self, environment):
        
        if self.y >= 170:
            if self.environment[30][30] <= self.environment[30][60]:
                self.gate_choice = 1
            elif self.environment[30][60] <= self.environment[30][90]:
                self.gate_choice = 2
            elif self.environment[30][90] <= self.environment[30][120]:
                self.gate_choice = 3
            else:
                self.gate_choice = 4
            