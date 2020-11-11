import csv


with open('TeslaMileageEdit.csv', newline='') as tesla_mileage:
    read_tesla_miles = csv.DictReader(tesla_mileage)

    list_of_fred = []
    list_of_mileage = []
    list_of_mileage_in_period = []
    list_of_elapsed_days = []  

    for row in read_tesla_miles:
        list_of_fred.append(row['Sam']) 
        list_of_mileage_in_period.append(row['Mileage in period'])
        list_of_mileage.append(row['Mileage'])
        list_of_elapsed_days.append(row['Elapsed days'])

print(list_of_fred)
print(list_of_mileage)
print(list_of_mileage_in_period)
print(list_of_elapsed_days)
   

 