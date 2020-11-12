import csv

bom_characters = 'ï»¿'

#READING CSV FILE WITH READ:

with open('TeslaMileageEdit.csv') as csv_file:
    read_csv = csv_file.read()

#print(read_csv, '\n')


################################################################################################

#READING CSV FILE WITH READER:


with open('TeslaMileageEdit.csv', newline='') as tesla_mileage_read:
    read_tesla_miles = csv.reader(tesla_mileage_read)

    list_of_dates = []
    list_of_mileage = []
    list_of_mileage_in_period = []
    full_read_data = []

    for row in read_tesla_miles:
        full_read_data.append(row)

        #CREATE AN ARRAY OF A SINGLE COLUMN
        #list_of_dates.append(row[0])
        #list_of_mileage.append(row[1])
        #list_of_mileage_in_period.append(row[2])

#print(list_of_dates, '\n')
#print(list_of_mileage, '\n')
#print(list_of_mileage_in_period, '\n')


################################################################################################

#WRITING CSV FILE WITH WRITER


with open('TeslaMileage_coded.csv', 'w') as tesla_mileage_write:
    write_tesla_miles = csv.writer(tesla_mileage_write)

    for item in full_read_data:
        write_tesla_miles.writerow(item)

    
################################################################################################

#READING CSV FILE WITH DICTREADER:


with open('TeslaMileageEdit.csv', newline='') as tesla_mileage_dictread:
    dictread_tesla_miles = csv.DictReader(tesla_mileage_dictread)

    dict_list_of_dates = []
    dict_list_of_mileage = []
    dict_list_of_mileage_in_period = []
    full_dictread_data = []

    for row in dictread_tesla_miles:
        full_dictread_data.append(row)

        #CREATE AN ARRAY OF A SINGLE COLUMN
        #dict_list_of_dates.append(row['Date']) 
        #dict_list_of_mileage_in_period.append(row['Mileage in period'])
        #dict_list_of_mileage.append(row['Mileage'])

#print(dict_list_of_dates, '\n')
#print(dict_list_of_mileage, '\n')
#print(dict_list_of_mileage_in_period, '\n')


################################################################################################

#WRITING CSV FILE WITH DICTWRITER


with open('TeslaMileage_dict_coded.csv', 'w') as tesla_mileage_dictwrite:
    fields = ['Date', 'Mileage', 'Mileage in period', 'Elapsed days', 'Average Daily Mileage', 'Average Annual Mileage', 'Projected Mileage @ 20/12/2023', 'Weekly Allowance', 'Week remaining']
    dictwrite_tesla_miles = csv.DictWriter(tesla_mileage_dictwrite, fieldnames=fields)
    
    dictwrite_tesla_miles.writeheader()
    for item in full_dictread_data:
        dictwrite_tesla_miles.writerow(item)


################################################################################################


#print(full_dictread_data, '\n')
#print(full_read_data)