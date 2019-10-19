#The data we need to retrieve.
#1. The total number of votes cast 
#2. A complete list of candidates who received votes 
#3.The percentage of votes eacg candisate won 
#4. The total number of votes eacg candidate won 
#5. The winner of the election based on popular vote.
#Assign a variable for the file to load adn the path.


    #To do:perfrom analysis.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load= os.path.join("Resources","election_results.csv")
# Open the election results and read the file.
#with open(file_to_load)as election_data:
    #Print the file object.
    #print(election_data)


#create a filename variable to a direct or indirect path to the file.
file_to_save= os.path.join("Resources", "election_analysis.txt")
print("Hello world")

#Create a filename variable to a direct or indirect path to file,
file_to_save= os.path.join("analysis", "election_analysis.txt")
dashes_25="-"*25

#Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
#Write some data to  file.

    txt_file.write("Hello World steph\n")

#Write three counties to the file.

    txt_file.write("Counties in the Election\n")

    txt_file.write(dashes_25)
    txt_file.write("\nArapahoe\nDenver\nJefferson\n")
    print(dashes_25)


#Add our dependecies.

import csv
import os

#Assign a variable to load a file from the path.
file_to_load=os.path.join("Resources/election_results.csv")

#Assign a variable to save the file to a path.
file_to_save= os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file.
with open (file_to_load)as election_data:

#To do: read and analyze the data here.

    

