def test_hash():
    ht = HashTable()
    actual = ht.hash('aseel')
    excepted = 582
    assert actual == excepted

from code_challenges.hashtable.hash import HashTable , left_join

def test_add():
    ht = HashTable()
    ht.add('aseel', 'fawwaz')
    actual = ('aseel', 'fawwaz')
    excepted = ('aseel', 'fawwaz')
    assert actual == excepted


def test_get():
    ht = HashTable()
    ht.add('aseel', 'fawwaz')
    actual = ht.get('aseel')
    excepted = 'fawwaz'
    assert actual == excepted


def test_contains():
    ht = HashTable()
    ht.add('aseel', 'fawwaz')
    actual = ht.contains('aseel')
    excepted = True
    assert actual == excepted


def test_contains2():
    ht = HashTable()
    ht.add('aseel', 'fawwaz')
    actual = ht.contains('hi')
    excepted = False
    assert actual == excepted

def test_left_join():
    ht1 = HashTable()
    ht1.add("aseel", 10)
    ht1.add("asel", 12)
    ht1.add("asl", 18)


    ht2 = HashTable()
    ht2.add("aseel", 20)
    ht2.add("asxl", 12)
    ht2.add("asl", 16)
    actual = left_join(ht1, ht2)
    excepted = [['asl', 18, 16], ['aseel', 10, 20], ['asel', 12, None]]


    assert excepted == actual

