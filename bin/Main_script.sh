# Nick Allan 2015-11-15
# this script will run my other scripts. 
# variables to enter when running this scripts is input_file and output_file 
# input_file = data you want to upload 
# output_file = what you want the file to be named. 
# output files will be save in the results figure directory

python Graph_maker.py ../data/QuestU_Remote_Weather_Station_oct312015.csv Weather_Project
python Stats_maker.py ../data/QuestU_Remote_Weather_Station_oct312015.csv Weather_Project
