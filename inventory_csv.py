import csv

inventory = [
    {"item name": "Blue bic","status":"checked in"}
]
with open("inventory.csv",mode = "w") as csvfile:
    fieldnames = inventory[0].keys()
    writter = csv.DictWriter(csvfile,fieldnames = fieldnames)
    writter.writerows(inventory)
