# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:36:30 2018

@author: BenG
"""

import random


class Passenger():
    def __init__ (self, environment, passengers, gate_queue):
            self.speed = 1 + round(random.random()*4)
            self.ease = random.random()
            self.y = 169 - round(random.random()*5)
            self.x = 0
            self.environment = environment
            self.gate_queue = gate_queue
            self.passengers = passengers
            self.status = "onplane"
            self.gate_choice = 1
            self.plane_wait = round(random.random()*5)
            if self.ease < 0.5:
                self.wait_time = 10
            elif self.ease < 0.8:
                self.wait_time = 15 
            elif self.ease < 0.9:
                self.wait_time = 20
            else:
                self.wait_time = 30

    def action(self):
        if self.status == "onplane":
            if self.plane_wait == 0:
                self.status = "walking"  
                self.walk()
            else:
                self.plane_wait -= 1
        elif self.status == "walking":
            self.walk()
        elif self.status == "queuing":
            self.queue()
        elif self.status == "atdesk":
            self.desk()
        
            
            
    def walk(self):
        if self.environment[self.y][self.x] == 0:
             self.x = self.x + self.speed
        else:
            self.gate_choice = self.queue_select()
            if self.gate_choice == 5:
                self.queue_enter()
                return
            
            if self.gate_queue[self.gate_choice] > self.gate_queue[self.gate_choice + 1] + 1:
                self.x = self.x + self.speed
            else:
                self.queue_enter()
                
                
         
    def queue(self):
        
        if self.queue_full() == False:
            self.y = self.y - 3
            if self.environment[self.y][self.x] == 50:
                self.status = "atdesk"

    def desk(self):   
              
        if self.wait_time > 0:    
           self.wait_time -= 1
        else: 
            self.status = "cleared"
            self.gate_queue[self.gate_choice] -= 1
            self.y = 2 + (random.random()*135)
            self.x = 2 + (random.random() * 70)
   
    def queue_enter(self):
        self.y = self.y - self.speed
        if self.environment[self.y][self.x] == 0:
            self.status = "queuing"
            self.gate_queue[self.gate_choice] += 1
            self.x = 83 + self.gate_choice*27
    #This checks to see is there is another passenger within 2 steps of them
    def queue_full(self):
        blocked = False
        for passenger in self.passengers:
            if passenger.status == "cleared":
                next
            
            else:
                
                if self.gate_choice == passenger.gate_choice:
                    if passenger.status == "atdesk":
                        dist = 6
                    else:
                        dist = 4
                    if 0 < self.y - passenger.y < dist:
                        blocked = True
                else:
                    next
        return(blocked)
   
    def queue_select(self):

        if 78 < self.x < 85:
            return(0)
            
        elif 105 < self.x < 112:
            return(1)
            
        elif 132 < self.x < 139:
            return(2)
            
        elif 159 < self.x < 166:
            return(3)
            
        elif 186 < self.x < 193:
            return(4)
            
        else:
            return(5)
    

               
