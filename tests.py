import unittest
from main import to_upper


class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Ritesh"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "RITESH dev1")


if __name__ == '__main__':
    unittest.main()