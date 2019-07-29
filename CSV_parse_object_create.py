import csv

with open("your_mailing_list.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	next(csv_reader)


	for row in csv_reader:
		Name,Email,f_Name,present = row
		if present == "no":
			print("obj.add_user('{}', 123.32, email='{}')".format(row[2],row[1]))
                 
