import unittest
from day04.day04a import sum_values
from readfile import read_file
from Card import Card

class TestCard(unittest.TestCase):
    def test_init(self):
        test_card = Card(1,[41,48,83,86,17],[83,86,6,31,17,9,48,53])
        self.assertEqual(test_card.id,1)
        self.assertEqual(test_card.wins,4)
        self.assertEqual(test_card.value,8)

class TestDay04(unittest.TestCase):
    def test_sum_values(self):
        text = read_file("day04.sample.txt");
        self.assertEqual(sum_values(text),13)

if __name__ == '__main__':
    unittest.main()