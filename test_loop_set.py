import unittest.mock

import set_loops as ex1

class TP10SetTest(unittest.TestCase):

    def test_unique_chars(self):
        result1 = ex1.unique_strings("hello")
        self.assertEqual(result1, {'h', 'e', 'l', 'o'})

        result = ex1.unique_strings("")
        self.assertEqual(result, set())


if __name__ == '__main__':
    unittest.main()
