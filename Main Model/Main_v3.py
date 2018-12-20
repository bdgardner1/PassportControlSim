import random
import matplotlib.pyplot as pyt
import matplotlib.animation as ani
import Passenger_Model_v3
import csv
#Adds criteria for my environment and defines the number of agents (sheep) and sheep dogs
environment = []

num_pass_text = input("Enter No. of Passengers (Max 75):")
num_pass = int(num_pass_text)
while num_pass > 75:
    num_pass_text = input("Incorrect Entry. Please enter a number up to 75:")
    num_pass = int(num_pass_text)
num_cleared = 0
passengers = []
environment = []
gate_queue = [0,0,0,0,0]

num_iter = 1000
f = open('EnvTestv3.txt', newline='') 
#Import existing environment data as csv and create list
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:				# A list of rows
    newrow = []
    for value in row: 
        newrow.append(value)
    environment.append(newrow)

  
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
#Create plot
clear_file = open('gate clear times.txt','w+')
clear_file.write("")
clear_file.close() 

fig = pyt.figure(figsize=(7,7))
pyt.xlim(0, 215)
pyt.ylim(0, 175)
ax = fig.add_axes([0,0,1,1])


for i in range(num_pass):
    passengers.append(Passenger_Model_v3.Passenger(environment, num_cleared, passengers, gate_queue, ))

for j in range(num_iter):
    
    def update(frame_number):
        fig.clear()
        
        for i in range(num_pass):
            random.shuffle(passengers[i].passengers)
            passengers[i].action()
            passengers[i].timer()

            
            
        for i in range(num_pass):
            global num_cleared
            pyt.scatter(passengers[i].x,passengers[i].y, color = 'red')
            pyt.xlim(0,215)
            pyt.ylim(0,175)
            pyt.text(100, 163,"Passport Control")
            pyt.text(10, 115, "Luggage Collection")
            pyt.text(80,20,"1")
            pyt.text(107,20,"2")
            pyt.text(134,20,"3")
            pyt.text(161,20,"4")
            pyt.text(188,20,"5")
            pyt.text(130, 12, "Gates")
            pyt.imshow(environment)

       
animation = ani.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_iter)

pyt.show()

print(num_cleared)   



#Writes new environment data to file


