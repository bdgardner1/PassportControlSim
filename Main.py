import random
import operator
import matplotlib.pyplot as pyt
import matplotlib.animation as ani
import Passenger_Model
import csv
#Adds criteria for my environment and defines the number of agents (sheep) and sheep dogs
environment = []
num_pass = 20
passengers = []
num_iter = 250
f = open('EnvTest.txt', newline='') 
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
fig = pyt.figure(figsize=(7,7))
pyt.xlim(0, 300)
pyt.ylim(0, 300)
ax = fig.add_axes([0,0,1,1])

for i in range(num_pass):
    passengers.append(Passenger_Model.Passenger(environment, passengers))

for j in range(num_iter):
    
    def update(frame_number):
        fig.clear()
        
        for i in range(num_pass):
            random.shuffle(passengers[i].passengers)
            passengers[i].move()
            
        for i in range(num_pass):
            
            pyt.scatter(passengers[i].x,passengers[i].y, color = 'red')
            pyt.xlim(0,300)
            pyt.ylim(0,300)
            pyt.imshow(environment)
          

animation = ani.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_iter)

pyt.pyplot.show()



#Writes new environment data to file


