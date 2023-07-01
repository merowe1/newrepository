import unittest
from shop import Shop

class TestShop(unittest.TestCase):

    def setUp(self):
        # Set up the test data
        self.items = {
            'item1': 50,
            'item2': 150,
            'item3': 75
        }
        self.customer_balance = 100
        self.shop = Shop(self.items, self.customer_balance)

    def test_display_items(self):
        # Test that the items are displayed correctly
        expected_output = "Items:\nitem1 - £50\nitem2 - £150\nitem3 - £75\n"
        self.assertEqual(self.shop.display_items(), expected_output)

    def test_valid_purchase(self):
        # Test a valid item purchase
        item = 'item1'
        expected_output = f"Here's your {item}!"
        self.assertEqual(self.shop.purchase_item(item), expected_output)

    def test_insufficient_funds(self):
        # Test a purchase where the customer doesn't have enough funds
        item = 'item2'
        with self.assertRaises(self.shop.InsufficientFundsError):
            self.shop.purchase_item(item)

    def test_invalid_item(self):
        # Test an invalid item selection
        item = 'item4'
        with self.assertRaises(self.shop.InvalidItemError):
            self.shop.purchase_item(item)

    def test_maximum_attempts_reached(self):
        # Test reaching the maximum purchase attempts
        with self.assertRaises(self.shop.MaximumAttemptsReachedError):
            for _ in range(4):
                self.shop.purchase_item('item1')

if __name__ == '__main__':
    unittest.main()
