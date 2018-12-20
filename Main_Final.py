import random
import matplotlib.pyplot as pyt
import matplotlib.animation as ani
import agentframework
import csv

#User inputs how many 'UK Only' queues they want
ukQno = int(input("Enter No. of UK Only Queues (0,1,2):"))
# checks for invalid input
while ukQno not in (0,1,2):
    ukQno = int(input("Invalid entry. Please type '0', '1' or '2':"))

# User inputs the number of passengers they want to model.
num_pass = int(input("Enter No. of Passengers (Max 75):"))
# checks for invalid input
while num_pass > 75:
    num_pass = int(input("Incorrect Entry. Please enter a number up to 75:"))
    
#User inputs chance of passenger being UK resident    
pr_UK = int(input("Enter percentage chance of UK passenger (1 - 98):"))
# checks for invalid input
while pr_UK > 98:
    pr_UK = int(input("Number must be 98 or lower. Please reenter:"))

#calculate max possible chance of being EU resident (assuming at least 1% chance of 'Other')    
maxEU = 99 - pr_UK  
 #User inputs chance of passenger being EU resident
pr_EU = int(input("Enter percentage chance of EU passenger (1 - " + str(maxEU) + "):"))
# checks for invalid input
while pr_EU > maxEU:
    pr_EU_text = input("Number must be " + str(maxEU) + " or lower. Please reenter:")
    pr_EU = int(pr_EU_text)

#converts to possibilty decimial and creates list
pr_UK = pr_UK/100
pr_EU = pr_EU/100
pass_ratio = [pr_UK, pr_EU]

#Creates required lists
environment = []
passengers = []
desk_queue = [0,0,0,0,0,0,0]    #the size of the queue for each desk

#Create queue label text and colour

if ukQno == 0:
    Q1_text = "UK & EU"
    Q1_col = "Green"
    Q2_text = "UK & EU"
    Q2_col = "Green"
elif ukQno == 1:
    Q1_text = "UK Only"
    Q1_col = "Blue"
    Q2_text = "UK & EU"
    Q2_col = "Green"
else:
    Q1_text = "UK Only"
    Q1_col = "Blue"
    Q2_text = "UK Only"
    Q2_col = "Blue" 

num_iter = 500

#Opens passport control environment file
f = open('Env_' + str(ukQno) + '.txt', newline='') 
#Import environment data as csv and creates list
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				
    newrow = []
    for value in row: 
        newrow.append(value)
    environment.append(newrow)

  
f.close() 	
		
#Creates a new file for passenger clear data to be added to later
clear_file = open('passenger clear times.txt','w+')
clear_file.write("")
clear_file.close() 

#Creates figure for use with pyplot
fig = pyt.figure(figsize=(7,7))
pyt.xlim(0, 215)
pyt.ylim(0, 175)
ax = fig.add_axes([0,0,1,1])

#creates passengers using passengers class. 
for i in range(num_pass):
    passengers.append(agentframework.Passenger(environment, passengers, desk_queue, pass_ratio ))

#Modelling process
for j in range(num_iter):       #runs model for specified number of 'turns'
    
    def update(frame_number):   #set update information for use in animation
        fig.clear()
        
        for i in range(num_pass):   # Each passenger performs the below actions
            random.shuffle(passengers[i].passengers) #randomise order of moves
            passengers[i].action()      
            passengers[i].timer()

            
            
        for i in range(num_pass):   #adds passengers and environment to plot
            pyt.scatter(passengers[i].x,passengers[i].y, color = 'red')
            pyt.xlim(0,215)
            pyt.ylim(0,175)
            pyt.text(25, 166,"Passport Control", color = "white")
            pyt.text(10, 115, "Luggage Collection")
            pyt.text(75,160,Q1_text, fontsize = 8, color = Q1_col)
            pyt.text(104,160,Q2_text, fontsize = 8, color = Q2_col)
            pyt.text(131,160,"UK & EU", fontsize = 8, color = "green")
            pyt.text(158,160,"ALL", fontsize = 8, color = "yellow")
            pyt.text(185,160,"ALL", fontsize = 8, color = "yellow")
            pyt.text(80,20,"1")
            pyt.text(107,20,"2")
            pyt.text(134,20,"3")
            pyt.text(161,20,"4")
            pyt.text(188,20,"5")

            pyt.text(130, 12, "Desks")
            pyt.imshow(environment)

# Animates the above model      
animation = ani.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_iter)

pyt.show() 



