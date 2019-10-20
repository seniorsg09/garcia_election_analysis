#Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load= os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path.
file_to_save= os.path.join("analysis", "election_analysis.txt")
dashes_25="-"*25

#Initialize a total vote counter.
total_votes= 0
#candidate options and candidate votes 
candidate_options=[]
candidate_votes= {}
#county options and county votes
county_votes= {}
county_options=[]
#Track the winning candidate, vote count, and percentage.
winning_candidate=""
winning_count= 0
winning_percentage= 0

winning_county=""
winning_county_count=0
winning_percentage=0 
#Open the election results and read the file.

with open (file_to_load) as election_data:
    file_reader= csv.reader (election_data)
#Read the header row.
headers= next(file_reader)
#Print each row in the CSV file.
for row in file_reader:
    #Add to the total vote count.
    total_votes +=1
    #Get the candidate name from each row.
    candidate_name= row[2]
    county_name=row[1]
    #If the candidate does not match any existing candidate add it the 
    # the candidate list.
if candidate_name not in candidate_options:
        #Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)
        # And begin tracking that candidate's voter count.    
        candidate_votes[candidate_name]= 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

if county_name not in county_options:
     county_options.append(county_name)
 #Tracking each candidates vote count 
     county_votes[county_name]=0
 #Add a vote to candidates count
     county_votes[county_name]+=1

 #Save the results to our text file.
with open (file_to_save,"w") as txt_file:
#Print(election_results, end="")
    election_results=(
    f"\nElection Results\n"
    f"-------------------------\n"
    f" Total votes:{total_votes:,}\n"
    f"-------------------------\n")   
    print (election_results,end="") 
#Save the results to our text file.
txt_file.write(election_results)  

for county in county_votes:
#Retrieve vote count and percentage.
votes=county_votes [county].
#Calculate percentage of votes.
vote_percentage=float(votes)/float(total_votes)*100
candidate_results=(f"{candidate}:{vote_percentage:.1f}%({votes:,})\n")
#Print each candidate's voter count and percentage to the terminal.
    print(candidate_results)
#save the candidate results io our text file.
txt_file.write(candidate_results)
#Determine winning vote county, winning percentage, and winning candidate.
    if (votes> winning_county_count) and (vote_percentage > winning_percentage):
    winning_county_count=votes\
    winning_candidate=candidate    
    winning_percentage= vote_percentage
    txt_file.write("\n")

    #print the winning candidate's results to terminal.
    election_results= (
     f"Winner: {winning_county}\n"
     f"-------------------------\n")
print(election_results,end="")
     txt_file.write(election_results)
for candidate in candidate_votes:
         #Retrieve vote count and percentage
         votes=candidate_votes[candidate]
         vote_percentage= float (votes)/ float (total_votes)*100
         candidate_results=(f"{candidate}:{vote_percentage:. 1f}% ({votes:,})\n")
         # Print each candidates voter count and percentage to the terminal.
         print(candidate_results)
         #Save the candidate results to our text file.
         txt_file.write(candidate_results)
         #Determine winning vote count, winning percentage, and winning candidate.
    if (votes > winning_count)and (vote_percentage > winning_percentage):
             winning_count= votes
             winning_candidate= candidate 
             winning_percentage= vote_percentage
#Print the winning candidates results to the terminal.
winning_candidate_summary= (
    f"-------------------------\n"
    f"Winner:{winning_candidate}\n"
    f"Winning Vote count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#Save the winning candidates results to the text file.
txt_file.write(winning_candidate_summary)
    