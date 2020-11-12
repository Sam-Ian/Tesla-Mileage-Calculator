import csv

bom_characters = 'ï»¿'

#READING CSV FILE WITH DICTREADER:

with open('TeslaMileageEdit.csv', newline='') as tesla_mileage_dict:
    dictread_tesla_miles = csv.DictReader(tesla_mileage_dict)

    dict_list_of_dates = []
    dict_list_of_mileage = []
    dict_list_of_mileage_in_period = []

    for row in dictread_tesla_miles:
        dict_list_of_dates.append(row['Date']) 
        dict_list_of_mileage_in_period.append(row['Mileage in period'])
        dict_list_of_mileage.append(row['Mileage'])

print(dict_list_of_dates, '\n')
print(dict_list_of_mileage, '\n')
print(dict_list_of_mileage_in_period, '\n')

#READING CSV FILE WITH READER:

with open('TeslaMileageEdit.csv', newline='') as tesla_mileage:
    read_tesla_miles = csv.reader(tesla_mileage)

    list_of_dates = []
    list_of_mileage = []
    list_of_mileage_in_period = []

    for row in read_tesla_miles:
        list_of_dates.append(row[0])
        list_of_mileage.append(row[1])
        list_of_mileage_in_period.append(row[2])

print(list_of_dates, '\n')
print(list_of_mileage, '\n')
print(list_of_mileage_in_period, '\n')
 