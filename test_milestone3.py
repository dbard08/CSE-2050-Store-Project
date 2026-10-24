import unittest
from product import Product
from store import Store
from algorithms import selection_sort, insertion_sort, binary_search


def make_products(ids):
    """Build a list of Product objects from a list of ID strings."""
    return [Product(pid, "Item " + pid, 10.0) for pid in ids]


def get_ids(products):
    """Return just the ID strings from a list of Products."""
    return [p.get_id() for p in products]


class TestSorting(unittest.TestCase):
    def test_selection_sort_reverse(self):
        items = make_products(["P3", "P2", "P1"])
        selection_sort(items)
        self.assertEqual(get_ids(items), ["P1", "P2", "P3"])

    def test_selection_sort_empty(self):
        items = []
        selection_sort(items)
        self.assertEqual(items, [])

    def test_insertion_sort_reverse(self):
        items = make_products(["P3", "P2", "P1"])
        insertion_sort(items)
        self.assertEqual(get_ids(items), ["P1", "P2", "P3"])

    def test_insertion_sort_already_sorted(self):
        items = make_products(["P1", "P2", "P3"])
        insertion_sort(items)
        self.assertEqual(get_ids(items), ["P1", "P2", "P3"])


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.items = make_products(["P1", "P2", "P3", "P4", "P5"])

    def test_first_item(self):
        self.assertEqual(binary_search(self.items, "P1"), 0)

    def test_middle_item(self):
        self.assertEqual(binary_search(self.items, "P3"), 2)

    def test_not_found(self):
        self.assertEqual(binary_search(self.items, "P9"), -1)


class TestStoreSortAndSearch(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.store.add_product(Product("P300", "Mouse", 29.99))
        self.store.add_product(Product("P100", "Keyboard", 59.99))
        self.store.add_product(Product("P200", "Headphones", 39.99))

    def test_sort_integration(self):
        self.store.insertion_sort_products()
        self.assertEqual(get_ids(self.store.products), ["P100", "P200", "P300"])

    def test_binary_lookup(self):
        self.store.insertion_sort_products()
        product = self.store.binary_search_product("P200")
        self.assertEqual(product.get_name(), "Headphones")


if __name__ == "__main__":
    unittest.main()