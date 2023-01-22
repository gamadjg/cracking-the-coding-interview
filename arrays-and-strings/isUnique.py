"""
1. Is Unique: Implement an algorithm to determine if a string has all unique characters. 
Can this be completed in-place, without additional data structures?
"""


def isUnique(arg):
    if len(arg) < 1:
        return False

    dict = {}
    for index in range(len(arg)):
        if arg[index] in dict:
            return False
        dict[arg[index]] = arg[index]
    return True


def isUnique2(lst):
    if len(lst) < 1:
        return False

    list(lst).sort()
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return False
    return True


def test_isUnique():
    assert isUnique("abb") == False
    assert isUnique("abba") == False
    assert isUnique("") == False
    assert isUnique("abc") == True


def test_isUnique2():
    assert isUnique2("abb") == False
    assert isUnique2("ab") == True
    assert isUnique2("abc123?!") == True
