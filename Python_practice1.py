#Add our dependencies 
import csv
import os

#Assign variable to load a file from path.
file_to_load=os.path.join("Resources/election_results.csv")

#Assign a variable to save the file path.
file_to_save=os.path.join("analysis","election_analysis.txt")        

#Initialize a total voter counter
total_votes= 0

#Candidate options and candisate votes
candidate_options=[]

#Declare the emprty dictionary.
candidate_votes={}

#open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Read the header row.
