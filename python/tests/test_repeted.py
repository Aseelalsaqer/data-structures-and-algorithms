from code_challenges.hashmap_repeated_word.code import HashTable ,repeated_word

def test_instantiate_hashmap():
    hashmap = HashTable()
    assert hashmap

def test_empty_string():
    string = ''
    actual = repeated_word(string)
    assert actual == None

def test_no_repeat():
    string = "asel"
    actual = repeated_word(string)
    assert actual == None
