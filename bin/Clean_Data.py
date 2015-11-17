#Nicholas Allan 2015-11-16

import sys
import pandas as pd

def main():
	#input variables 
	input_file = sys.argv[1]

	#load the data
	data= pd.read_csv(input_file, delimiter = ',')
	
	#rename data columns
	data.columns=[['Num_Test', 'Date_Time', 'Rainfall', 'Temperature', 'Relative_humidity', 'Wind_direction', 'Wind_speed', 'Gust_speed']]
	
	#make sure that Date Time column is seen as a value of datetime
	data['Date_Time']= pd.to_datetime(data['Date_Time'])
	
main()