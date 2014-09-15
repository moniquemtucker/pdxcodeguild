__author__ = 'Monique Tucker'

import unittest
from test_pairstest import look_for_pairs

class MyTestCase(unittest.TestCase):
    def test_successful_pairs_match(self):
        self.assertTrue(look_for_pairs([2, 5]))


if __name__ == '__main__':
    unittest.main()
