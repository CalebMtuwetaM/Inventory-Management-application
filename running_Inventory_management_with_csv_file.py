import Inventorymanagement

#add items
Inventorymanagement.add_item("pen","blue bic",20,30,"checked in")

#giving items variables
item1 = Inventorymanagement.items[0]

#to test if the function that finds an item by item id really works
print(Inventorymanagement.find_item_by_ID(item1["item_id"]))

#to remove an item
#print(Inventorymanagement.item_remove(item1["item_id"]))

#to list all the items
#print(Inventorymanagement.items_list())

#to check out an item
#print(Inventorymanagement.item_checkout(item1["item_id"]))

#to check in an item
#print(Inventorymanagement.item_check_in(item1["item_id"]))

#to view an item
#print(Inventorymanagement.item_view(item1["item_id"]))

#to search an item by name
#print(Inventorymanagement.item_search_by_name("pen"))

#to search an item by the item description
#print(Inventorymanagement.item_search_by_description("bic"))

#to export the inventory csv file
Inventorymanagement.export_items("inventory.csv")

#to import the inventory csv file
Inventorymanagement.import_items("inventory.csv")
