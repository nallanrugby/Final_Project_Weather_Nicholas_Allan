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
	'''add comment'''
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

	#call stats test 
	a = spearman_test(data['Wind_direction'], data['Temperature'])

	b = spearman_test(data['Wind_speed'], data['Temperature'])

	c = spearman_test(data['Gust_speed'], data['Temperature'])

	d = spearman_test(data['Relative_humidity'], data['Temperature'])

	e = spearman_test(data['Rainfall'], data['Temperature'])
	
	stats_dataframe = pd.DataFrame({'formula':['Temperature vs Rainfall' ,'Temperature vs Relative Humidity', 'Temperature vs Gust Speed', 'Temperature vs Wind Speed','Temperature vs Wind Direction'], 'pvalue':[e[0], d[0], c[0],b[0], a[0]], 'rho':[e[1],d[1], c[1],b[1],a[1]]})
	
	stats_dataframe.to_csv('../results_figures/tables/'+ output_file +'_' + 'Temperature_vs_Variables '+'.csv')
	
def spearman_test(stat_data, x_value):
    
    #run test
    answer =scipy.stats.spearmanr(x_value , stat_data) 
    pvalue = answer[1]
    rho = answer[0]
    return pvalue, rho
    

	
main()