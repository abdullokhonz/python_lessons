import csv

rows = [
    ["Abdullo", "+992927448854"]
]

with open('people.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)