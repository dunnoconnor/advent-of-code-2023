from day04a import sum_values
from readfile import read_file
from Card import Card

def test_card():
    test_card = Card(1,[41,48,83,86,17],[83,86,6,31,17,9,48,53])
    assert test_card.id == 1, "Should be 1"
    assert test_card.wins == 4, "Should be 4"
    assert test_card.value == 8, "Should be 8"

def test_sum_values():
        text = read_file("day04.sample.txt");
        assert sum_values(text) == 13, "Should be 13"

if __name__ == "__main__":
    test_card()
    test_sum_values()
    print("Everything passed")