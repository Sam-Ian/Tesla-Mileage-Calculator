import csv
from datetime import datetime
import time

################################################################################################

#READING CSV FILE WITH DICTREADER:

with open('Tesla_Mileage.csv', newline='') as tesla_mileage_read:
    read_tesla_miles = csv.DictReader(tesla_mileage_read)

    list_of_dates = []
    list_of_mileage = []
    full_read_data = []

    for row in read_tesla_miles:
        full_read_data.append(row)

        #CREATE AN ARRAY OF A SINGLE COLUMN
        list_of_dates.append(row['Date']) 
        list_of_mileage.append(row['Mileage'])


################################################################################################

#USER INTERFACE FEATURE


print("""  ______          __         __  ____ __                         ______      __           __      __            
 /_  __/__  _____/ /___ _   /  |/  (_) /__  ____ _____ ____     / ____/___ _/ /______  __/ /___ _/ /_____  _____
  / / / _ \/ ___/ / __ `/  / /|_/ / / / _ \/ __ `/ __ `/ _ \   / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
 / / /  __(__  ) / /_/ /  / /  / / / /  __/ /_/ / /_/ /  __/  / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
/_/  \___/____/_/\__,_/  /_/  /_/_/_/\___/\__,_/\__, /\___/   \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
                                               /____/                                                          """)

print('\n')
print("Welcome back Ian, today's date is: " + datetime.today().strftime('%d/%m/%Y') + ".")
print('\n')


while True:

    new_mileage = (input("Please enter your Tesla's current total mileage reading: "))

    print('\n')
    y_n_statement = input("You typed in '" + new_mileage + "'. If this is correct please type 'y'. To cancel type 'n': ")
    print('\n')
    if y_n_statement == 'y' or y_n_statement == 'n':
        if y_n_statement == 'y':
            if (datetime.today().strftime('%d/%m/%Y')) in list_of_dates:
                print("You have already submitted a mileage reading today. Please try again tomorrow.")
                break 
            else:
                list_of_mileage.append((new_mileage))
                list_of_dates.append(datetime.today().strftime('%d/%m/%Y'))
                print("Thank you, we are adding the updated mileage to your database now.", '\n')
                time.sleep(1)
                print("Updating... ", '\n')
                time.sleep(1)
                print("Your database has now been updated.",'\n')
                time.sleep(1)
                print("Drive Safe!",'\n\n')   
                break             
        else:
            continue
    else:
        print('\n')
        print("Please type 'y' for yes, or 'n' for no.")
        print('\n')


################################################################################################

#FORMULAS FOR OTHER COLUMNS

################################################################################################

#MILEAGE IN PERIOD

#MILEAGE - PREVIOUS MILEAGE

#Convert mileage list into 'int' type

list_of_mileage = list(map(int, list_of_mileage))

list_of_mileage_in_period = [0 for item in list_of_mileage]

for i in range(len(list_of_mileage)):
    if i == 0:
        list_of_mileage_in_period[i] = 0
    else:
        list_of_mileage_in_period[i] = list_of_mileage[i] - list_of_mileage[i-1]


################################################################################################

#ELAPSED DAYS

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


#Create dictionary of all column lists

new_csv_data = [{'Date': date, 'Mileage': mileage, 'Mileage in Period': mileageperiod, 'Elapsed Days': elapseddays, 'Average Daily Mileage': averagedailymileage, 'Average Annual Mileage': averageannualmileage, 'Projected Mileage @ 20/12/2023': projectedmileage, 'Weeks Remaining': weeksremaining, 'Remaining Miles': remainingmiles, 'Weekly Allowance': weeklyallowance} for date, mileage, mileageperiod, elapseddays, averagedailymileage, averageannualmileage, projectedmileage, weeksremaining, remainingmiles, weeklyallowance in zip(list_of_dates, list_of_mileage, list_of_mileage_in_period, elapsed_days, average_daily_mileage, average_annual_mileage, projected_mileage, weeks_remaining, remaining_miles, weekly_allowance)]


# print(new_csv_data)

#WRITING CSV FILE WITH DICTWRITER


with open('Tesla_Mileage.csv', 'w', newline='') as tesla_mileage_write:
    fields = ['Date', 'Mileage', 'Mileage in Period', 'Elapsed Days', 'Average Daily Mileage', 'Average Annual Mileage', 'Projected Mileage @ 20/12/2023', 'Weeks Remaining', 'Remaining Miles', 'Weekly Allowance']
    write_tesla_miles = csv.DictWriter(tesla_mileage_write, fieldnames=fields)
    
    write_tesla_miles.writeheader()
    for item in new_csv_data:
        write_tesla_miles.writerow(item)

