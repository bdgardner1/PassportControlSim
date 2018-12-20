# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:36:30 2018

@author: BenG
"""

import random

class Passenger():
    def __init__ (self, environment, passengers, gate_queue):
            self.speed = 1 + round(random.random()*3)
            self.ease = random.random()
            self.y = 180 - round(random.random()*10)
            self.x = 0
            self.environment = environment
            self.gate_queue = gate_queue
            self.passengers = passengers
            self.status = "onplane"
            self.gate_choice = 1
            self.plane_wait = round(random.random()*10)
            if self.ease < 0.5:
                self.wait_time = 2
            elif self.ease < 0.8:
                self.wait_time = 5 
            elif self.ease < 0.9:
                self.wait_time = 8
            else:
                self.wait_time = 12

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
            if self.gate_queue[self.gate_choice] > self.gate_queue[self.gate_choice + 1] + 2:
                self.x = self.x + self.speed
            else:
                self.y = self.y - self.speed
                
                if self.environment[self.y][self.x] == 0:
                        self.status = "queuing"
                        self.gate_queue[self.gate_choice] += 1  
         
    def queue(self):
        
        if self.queue_full() == False:
            self.y = self.y - self.speed
            if self.environment[self.y][self.x] == 50:
                self.status = "atdesk"

    def desk(self):   
              
        if self.wait_time > 0:    
           self.wait_time -= 1
        else: 
            self.y = 10
            self.status = "cleared"
            self.gate_queue[self.gate_choice] -= 1
   
    #This checks to see is there is another passenger within 2 steps of them
    def queue_full(self):
        blocked = False
        for passenger in self.passengers:
            if self.gate_choice == passenger.gate_choice:
                if passenger.status == "atdesk":
                    dist = 4
                else:
                    dist = 2
                if 0 < self.y - passenger.y < dist:
                    blocked = True
        return(blocked)
   
    def queue_select(self):
        
        if 24 < self.x < 33:
            return(0)
          
        elif 51 < self.x < 60:
            return(1)
            
        elif 78 < self.x < 87:
            return(2)
            
        elif 105 < self.x < 114:
            return(3)
            
        elif 132 < self.x < 141:
            return(4)
            
        elif 159 < self.x < 168:
            return(5)
            
        elif 186 < self.x < 195:
           return(6)
            
        else:
            return(7)
    

               
