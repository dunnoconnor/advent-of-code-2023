import unittest
from day01.day01b import get_calibration_value
# open file, read data, split by newline
f = open("day01.sampleb.txt", "r");
text = f.read();
f.close();

class TestDay01(unittest.TestCase):
    def test_a(self):
        self.assertEqual(get_calibration_value(text),281)

if __name__ == '__main__':
    unittest.main()