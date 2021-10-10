def reverse_list(ll):
    """Reverses a linked list
    Args:
        ll: linked list
    Returns:
        linked list in reversed form
    """
    # put your function implementation here


# def array_everse(ll):

#     return ll


# ll = [1, 2, 3, 4, 5, 6]
# for i in range(len(ll)-1, -1, -1):
#     print(ll[i]),

def array_everse(ll):
    arr = []
    for i in ll:
        arr.insert(0, i)
    return arr


print(array_everse([1, 2, 3, 4]))


def rev(ll):
    return ll[::-1]
