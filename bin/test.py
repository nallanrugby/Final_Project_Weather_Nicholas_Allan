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
	
def plot(plot_data, savename):
        #plot data
	plt.plot(plot_data)
        #save the plot
	plt.savefig(savename)
        
main()