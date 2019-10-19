    #To do:perfrom analysis.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load= os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to file,
file_to_save= os.path.join("analysis", "election_analysis.txt")
dashes_25="-"*25
with open(file_to_load)as election_data:
    file_reader=csv.reader(election_data)
    #Read and print header row.
    headers=next(file_reader)
    print(headers)


#print each row in the csv file.
    i = 0
    for row in file_reader:
        if i < 5:
            print(row)
            i += 1



        