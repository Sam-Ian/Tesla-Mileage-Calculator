import csv


with open('TeslaMileage.csv', newline='') as tesla_mileage:
    read_tesla_miles = csv.DictReader(tesla_mileage)

    list_of_dates = []
    list_of_mileage = []
    list_of_mileage_in_period = []
    list_of_elapsed_days = []

    for row in read_tesla_miles:
        list_of_dates.append(row['Date'])

    for row in read_tesla_miles:
        list_of_mileage.append(row['Mileage'])

    for row in read_tesla_miles:
        list_of_mileage_in_period.append(row['Mileage in period'])
        
    for row in read_tesla_miles:
        list_of_elapsed_days.append(row['Elapsed days'])



   


    