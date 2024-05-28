from tabulate import tabulate
import csv
import os
import prints
from pprint import pprint

class Restaurant:
    
    def create(self):
	    with open("./list_restaurants.csv", "r") as read_obj:
	        csv_reader = csv.reader(read_obj)
	        list_of_csv = list(csv_reader)
	        num = len(list_of_csv)
	    prints.choice_to_add()
	    id = num
	    name = input("Name: ")
	    cuisine = input("Type of cuisine: ")
	    price = input("Price category with $ sign: ")
	    district = input("Location: ")
	    data = [
	        id,
	        name.title().strip(),
	        cuisine.capitalize().strip(),
	        price.strip(),
	        district.title().strip(),
	    ]

	    with open("./list_restaurants.csv", "a", newline="") as file:
	        writer = csv.writer(file)
	        writer.writerow(data)
	        prints.added()
	        prints.take_action()

    def search(self):
	    value = input("enter price\n")
	    result_list = []
	    with open("./list_restaurants.csv", mode="r") as file:
	        csv_reader = csv.reader(file)
	        for row in csv_reader:
	            for item in row:
	                if item == value:
	                    result_list.append(row)
	    if len(result_list) < 1:
	        prints.no_match()
	        prints.take_action()
	    else:
	        print(
	            tabulate(
	                result_list,
	                headers=["ID", "Name", "Cuisine", "Price", "District"],
	                tablefmt="psql",
	            )
	        )
	        prints.take_action()
	
    def list(self):
	    if len(list(csv.reader(open("./list_restaurants.csv")))) == 1:
	        prints.empty()
	    with open("./list_restaurants.csv", "r") as read_obj:
	        csv_reader = csv.reader(read_obj)
	        list_of_csv = list(csv_reader)
	        print(tabulate(list_of_csv, headers="firstrow", tablefmt="psql"))
	        prints.take_action()

    def update(self):
    	id = input('Enter id of restaurant\n')
    	restaurant = ['0']
    	with open('./list_restaurants.csv', 'r') as read_obj:
    		for row in csv.reader(read_obj):
    			if row[0] == id:
    				restaurant = row
    				print(tabulate([restaurant], headers= ["ID", "Name", "Cuisine", "Price", "District"], tablefmt="psql"))
    	return restaurant[0]
   
    def update_item(self, column=None):
    	restaurant_id = Restaurant.update(self)
    	if restaurant_id == '0':
    		prints.no_exists()
	    	Restaurant.update_item(self, column)
    	elif restaurant_id != '0':
	    	new_item = input(f"Enter new {column}\n")
	    	csv_file_path = "./list_restaurants.csv"
	    	with open(csv_file_path, mode='r', newline='') as file:
	    		csv_reader = csv.DictReader(file)
	    		rows = list(csv_reader)
	    		for row in rows:
	    			if row["ID"] == restaurant_id:
	    				row[f"{column}"] = new_item
	    	fieldnames = rows[0].keys()
	    	with open(csv_file_path, mode="w", newline="") as file:
	    		csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
	    		csv_writer.writeheader()
	    		csv_writer.writerows(rows)
	    	prints.update_successful()
    
    def delete_item(self, column=None):
    	prints.enter_id()
    	column = 'ID'
    	delete_item = ''
    	rows = []
    	idx = 0
    	restaurant_id = input()
    	if restaurant_id == '0':
    		prints.no_exists()
    		Restaurant.update_item(self, column)
    	if restaurant_id != '0':
    	    restaurant = ['0']
    	    csv_file_path = "./list_restaurants.csv"
    	    with open(csv_file_path, 'r') as read_obj:
    	    	for row in csv.reader(read_obj):
    	    		if row[0] == restaurant_id:
    	    			restaurant = row
    	    			prints.about_to_delete()
    	    			print(tabulate([restaurant], headers= ["ID", "Name", "Cuisine", "Price", "District"], tablefmt="psql"))
    	    
    	    prints.type_to_confirm()
    	    confirmation = input()
    	    if confirmation in ('1'):
	    	    with open(csv_file_path, mode='r', newline='') as file:
	    	    	rows = list(csv.reader(file))

	    	    for row in rows:
	    	    	if row[0] == restaurant_id:
	    	    		delete_item = row
	    	    		idx = rows.index(delete_item)
	    	    		rows.pop(idx)
	    	    csv_file_path = "./list_restaurants.csv"
	    	    with open(csv_file_path, mode='w', newline='') as file:
	    	    	csv.writer(file).writerows(rows)
	    	    prints.update_successful()


