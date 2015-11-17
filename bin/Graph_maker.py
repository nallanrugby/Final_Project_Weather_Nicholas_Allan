#Nicholas Allan 2015-11-16
#this document is where my graphs will be produced. 
# data used must but in order of number test, date_time of test, rainfall, temperature , relative humidity, wind direction, wind speed, wind gust.  

# loading libraries that help load or graph data
import sys
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import random


def main():


     
    #output variables
	output_file = sys.argv[2]
	
	#input variables 
	input_file = sys.argv[1]

	#load the data
	data= pd.read_csv(input_file, delimiter = ',')
	
	#rename data columns
	data.columns=[['Num_Test', 'Date_Time', 'Rainfall', 'Temperature', 'Relative_humidity', 'Wind_direction', 'Wind_speed', 'Gust_speed']]
	
	#make sure that Date Time column is seen as a value of datetime
	data['Date_Time']= pd.to_datetime(data['Date_Time'])

	#print plots
	#scatter plot vs time
	
	plot(data['Temperature'], data['Date_Time'], output_file)
	
	plot(data['Rainfall'], data['Date_Time'], output_file)
	
	plot(data['Relative_humidity'], data['Date_Time'], output_file)

	plot(data['Wind_direction'], data['Date_Time'], output_file)
	
	plot(data['Wind_speed'], data['Date_Time'], output_file)
	
	plot(data['Gust_speed'], data['Date_Time'], output_file)
	
	#scatter plot vs temperature

	plot(data['Wind_direction'], data['Temperature'], output_file)

	plot(data['Wind_speed'], data['Temperature'], output_file)

	plot(data['Gust_speed'], data['Temperature'], output_file)

	plot(data['Relative_humidity'], data['Temperature'], output_file)

	plot(data['Rainfall'], data['Temperature'], output_file)


def plot(plot_data, x_axis, savename):

	#produce random colors for graphs markers
	r = lambda: random.randint(0,255)
	
	#plot any variable in data frame
	plt.plot(x_axis, plot_data, marker='8', color='#%02X%02X%02X' % (r(),r(),r()), linestyle='')

    #add title
	plt.title(plot_data.name)

    #add gridlines
	plt.grid(True)
		
    #add axis lables 
	plt.ylabel(plot_data.name)	
	plt.xlabel (x_axis.name)
    
		#plt.show()
            
	#save the plot	
	plt.savefig(savename+ '_' + plot_data.name +'_'+ 'vs' +'_'+ x_axis.name + '.pdf')
    
	plt.close()
	#plt.clf()


main()


