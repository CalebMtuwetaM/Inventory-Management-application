#Import necessary modules
import uuid
from datetime import datetime

#Create an empty items list
items = []

#add item function
def add_item(name,description,number,cost,status):
    # item name cannot be empty
    for item in items:
        if name == "":
            raise ("item name cannot be empty")
    # item description cannot be empty
    for item in items:
        if description == "":
            raise ("item description cannot be empty")
    # item number cannot be empty
    for item in items:
        if number == "":
            raise ("item number cannot be empty")
    # item cost cannot be empty
    for item in items:
        if cost == "":
            raise ("item cost cannot be empty")
    #validate the number to only allow integers for item in items:
    if not isinstance(number, int):
        raise ("number should be an integer")
    # validate the cost to only allow integers for item in items:
    if not isinstance(cost, int):
        raise ("cost should be an integer")
    #validate the state if its only "checked in or checked out"
    for item in items:
        if status != "checked in " or "checked out":
            raise("status can only be checked in or checked out")
    #item properties
    item = {
        "item_name": name,
        "item_id": uuid.uuid4(),
        "item_description": description,
        "total_number": number,
        "cost_per_item": cost,
        "date_added": datetime.now(),
        "item_status": status
    }
    # add item to items
    items.append(item)


# remove item function
def item_remove(item_id):
    is_removed = False
    for item in items:
        if item["item_id"] == item_id:
            items.remove(item)
            is_removed = True
    if is_removed == True:
        return ("the item has been removed")

#list all items
def items_list():
    return items

#item check out function to remove an item from the items array
def item_checkout(item_id):
    is_checked_out = False
    for item in items:
        if item["item_id"] == item_id:
            items.remove(item)
            is_checked_out = True
    #update the status of the item
    for item in items:
        if is_checked_out == True and item["item_id"] == item_id:
            item["item_status"] = "checked out"
    if is_checked_out == True:
        return("item has been checked out")

#item check in function to check in an item that had been checked out
def item_check_in(item_id):
    is_checked_in = False
    for item in items:
        if item["item_id"] == item_id and item["item_status"] == "checked out":
            items.append(item)
            is_checked_in = True
    #update the status of the item
    for item in items:
        if is_checked_in == True and item["item_id"] == item_id:
            item["item_status"] = "checked in"
    if is_checked_in == True:
        return("item has been checked back in")

#item view fuction to view an item
def item_view(item_id):
    for item in items:
        if item["item_id"] == item_id:
            return item

#make an item search function by name
def item_search_by_name(name):
    for item in items:
        if item["item_name"] == name:
            return item

# make an item search function by description
def item_search_by_description(querystring):
    items_found = []
    for item in items:
        if querystring in item["item_description"]:
            items_found.append(item)

    return items_found
