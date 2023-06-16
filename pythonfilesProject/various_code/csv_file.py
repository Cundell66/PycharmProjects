import json

file = open('csv_file.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines]

jclub = []

for line in lines:
    club, city, country = line.split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    jclub.append(data)

out_file = open("json_file.txt", "w")

json.dump(jclub, out_file, indent=6)

out_file.close()
