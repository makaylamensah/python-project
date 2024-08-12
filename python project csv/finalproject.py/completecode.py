"""
Makayla Mensah
2257168
"""

import csv
from datetime import datetime

#code for selecting the csv and running it
def print_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# loading data from a csv file into the dictionary
def load_data(filename, column):
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[column]
            data[key] = row
    return data

# load the data from the CSV files
manufacturer_data = load_data('ManufacturerList.csv', 0)
price_data = load_data('PriceList.csv', 0)
service_date_data = load_data('ServiceDatesList.csv', 0)

# turn the data into a inventory list
full_inventory = []
for item_id in manufacturer_data:
    manufacturer_info = manufacturer_data[item_id]
    price = price_data[item_id][1]
    service_date = service_date_data[item_id][1]
    full_inventory.append(manufacturer_info + [price, service_date])

#  name sort my manu name
full_inventory.sort(key=lambda x: x[1])




# heres the outputs code below

# write data to a csv file
def write_data(filename, data, titles=None):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        if titles:
            writer.writerow(titles)
        writer.writerows(data)

# write the full inventory to a file
write_data('FullInventory.csv', full_inventory, titles=['Item ID', 'Manufacturer', 'Item Type', 'Damaged', 'Price', 'Service Date'])

#  separate inventory lists by their item type
item_types = {}
for item in full_inventory:
    item_type = item[2]
    if item_type not in item_types:
        item_types[item_type] = []
    item_types[item_type].append(item)

# write the full inventory to seperate files
for item_type, items in item_types.items():
    items.sort(key=lambda x: x[0])  # this will sort by item ID
    write_data(f'{item_type}LaptopInventory.csv', items, titles=['Item ID', 'Manufacturer', 'Price', 'Service Date', 'Damaged'])

# make a list of items thats past their service dates
today = datetime.now()
past_service_date_inventory = []
for item in full_inventory:
    service_date = datetime.strptime(item[5], '%m/%d/%Y') #creates a datatime object from a given string
    if service_date < today:
        past_service_date_inventory.append(item) #adds an elment to the end of a list

# sort the past service date inventory by date
past_service_date_inventory.sort(key=lambda x: datetime.strptime(x[5], '%m/%d/%Y'))

# write the past service date inventory to a csv file
write_data('PastServiceDateInventory.csv', past_service_date_inventory, titles=['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])

# make a list of items for the damaged items
damaged_inventory = [item for item in full_inventory if item[3]]


# sort the damaged inventory by price in decreasing order
damaged_inventory.sort(key=lambda x: float(x[4]), reverse=True)


# write the damaged inventory to a CSV file
write_data('DamagedInventory.csv', damaged_inventory, titles=['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date'])

if __name__ == '__main__':
    while True:
        print("1. FullInventory.csv")
        print("2. LaptopInventory.csv")
        print("3. PastServiceDateInventory.csv")
        print("4. DamagedInventory.csv")
       

        choice = input("pick the # to print your selected csv file ")

        # not sure if i did that part right but I respectfully gave up