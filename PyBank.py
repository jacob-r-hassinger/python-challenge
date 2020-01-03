import csv
PyBank_csv = r'C:\GitLab\GWU-ARL-DATA-PT-12-2019-U-C\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv'
with open(PyBank_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    total_months = 0
    total_profit = 0
    profits = []
    months = []
    profit_change_list = []
    for row in csvreader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        profits.append(int(row[1]))
        months.append(str(row[0]))
    counter = 1
    while counter < total_months:
        profit_change = int(profits[counter]) - int(profits[counter - 1])
        profit_change_list.append(profit_change)
        counter += 1
    average_profit_change = sum(profit_change_list)/(total_months - 1)
    greatest_increase = max(profit_change_list)
    month_of_increase = months[profit_change_list.index(greatest_increase)+1]
    greatest_decrease = min(profit_change_list)
    month_of_decrease = months[profit_change_list.index(greatest_decrease)+1]
    financial_analysis_str = (f"Financial Analysis \n ---------------------------- \n Total Months: {total_months} \n Total: ${total_profit} \n Average Change: ${profit_change} \n Greatest Increase in Profits: {month_of_increase} (${greatest_increase}) \n Greatest Decrease in Profits: {month_of_decrease} (${greatest_decrease})")
    print(financial_analysis_str)
    PyBank_financial_analysis = open("PyBank.txt", "w+")
    PyBank_financial_analysis.write(financial_analysis_str)
