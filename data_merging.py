import csv
df = []

with open("dataset_2.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        df.append(row)

headers = df[0]
planet_data = df[1:]

for data_point in planet_data:
    data_point[2] = data_point[2].lower()
planet_data.sort(key = lambda planet_data : planet_data[2])

with open("dataset2_sorted.csv","a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)  