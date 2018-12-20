# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:36:30 2018

@author: BenG
"""

import random


class Passenger():
    def __init__ (self, environment, num_cleared, passengers, gate_queue):
            
            self.speed = 2 + round(random.random()*2)
            self.ease = random.random()
            self.y = 154 - round(random.random()*5)
            self.x = 0
            self.environment = environment
            self.num_cleared = num_cleared
            self.gate_queue = gate_queue
            self.passengers = passengers
            self.status = "onplane"
            self.gate_choice = 6
            self.plane_wait = round(random.random()*5)
            self.time = 0 - self.plane_wait
            if self.ease < 0.5:
                self.wait_time = 10
            elif self.ease < 0.8:
                self.wait_time = 15 
            elif self.ease < 0.98:
                self.wait_time = 18
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
            if self.gate_choice == 4:
                self.queue_enter()
                return
            
            if self.gate_queue[self.gate_choice] > self.gate_queue[self.gate_choice + 1] + 1:
                self.x = self.x + self.speed
            else:
                self.queue_enter()
                              
         
    def queue(self):
        self.environment[self.y][self.x] +=1
        if self.queue_full() == False:
            self.y = self.y - 3
            if self.environment[self.y][self.x] == 50:
                self.y = 34
                self.status = "atdesk"

    def desk(self):   
        global clear_time     
        if self.wait_time > 0:    
           self.wait_time -= 1
        else: 
            self.status = "cleared"
            self.num_cleared += 1
            clear_value = [self.time,self.gate_choice + 1]
            clear_text = str(clear_value)
            clear_file = open("gate clear times.txt", "a+")
            clear_file.write(clear_text)
            clear_file.close()
            self.gate_queue[self.gate_choice] -= 1  
            self.y = 5 + (random.random()*100)
            self.x = 5 + (random.random() * 60)
   
    def queue_enter(self):
        
        self.y = self.y - self.speed
        if self.y < 128:
            self.status = "queuing"
            self.gate_queue[self.gate_choice] += 1
            self.x = 82 + self.gate_choice*27
    #This checks to see is there is another passenger within 2 steps of them
   
    def queue_full(self):
        blocked = False
        for passenger in self.passengers:
            if passenger.status == "cleared":
                next
            
            else:
                
                if self.gate_choice == passenger.gate_choice:
                    if passenger.status == "atdesk":
                        dist = 8
                    else:
                        dist = 4
                    if 0 < self.y - passenger.y < dist:
                        blocked = True
                else:
                    next
        return(blocked)
   
    def queue_select(self):

        if self.x < 86:
            return(0)
            
        elif self.x < 113:
            return(1)
            
        elif self.x < 140:
            return(2)
            
        elif self.x < 170:
            return(3)
            
        else:
            return(4)
    
    def timer(self):
        if self.status != "cleared":
            self.time += 1
            



    
        