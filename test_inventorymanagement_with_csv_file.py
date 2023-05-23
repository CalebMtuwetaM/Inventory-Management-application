import unittest
import Inventorymanagement_with_inventory_csv_file

class TestEvents(unittest.TestCase):

    # happy path test add item function 
    def happy_path_test_for_add_item_function(self):
        is_added = False
        Inventorymanagement_with_inventory_csv_file.add_item("cake","blackforest",20,300,"checked in")
        item2 = Inventorymanagement_with_inventory_csv_file.items[-1]
        is_added = True
        if is_added == False:
            self.assertRaises(ValueError)

if __name__ == '__main__':
    unittest.main()
    
