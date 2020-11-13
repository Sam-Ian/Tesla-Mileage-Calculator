import csv


################################################################################################

#READING CSV FILE WITH DICTREADER:


with open('TeslaMileageEdit.csv', newline='') as tesla_mileage_read:
    read_tesla_miles = csv.DictReader(tesla_mileage_read)

    list_of_dates = []
    list_of_mileage = []
    list_of_mileage_in_period = []
    full_read_data = []

    for row in read_tesla_miles:
        full_read_data.append(row)

        #CREATE AN ARRAY OF A SINGLE COLUMN
        list_of_dates.append(row['Date']) 
        list_of_mileage_in_period.append(row['Mileage in period'])
        list_of_mileage.append(row['Mileage'])


################################################################################################

#FORMULAS FOR OTHER COLUMNS

################################################################################################

#ELAPSED DAYS

from datetime import datetime

#Find difference between two dates
elapsed_days = []

for i in range(len(list_of_dates)):
    if i == 0:
        elapsed_days.append(0)    
    else:
        date_format = "%d/%m/%Y"
        current_date = datetime.strptime(list_of_dates[i], date_format)
        previous_date = datetime.strptime(list_of_dates[i-1], date_format)
        elapsed_days_difference_date = (current_date - previous_date)
        elapsed_days.append(elapsed_days_difference_date.days)

#Add the cumulative value of difference of dates

for i in range(len(elapsed_days)):
    if i != 0:
        elapsed_days[i] += elapsed_days[i-1]


#####################################################

#AVERAGE DAILY MILEAGE

#Convert mileage list into 'int' type

list_of_mileage = list(map(int, list_of_mileage))

#Creating empty array for average daily mileage
average_daily_mileage = [0 for num in elapsed_days]

#Looping through (mileage / elapsed days) and adding the sum to average daily miles
for i in range(len(average_daily_mileage)):
    try:
        average_daily_mileage[i] = list_of_mileage[i] / elapsed_days[i]
    except ZeroDivisionError:
        average_daily_mileage[i] = 0

#Rounding average_daily_miles list to 8 decimal places

average_daily_mileage = [round(num, 8) for num in average_daily_mileage]


#####################################################

#AVERAGE ANNUAL MILEAGE

#Average Annual Mileage = Average Daily Mileage * 365

average_annual_mileage = [0 for num in average_daily_mileage]

for i in range(len(average_daily_mileage)):
    average_annual_mileage[i] = average_daily_mileage[i] * 365

#Rounding numbers to nearest int

average_annual_mileage = [round(num) for num in average_annual_mileage]


#####################################################

#Projected Mileage @ 20/12/2023

#Projected Mileage @ 20/12/2023 = Average Daily Mileage * 1460

projected_mileage = [0 for num in average_daily_mileage]

for i in range(len(average_daily_mileage)):
    projected_mileage[i] = average_daily_mileage[i] * 1460

#Rounding numbers to nearest int

projected_mileage = [round(num) for num in projected_mileage]


#####################################################

#WEEKS REMAINING


weeks_remaining = []
end_date = '20/12/2023'

for i in range(len(list_of_dates)):
    if i == 0:
        weeks_remaining.append(0)    
    else:
        date_format = "%d/%m/%Y"
        end_week = datetime.strptime(end_date, date_format)
        date_list = datetime.strptime(list_of_dates[i], date_format)
        weeks_remaining_sum = (end_week - date_list)
        weeks_remaining.append(weeks_remaining_sum.days / 7)

#Rounding weeks to a whole week

weeks_remaining = [round(num) for num in weeks_remaining]


#####################################################

#REMAINING MILES

#40,000 - MILEAGE

remaining_miles = [0 for num in list_of_mileage]

for i in range(len(list_of_mileage)):
    remaining_miles[i] = 40000 - list_of_mileage[i]


#####################################################

#WEEKLY ALLOWANCE

# (REMAINING MILES / REMAINING WEEKS)


weekly_allowance = [0 for num in weeks_remaining]

for i in range(len(weekly_allowance)):
    try:
        weekly_allowance[i] = remaining_miles[i] / weeks_remaining[i]
    except ZeroDivisionError:
        weekly_allowance[i] = 0

#Rounding to whole number

weekly_allowance = [round(num, 1) for num in weekly_allowance]


#####################################################

list_of_dates.insert(0, 'Date')
list_of_mileage.insert(0, 'Mileage')
list_of_mileage_in_period.insert(0, 'Mileage in period')
elapsed_days.insert(0, 'Elapsed days')
average_daily_mileage.insert(0, 'Average Daily Mileage')
average_annual_mileage.insert(0, 'Average Annual Mileage')
projected_mileage.insert(0, 'Projected Mileage @ 20/12/2023')
weeks_remaining.insert(0, 'Week remaining')
remaining_miles.insert(0, 'Remaining miles')
weekly_allowance.insert(0, 'Weekly Allowance')
print(list_of_dates)
print(list_of_mileage)
print(list_of_mileage_in_period)
print(elapsed_days)
print(average_daily_mileage)
print(average_annual_mileage)
print(projected_mileage)
print(weeks_remaining)
print(remaining_miles)
print(weekly_allowance)




#WRITING CSV FILE WITH DICTWRITER


with open('TeslaMileage_coded.csv', 'w') as tesla_mileage_write:
    fields = ['Date', 'Mileage', 'Mileage in period', 'Elapsed days', 'Average Daily Mileage', 'Average Annual Mileage', 'Projected Mileage @ 20/12/2023', 'Weekly Allowance', 'Week remaining']
    write_tesla_miles = csv.DictWriter(tesla_mileage_write, fieldnames=fields)
    
    write_tesla_miles.writeheader()
    for item in full_read_data:
        write_tesla_miles.writerow(item)

