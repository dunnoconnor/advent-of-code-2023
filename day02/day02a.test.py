import unittest
from day02.day02a import get_possible_games

# open file, read data, split by newline
f = open("day01.sample.txt", "r");
text = f.read();
f.close();

class TestDay01(unittest.TestCase):
    def test_a(self):
        self.assertEqual(get_possible_games(text),8);

if __name__ == '__main__':
    unittest.main()