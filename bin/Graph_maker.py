#Nicholas Allan 
#this document is where my graphs will be produced. 
# data used must but in order of number test, date_time of test, rainfall, temperature , relative humidity, wind direction, wind speed, wind gust.  

# loading libraries that help load or graph data
import sys
import pandas as pd
import numpy
import matplotlib.pyplot as plt



def main():


     
    #output variables
	output_file = sys.argv[2]
	
	#input variables 
	input_file = sys.argv[1]

	#load the data
	data = pd.read_csv(input_file, delimiter = ',')
	
	#rename data columns
	data.columns=[['Num_Test', 'Date_Time', 'Rainfall', 'Temperature', 'Relative_humidity', 'Wind_direction', 'Wind_speed', 'Gust_speed']]
	
	#make sure that Date Time column is seen as a value of datetime
	data['Date_Time']= pd.to_datetime(data['Date_Time'])

	#print data
	plot(data, output_file)


def plot(data, savename):

	for y in range(2,6):
	
	#plot any variable in data frame
		plt.plot(data['Date_Time'], data[y], marker='o', color='b', linestyle='')

    #add title
		plt.title(data[y])

    #add gridlines
		plt.grid(True)
		
    #add axis lables 
		plt.ylabel(data[y])	
		plt.xlabel ('Date Time')
    
		plt.show()
            
	#save the plot	
		plt.savefig(str(y) + "_" + savename)
        



main()


