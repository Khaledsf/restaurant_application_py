from tabulate import tabulate
import csv
import os
import prints
import restaurant


eatery = restaurant.Restaurant()

prints.greet()
prints.take_action()
menu = ''
while menu != 'q' and menu != 'quit':
	menu = input()
	if menu == '1':
		eatery.create()
		eatery.list()
	elif menu == '2':
		eatery.search()
	elif menu == '3':
		eatery.list()
	elif menu == '4':
		change = input('''What would you like to to alter?\nType 1 to change the name.\nType 2 to change the cuisine.\nType 3 to change the price.\nType 4 to change the location.\nType 5 to delete restaurant.\nType 6 to go back to the main menu.\n''')
		if change == '1':
			column = 'Name'
			print('Name')
			eatery.update_item(column)
			eatery.list()
		elif change == '2':
			print('Cuisine')
			column = 'Cuisine'
			eatery.update_item(column)
			eatery.list()
		elif change == '3':
			print('Price')
			column = 'Price'
			eatery.update_item(column)
			eatery.list()
		elif change == '4':
			print('Location')
			column = 'Location'
			eatery.update_item(column)
			eatery.list()
		elif change == '5':
			eatery.delete_item()
			eatery.list()
		elif change == '6':
			prints.take_action()
		else:
			prints.option_no_exists()
	
	elif menu not in ('1', '2', '3', '4') and menu not in ('quit', 'q'):
		prints.option_no_exists()
		prints.take_action()
	else:
		prints.say_bye()
		break