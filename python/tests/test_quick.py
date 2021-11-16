from code_challenges.quick_sort.blog import quickSort


def test_merging():
    #arrange

    l = [8,4,23,42,16,15]
    n = len(l)
    expected = [4,8,15,16,23,42]
    actual = quickSort(l, 0, n-1)
    assert expected == actual

def test_merging_2():
    l = [20,18,12,8,5,-2]
    n = len(l)
    excepted = [-2,5,8,12,18,20]
    actual = quickSort(l, 0, n-1)
    assert excepted == actual

def test_merging_3():
    l = [5,12,7,5,5,7]
    n = len(l)
    excepted = [5,5,5,7,7,12]
    actual = quickSort(l, 0, n-1)
    assert excepted == actual

def test_merging_4():
    l = [2,3,5,7,13,11]
    n = len(l)
    excepted = [2,3,5,7,11,13]
    actual = quickSort(l, 0, n-1)
    assert excepted == actual
