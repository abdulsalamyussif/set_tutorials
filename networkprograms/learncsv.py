import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_read_dict_method = csv.DictReader(csv_file)

    for row in csv_read_dict_method:
        print(row['department'])

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter= '\t')

#    next(csv_reader)

        for line in csv_reader:
            csv_writer.writerow(line)
