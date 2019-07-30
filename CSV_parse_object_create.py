import csv

with open("example_list.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	next(csv_reader)


	for row in csv_reader:
		Name,Email,Present = row
		if present == "yes":
			print("obj.add_user('{}', email='{}')".format(row[0],row[1]))
                 
