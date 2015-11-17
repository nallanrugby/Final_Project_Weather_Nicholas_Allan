#Nicholas Allan 2015-11-16
#this document is where my statistics will preformed for this project. 
# data used must but in order of number test, date_time of test, rainfall, temperature , relative humidity, wind direction, wind speed, wind gust.  
# data must have delimiter of , for this program. 


# loading libraries that help load or graph data
import sys
import pandas as pd
import numpy

#import stats libraries
import statsmodels.api as sm 
import scipy

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
	
	spearman_test(data['Wind_direction'], data['Temperature'], output_file)

	spearman_test(data['Wind_speed'], data['Temperature'], output_file)

	spearman_test(data['Gust_speed'], data['Temperature'], output_file)

	spearman_test(data['Relative_humidity'], data['Temperature'], output_file)

	spearman_test(data['Rainfall'], data['Temperature'], output_file)
	
def spearman_test(stat_data, x_value,  savename):
    
    #run test
	scipy.stats.spearmanr(x_value , stat_data) 
	
main()