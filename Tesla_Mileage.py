import csv


with open('TeslaMileage.csv', newline='') as tesla_mileage:
    read_tesla_miles = csv.DictReader(tesla_mileage)

    list_of_dates = []
    list_of_mileage = []
    list_of_mileage_in_period = []
    list_of_elapsed_days = []


    #WHY IS THERE A KEY ERROR WITH THIS FOR LOOP, 'Date' IS THE CORRECT KEY IN THE CSV FILE?!?!
    for row in read_tesla_miles:
        list_of_dates.append(row['Date'])

    #ONLY THE ABOVE FOR LOOP WORKS^^^
    #TOP FOR LOOP IS THE ONLY ONE THAT EXECUTES WHICHEVER ONE I PUT AT THE TOP

    for row in read_tesla_miles:
        list_of_mileage.append(row['Mileage'])

    for row in read_tesla_miles:
        list_of_mileage_in_period.append(row['Mileage in period'])
        
    for row in read_tesla_miles:
        list_of_elapsed_days.append(row['Elapsed days'])


print(list_of_mileage)
print(list_of_mileage_in_period)
   


    