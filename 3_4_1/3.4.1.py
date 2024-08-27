import csv


primary_type = {"max_value": 0}


with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[5] in primary_type.keys():
            primary_type[row[5]] = 1
        else:
            primary_type[row[5]] += 1
            if primary_type[row[5]] > primary_type["max_value"]:
                primary_type["max_value"] = primary_type[row[5]]
                result = row[5]





print(result)


