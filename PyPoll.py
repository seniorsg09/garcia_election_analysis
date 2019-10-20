    #To do:perfrom analysis.
import csv
import os

# Assign a variable for the file to load and the path
file_to_load= os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to file,
file_to_save= os.path.join("analysis", "election_analysis.txt")
dashes_25="-"*25

# Initialize a total vote counter.
total_votes=0

#Candidate options and candidate votes
candidate_options=[]
candidate_votes={}

#Track the winning candidate, vote count, and percentage.
winning_candidate=""
winning_count= 0
winning_percentage= 0

with open(file_to_load)as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print(headers)


#print each row in the csv file.
    i = 0
    for row in file_reader:
        if i < 5:
            print(row)
            i += 1

#Candidate options and candidate votes
candidate_options= []

#Declare the empty dictionary.
candidate_votes={}

#Open the election results and read the file.
with open (file_to_load) as election_data:
    file_reader= csv.reader(election_data)

    #print each row in the CSV file.
    for now in file_reader:
        #Add to the total vote count.
        total_votes +=1

        #Print the candidate name from each row.
        candidate_name= row[2]
        
if  candidate_name not in candidate_options:
    #Add the candidate name to the candidate list.
    candidate_options.append(candidate_name) 

    #Begin tracking that candidate's vote count.
    candidate_votes[candidate_name]= 0

    #Add a vote to that candidate's count
    candidate_votes[candidate_name]+= 1

    #Print the candidate vote dictionary
    print(candidate_votes)   

#Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:
    #Retrieve vote count of a candidate.
    votes= candidate_votes[candidate]  
#Calcualte the percentage of votes.
vote_percentage= int(votes)/ int(total_votes)*100
#Print the candidate name and percentage of votes.
print(f"{candidate}: received {vote_percentage}% of vote.")    

#winning candidate and Winning Count Tracker
winning_candidate=""
winning_count= 0
winning_percentage= 0

#Determiine the percentage of votes for each candidate by looping through the counts.
#Iterate through the candidate list.
for candidate in candidate_votes:
    #Retrieve vote count of a candidate.
    votes= candidate_votes[candidate]
    #Calculate percentage of votes.
    vote_percentage= float(votes)/ float(total_votes)*100

    #To do: Print out each candidate's name, vote count, and percenatge of 
    #votes to the terminal.

    #Determine winning vote count and candidate 
    #Determine if the votes is greater than the winning count.
    if (votes> winning_count) and (vote_percentage> winning_percentage):
        # If true then set winning_count= votes and winning_percent=
        #vote_percentage.
        winning_count= votes 
        winning_percentage= vote_percentage
        #And, set the winning_candidate equal to the candidate's name.
        winning_candidate=candidate
# To do: print out the winning candidate, vote count and percentage to 
# terminal.
print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n") 

winning_candidate_summary=(f"dashes_25\n" f"Winnner: {winning_candidate}\n" f"Winning Vote Count: {winning_count:,}\n" f"Winning Percentage:{winning_percentage:.1f}%\n" f"dashes_25\n" )
