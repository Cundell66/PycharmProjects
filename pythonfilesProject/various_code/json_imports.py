import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file)

file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

out_file = open("cars.json", "w")

json.dump(cars, out_file, indent=6)

out_file.close()
