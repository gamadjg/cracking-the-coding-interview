# Given two strings, write a function to check if they are at most, one edit away (inserting, removing, replacing a char)


def oneWay(baseStr, checkStr):
    # check for empty arguments, if empty, return false
    # check type, if baseStr or checkStr aren't strings, return false
    # length check, if baseStr and checkStr aren't at most 1 character length diff, return false
    # if length check succeeded, now check to make sure multiple characters weren't edited

    # replacement: loop through characters in both strings, count how many were different (strings are the same length)

    # removal: loop through the smallest string,
    return True


def test_oneWay():
    # empty base and check string
    assert oneWay("", "abc") == False
    assert oneWay("abc", "") == False

    # non-string inputs
    assert oneWay(["abc"], "abc") == False
    assert oneWay(123, "abc") == False

    # # one character replacement
    # assert oneWay("abc", "abd") == True
    # # one character removal
    # assert oneWay("abc", "ab") == True
    # # one character insertion
    # assert oneWay("abc", "abcd") == True

    # # multiple character replacement, fail
    # assert oneWay("abc", "axy") == False
    # # multiple character replacement, same characters, different order, fail
    # assert oneWay("abc", "bca") == False
    # # multiple character removal, fail
    # assert oneWay("abc", "a") == False
    # # multiple character insertion, fail
    # assert oneWay("abc", "abcde") == False

    # # multi-case failure: insert + replacement
    # assert oneWay("abc", "axcd") == False
    # # multi-case failure: removal + replacement
    # assert oneWay("abc", "ax")
