from day07b import get_winnings,get_hand_value,card_counter,card_valuer

def test_card_valuer():
    assert card_valuer('2') == '02', "Test 2 failed"
    assert card_valuer('3') == '03', "Test 3 failed"
    assert card_valuer('4') == '04', "Test 4 failed"
    assert card_valuer('5') == '05', "Test 5 failed"
    assert card_valuer('6') == '06', "Test 6 failed"
    assert card_valuer('7') == '07', "Test 7 failed"
    assert card_valuer('8') == '08', "Test 8 failed"
    assert card_valuer('9') == '09', "Test 9 failed"
    assert card_valuer('T') == '10', "Test T failed"
    assert card_valuer('J') == '01', "Test J failed"
    assert card_valuer('Q') == '12', "Test Q failed"
    assert card_valuer('K') == '13', "Test K failed"
    assert card_valuer('A') == '14', "Test A failed"
    print("card_valuer() tests pass")

def test_card_counter():
    assert card_counter('AJJJJ') == '7', "Test 5ofk failed"
    assert card_counter('AJJJK') == '6', "Test 40fk failed"
    assert card_counter('AAJKK') == '5', "Test fullhouse failed"
    assert card_counter('AAJKQ') == '4', "Test 3ofk failed"
    assert card_counter('AAKKQ') == '3', "Test 2p failed"
    assert card_counter('AJKQT') == '2', "Test 1p failed"
    assert card_counter('AKQT9') == '1', "Test 1 failed"
    print("card_counter() tests pass")

def test_hand_value():
    assert get_hand_value('AAAAA') == 71414141414, "Test 5ofk failed"
    assert get_hand_value('AAAAK') == 61414141413, "Test 40fk failed"
    assert get_hand_value('AAAKK') == 51414141313, "Test fullhouse failed"
    assert get_hand_value('AAAKQ') == 41414141312, "Test 3ofk failed"
    assert get_hand_value('AAKKQ') == 31414131312, "Test 2p failed"
    assert get_hand_value('AAKQT') == 21414131210, "Test 1p failed"
    assert get_hand_value('AKQT9') == 11413121009, "Test 1 failed"

test_card_valuer();
test_card_counter();
test_hand_value();