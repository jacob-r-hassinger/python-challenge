import csv
PyBank_csv = r'C:\GitLab\GWU-ARL-DATA-PT-12-2019-U-C\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv'
with open(PyBank_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    totalvotes = 0
    khanvotes = 0
    correyvotes = 0
    livotes = 0
    otooleyvotes = 0
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] == "Khan":
            khanvotes = khanvotes + 1
        if row[2] == "Correy":
            correyvotes = correyvotes + 1
        if row[2] == "Li":
            livotes = livotes + 1
        if row[2] == "O'Tooley": 
            otooleyvotes = otooleyvotes + 1
    
    if khanvotes > correyvotes and khanvotes > livotes and khanvotes > otooleyvotes:
        winner = "Khan"
    if correyvotes > khanvotes and correyvotes > livotes and correyvotes > otooleyvotes:
        winner = "Correy"
    if livotes > khanvotes and livotes > correyvotes and livotes > otooleyvotes:
        winner = "Li"
    if otooleyvotes > khanvotes and otooleyvotes > correyvotes and otooleyvotes > livotes:
        winner = "O'Tooley"
        
    election_data_string = (f"Election Details \n ------------------------- \n Total Votes: {totalvotes} \n ------------------------- \n Khan: {round((khanvotes/totalvotes)*100,4)}% {khanvotes} \n Correy: {round((correyvotes/totalvotes)*100, 4)}% {correyvotes} \n Li: {round((livotes/totalvotes)*100, 4)}% {livotes} \n O'Tooley: {round((otooleyvotes/totalvotes)*100, 4)}% {otooleyvotes} \n ------------------------- \n Winner: {winner} \n -------------------------")
    print(election_data_string)
    election_data_analysis = open("Election_Data.txt", "w+")
    election_data_analysis.write(election_data_string)