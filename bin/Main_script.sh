# Nick Allan 2015-11-15
# This script will run my other scripts. 
# This script is case specific and will only work for my project.  
# Output files will be save in the results figure directory
# to run this script write in the command line write $bash Main_script.sh 

# this is the script that creates the graph functions. 
python Graph_maker.py ../data/QuestU_Remote_Weather_Station_oct312015.csv Weather_Project

#this is a python script tha creates a new dataframe that contains my statistical analysis
python Stats_maker.py ../data/QuestU_Remote_Weather_Station_oct312015.csv Weather_Project
