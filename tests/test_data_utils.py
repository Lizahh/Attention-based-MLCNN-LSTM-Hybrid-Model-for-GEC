
import unittest

from fairseq.data import data_utils


class TestDataUtils(unittest.TestCase):

    def test_counting_iterator(self):
        x = list(range(10))
        itr = data_utils.CountingIterator(x)
        self.assertTrue(itr.has_next())
        self.assertEqual(next(itr), 0)
        self.assertEqual(next(itr), 1)
        itr.skip(3)
        self.assertEqual(next(itr), 5)
        itr.skip(3)
        self.assertEqual(next(itr), 9)
        self.assertFalse(itr.has_next())


if __name__ == '__main__':
    unittest.main()
