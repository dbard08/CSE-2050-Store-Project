import unittest
from customer import Customer
from linked_list import LinkedList
from order import Order
from order_queue import OrderQueue
from product import Product
from stack import Stack
from store import Store


class TestOrder(unittest.TestCase):
    def test_order_creation_and_status(self):
        customer = Customer("C1", "Noah")
        p1 = Product("P1", "Item A", 10.0)
        order = Order("O1", customer, [p1])

        self.assertEqual(order.get_id(), "O1")
        self.assertEqual(order.get_customer().get_name(), "Noah")
        self.assertEqual(order.get_status(), "PENDING")
        order.set_status("COMPLETED")
        self.assertEqual(order.get_status(), "COMPLETED")

    def test_order_total_and_cart_independence(self):
        customer = Customer("C1", "Noah")
        p1 = Product("P1", "Item A", 15.50)
        p2 = Product("P2", "Item B", 24.50)
        items = [p1, p2]

        order = Order("O1", customer, items)
        self.assertAlmostEqual(order.calculate_total(), 40.0)

        items.append(Product("P3", "Item C", 5.0))
        self.assertEqual(len(order.get_items()), 2)
        self.assertAlmostEqual(order.calculate_total(), 40.0)


class TestLinkedList(unittest.TestCase):
    def test_add_first(self):
        ll = LinkedList()
        ll.add_first("A")
        ll.add_first("B")
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.get_first(), "B")

    def test_add_last(self):
        ll = LinkedList()
        ll.add_last("A")
        ll.add_last("B")
        self.assertEqual(ll.size(), 2)
        self.assertEqual(ll.get_first(), "A")

    def test_remove_first(self):
        ll = LinkedList()
        ll.add_last("A")
        ll.add_last("B")
        self.assertEqual(ll.remove_first(), "A")
        self.assertEqual(ll.remove_first(), "B")
        self.assertIsNone(ll.remove_first())
        self.assertTrue(ll.is_empty())

    def test_empty_first_and_size_behavior(self):
        ll = LinkedList()
        self.assertTrue(ll.is_empty())
        self.assertEqual(ll.size(), 0)
        self.assertIsNone(ll.get_first())
        self.assertIsNone(ll.remove_first())


class TestStack(unittest.TestCase):
    def test_lifo_order(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)

    def test_peek(self):
        stack = Stack()
        stack.push("X")
        self.assertEqual(stack.peek(), "X")
        self.assertEqual(stack.size(), 1)
        self.assertFalse(stack.is_empty())

    def test_empty_pop(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertIsNone(stack.pop())
        self.assertIsNone(stack.peek())


class TestOrderQueue(unittest.TestCase):
    def test_fifo_order(self):
        q = OrderQueue()
        q.enqueue("First")
        q.enqueue("Second")
        self.assertEqual(q.dequeue(), "First")
        self.assertEqual(q.dequeue(), "Second")

    def test_peek(self):
        q = OrderQueue()
        q.enqueue("Item")
        self.assertEqual(q.peek(), "Item")
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())

    def test_empty_dequeue(self):
        q = OrderQueue()
        self.assertTrue(q.is_empty())
        self.assertIsNone(q.dequeue())
        self.assertIsNone(q.peek())


class TestStoreIntegration(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.cust = Customer("C1", "Noah")
        self.prod = Product("P1", "Item 1", 20.0)
        self.store.add_customer(self.cust)
        self.store.add_product(self.prod)

    def test_checkout_workflow(self):
        self.cust.get_cart().add_product(self.prod)
        order = self.store.checkout("C1")
        self.assertIsNotNone(order)
        self.assertEqual(order.get_id(), "O1")
        self.assertTrue(self.cust.get_cart().is_empty())
        self.assertEqual(len(self.store.get_orders()), 1)
        self.assertEqual(self.store.find_order("O1"), order)

    def test_processing_workflow(self):
        self.cust.get_cart().add_product(self.prod)
        self.store.checkout("C1")
        processed = self.store.process_next_order()
        self.assertIsNotNone(processed)
        self.assertEqual(processed.get_status(), "PROCESSING")
        self.assertIsNone(self.store.process_next_order())

    def test_order_history_ordering_and_persistence(self):
        cust2 = Customer("C2", "Alex")
        self.store.add_customer(cust2)

        self.cust.get_cart().add_product(self.prod)
        cust2.get_cart().add_product(self.prod)

        o1 = self.store.checkout("C1")
        o2 = self.store.checkout("C2")

        self.store.process_next_order()
        self.store.process_next_order()

        history = self.store.get_order_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].get_id(), o2.get_id())
        self.assertEqual(history[1].get_id(), o1.get_id())
        self.assertEqual(len(self.store.get_order_history()), 2)


if __name__ == "__main__":
    unittest.main()
