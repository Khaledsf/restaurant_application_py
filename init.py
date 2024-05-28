import subprocess
import os
import csv

if not os.path.exists('./list_restaurants.csv'):
	with open("./list_restaurants.csv", "x") as file:
		csv.writer(file).writerow(['ID' ,'Name', 'Cuisine', 'Price', 'Location'])

subprocess.run(["python", "guide.py"])