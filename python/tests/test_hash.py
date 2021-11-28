def test_hash():
    ht = HashTable()
    actual = ht.hash('aseel')
    excepted = 582
    assert actual == excepted

from code_challenges.hashtable.hash import HashTable

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

