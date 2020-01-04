#PyBank script: works through the PyBank csv file and prepares requested summary statistics
import csv
PyBank_csv = r'C:\GitLab\GWU-ARL-DATA-PT-12-2019-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv'
with open(PyBank_csv, newline='') as csvfile:
#opens the file, sets indicates delimited by comma, assigns the header
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #assigns variables and sets initial values for loops
    total_months = 0
    total_profit = 0
    profits = []
    months = []
    profit_change_list = []

    #loops through the rows to count the total months, accumulates profit totals, and adds total profits and months to separate lists
    for row in csvreader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        profits.append(int(row[1]))
        months.append(str(row[0]))
    #sets counter to 1 for the next loop; calculates the changes between the different profit values that were stored in the list in the last loop
    #then adds the changes in profit to a new list
    counter = 1
    while counter < total_months:
        profit_change = int(profits[counter]) - int(profits[counter - 1])
        profit_change_list.append(profit_change)
        counter += 1

    #calculates the summary statistics for the .txt file and terminal, finds the month for some of the corresponding values (greatest and least, etc)
    average_profit_change = sum(profit_change_list)/(total_months - 1)
    greatest_increase = max(profit_change_list)
    month_of_increase = months[profit_change_list.index(greatest_increase)+1]
    greatest_decrease = min(profit_change_list)
    month_of_decrease = months[profit_change_list.index(greatest_decrease)+1]
    
    #creates the string with the summary values formatted into it
    financial_analysis_str = (f"Financial Analysis \n ---------------------------- \n Total Months: {total_months} \n Total: ${total_profit} \n Average Change: ${profit_change} \n Greatest Increase in Profits: {month_of_increase} (${greatest_increase}) \n Greatest Decrease in Profits: {month_of_decrease} (${greatest_decrease})")
    
    #displays in terminal
    print(financial_analysis_str)
    
    #creates a .txt file and writes the summary string to the file
    PyBank_financial_analysis = open("PyBank.txt", "w+")
    PyBank_financial_analysis.write(financial_analysis_str)
