import unittest


from product import Product
from store import Store
from algorithms import merge_sort, quick_sort, quick_select
from entry import Entry 
from hash_mapping import HashMapping 

class TestMergeSort(unittest.TestCase): #groups our merge sort test together 
    def test_empty_list(self): #testing for empty list 
        products = []
        merge_sort(products)
        self.assertEqual(products,[])

    def test_reverse_order(self):
        products = [
            Product("P300", "Mouse", 20.00),
            Product("P200", "Keyboard", 30.00),
            Product("P100", "Headphones", 39.99)
        ]
        merge_sort(products)
        self.asserEqual(
            [p.get_id() for p in products],
            ["P100","P200","P300"]
        )

    def test_duplicate_ids(self):
        products = [
            ("P200", "Mouse", 20.00), 
            ("P100", "Headphones", 39.99),
            ("P100", "Monitor", 40.00)
        ]
        merge_sort(products)

        self.assertEqual(
            [p.get_id() for p in products],
            ["P200", "P100", "P100"]
        )

    class TestQuickSort(unittest.TestCase):
        def test_empty_list(self):
            products = []
            quick_sort(products)
            self.assertEqual(products, [])

        def test_already_sorted(self):
            products = [
                Product("P100", "Mouse", 20.00),
                Product("P200", "Keyboard", 30.00),
                Product("P300", "Headphones", 39.99)
            ]

            quick_sort(products)
            self.assertEqual(
                [p.get_id() for p in products],
                ["P100", "P200","P300"]
            )

        def test_reverse_order(self):
            products = [
                Product("P300", "Mouse", 20.00),
                Product("P200", "Keyboard", 30.00),
                Product("P100", "Headphones", 39.99)
            ]

            quick_sort(products)
            self.assertEqual(
                [p.get_id() for p in products],
                ["P100","P200","P300"]
            )
class TestQuickSelect(unittest.TestCase):
    def test_first_rank(self):
        products = [
            Product("P300", "Mouse", 20.00),
            Product("P200", "Keyboard", 30.00),
            Product("P100", "Headphones", 39.99)
        ]

        result = quick_select(products, 1)
        self.assertEqual(result.get_id(), "P100")

        def test_middle_rank(self):
            products = [
                Product("P300", "Mouse", 20.00),
                Product("P200", "Keyboard", 30.00),
                Product("P100", "Headphones", 39.99)   
            ]
            quick_select(products, 2)
            self.assertEqual(result.get_id(), "P200")

            def test_invalid_rank(self):
                products = [
                    Product("P100", "Keyboard", 30.00),
                    Product("P200", "Headphones", 39.99)
                ]
                result = quick_select(products, 0)
                self.assertIsNone(result)
class TestHashMapping(unittest.TestCase):
    def test_put_and_get(self):
        mapping = HashMapping(size = 3)
        mapping.put("P100", "Keyboard")

        self.asserEqual(mapping.get("P100"), "Keyboard")
        self.assertEqual(len(mapping), 1)

    def test_update_existing_key(self):
        mapping = HashMapping(size = 3)

        mapping.put("P100", "Keyboard")
        mapping.put("P100", "Wireless Keyboard")

        self.assertEqual(mapping.get("P100"), "Wireless Keyboard")
        self.assertEqual(len(mapping), 1)

    def test_rehash_perserves_entries(self):
        mapping = HashMapping( size = 2)
        mapping.put("P100", "Keyboard")
        mapping.put("P200", "Mouse")
        mapping.put("P300", "Monitor")

        mapping.rehash()

        self.assertEqual(mapping.get("P100"), "Keyboard")
        self.assertEqual(mapping.get("P200"), "Mouse")
        self.assertEqual(mapping.get("P300"), "Monitor")

   

class TestStoreIntegration(unittest.TestCase):
    def test_merge_sort_products(self):
        store = Store()
        store.add_product(Product("P300", "Mouse", 20.00))
        store.add_product(Product("P100", "Keyboard", 30.00))
        store.add_product(Product("P200", "Monitor", 40.00))
        store.merge_sort_products()

        self.assertEqual(
            [p.get_id() for p in store.products],
            ["P100", "P200", "P300"]
        )

    def test_quick_select_products(self):
        store = Store()

        store.add_product(Product("P300", "Mouse", 20.00))
        store.add_product(Product("P100", "Keyboard", 30.00))
        store.add_product(Product("P200", "Monitor", 40.00))
        result = store.quick_select_product(2)

        self.assertEqual(result.get_id(),"P200")

    def test_find_product(self):
        store = Store()

        keyboard = Product("P100", "Keyobard", 30.00)
        store.add_product(keyboard)

        result = store.find_product("P100")

        self.assertIs(result, keyboard)
        self.assertIsNone(store.find_product("P999"))







        




        



    


