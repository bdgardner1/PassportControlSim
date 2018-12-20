# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:36:30 2018

@author: BenG
"""

import random
#main passenger class
class Passenger():
    def __init__ (self, environment, passengers, desk_queue, pass_ratio):
            
            self.speed = 2 + round(random.random()*2)   #sets passenger walking speed
            self.y = 154 - round(random.random()*5)     #sets passenger entry point
            self.x = 0
            self.environment = environment
            self.desk_queue = desk_queue
            self.passengers = passengers
            self.status = "waiting"         #Sets initial status as waiting to enter passport control
            self.desk_choice = None            
            self.plane_wait = round(random.random()*5)   #Creates random wait time to enter passport control
            self.desk_wait = round(random.random()*10)   #Creates random wait time at passport desk
            self.time = 0 - self.plane_wait        #creates a minus initial time to account for time spent on plane
            self.passenger_type(pass_ratio)    #Access function to set pasenger type

# Selects the passenger action dependent on status
    def action(self):
        if self.status == "waiting":    #Waiting to enter passport control
            if self.plane_wait == 0:
                self.status = "walking"  
                self.walk()
            else:
                self.plane_wait -= 1    #reduce wait time
        elif self.status == "walking":  #walking to queues
            self.walk()
        elif self.status == "queuing":  #queuing to enter desk
            self.queue()
        elif self.status == "atdesk":   #waiting at control desk
            self.desk()
        
            
            
    def walk(self):
        if self.environment[self.y][self.x]< self.ptype_no: #If not in a valid queue loading zone
             self.x = self.x + self.speed #walk towards queue loading zone
        else: 
            self.desk_choice = self.queue_select()  #run queue selection function
            if self.desk_choice == 4:   #if at the last desk queue
                self.queue_enter()      #run the enter desk queue function
                return
            
            if self.desk_queue[self.desk_choice] > self.desk_queue[self.desk_choice + 1]:   # compare current desk queue with the following
                self.x = self.x + self.speed #Continue walking if next queue is smaller
            else:
                self.queue_enter()  #run enter queue function
                              
         
    def queue(self): 
        self.environment[self.y][self.x] +=1 #Increases density count in queue
        if self.queue_full() == False:  #run funciton to check if someone is blocking from moving forward in queue
            self.y = self.y - 3 #moves down queue
            if self.environment[self.y][self.x] == 50: #checks if passenger has entered desk area
                self.y = 34 #passenger moves to front of desk
                self.status = "atdesk"#sets that passenger is at a desk

    def desk(self):   
        if self.desk_wait > 0:    #Checks if passenger still has to wait at desk
           self.desk_wait -= 1      #Reduces wait time by 1
        else: #passenger has cleared desk
            clear_text = str([self.time,self.desk_choice + 1,self.ptype]) #creates text value for data file
            clear_file = open("Passenger clear times.txt", "a+")    #Opens file in append mode and adds passenger clearance data
            clear_file.write(clear_text)
            clear_file.close()
            self.desk_queue[self.desk_choice] -= 1  #Reduces the queue size
            self.y = 5 + (random.random()*100)  #Randomly allocates them a waiting point in luggage collection
            self.x = 5 + (random.random() * 60)
            self.status = "cleared"     #Sets that the passenger has cleared passport control
    
    def passenger_type(self, pass_ratio): #Randomly allocates a passenger as 'UK', 'EU' or 'Other'
        self.ptype_no = random.random()
        
        if self.ptype_no < pass_ratio[0]: 
            self.ptype = "UK"
            self.ptype_no = 50
            self.desk_wait += 1
        elif self.ptype_no < (pass_ratio[0] + pass_ratio[1]): 
            self.ptype = "EU"
            self.ptype_no = 100
            self.desk_wait += 2
        else:
            self.ptype = "Other"
            self.ptype_no = 50
            self.ptype_no = 100
            self.desk_wait += 3
    
    
    
    def queue_select(self): #Determines the queue the passenger is assessing

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
        
    #passenger moves towards queue and enters once reaching a certain point
    def queue_enter(self): 
        
        self.y = self.y - self.speed
        if self.y < 128:    # Enters queue
            self.status = "queuing" #sets status as queuing
            self.desk_queue[self.desk_choice] += 1 #Increases desk queue size by 1
            self.x = 82 + self.desk_choice*27   #Centers the passenger in the queue
   
    #This checks to see is there is another passenger within 4 steps of them (8 if the passenger is at the desk)
    def queue_full(self):
        blocked = False
        for passenger in self.passengers: 
            if passenger.status == "cleared":   #Ignores passengers that have cleared
                next
            
            else:
                
                if self.desk_choice == passenger.desk_choice: #Checks if passenger is in the same queue
                    if passenger.status == "atdesk":
                        dist = 8
                    else:
                        dist = 4
                    if 0 < self.y - passenger.y < dist:
                        blocked = True
                else:
                    next
        return(blocked)
   

   # Adds 1 to passengers timer for each turn until they clear 
    def timer(self):
        if self.status != "cleared":
            self.time += 1
            



    
        