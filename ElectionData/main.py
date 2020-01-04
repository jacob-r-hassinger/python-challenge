#opens the csv file for the Election Data csv file
import csv
electiondata_csv = r'C:\GitLab\GWU-ARL-DATA-PT-12-2019-U-C\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv'
#assigns the header and sets comma as delimiter for the reader
with open(electiondata_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #sets all count variables to 0 and declares variable type
    totalvotes = 0.000
    khanvotes = 0.000
    correyvotes = 0.000
    livotes = 0.000
    otooleyvotes = 0.000
    
    #loops through the csv file to count total votes that were made and the counts the total votes for each of those running
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] == "Khan":
            khanvotes = khanvotes + 1
        elif row[2] == "Correy":
            correyvotes = correyvotes + 1
        elif row[2] == "Li":
            livotes = livotes + 1
        elif row[2] == "O'Tooley": 
            otooleyvotes = otooleyvotes + 1
    
    #determines the winner by comparing vote totals
    if khanvotes > correyvotes and khanvotes > livotes and khanvotes > otooleyvotes:
        winner = "Khan"
    elif correyvotes > khanvotes and correyvotes > livotes and correyvotes > otooleyvotes:
        winner = "Correy"
    elif livotes > khanvotes and livotes > correyvotes and livotes > otooleyvotes:
        winner = "Li"
    elif otooleyvotes > khanvotes and otooleyvotes > correyvotes and otooleyvotes > livotes:
        winner = "O'Tooley"
        
    #uses the values assigned in the earlier sections to compose a formatted summary string
    election_data_string = (f"Election Details \n ------------------------- \n Total Votes: {totalvotes} \n ------------------------- \n Khan: {round((khanvotes/totalvotes)*100,4)}% {khanvotes} \n Correy: {round((correyvotes/totalvotes)*100, 4)}% {correyvotes} \n Li: {round((livotes/totalvotes)*100, 4)}% {livotes} \n O'Tooley: {round((otooleyvotes/totalvotes)*100, 4)}% {otooleyvotes} \n ------------------------- \n Winner: {winner} \n -------------------------")
    #prints the string to terminal
    print(election_data_string)
    #creates a .txt file and writes the summary string to the text file as well
    election_data_analysis = open("Election_Data.txt", "w+")
    election_data_analysis.write(election_data_string)
