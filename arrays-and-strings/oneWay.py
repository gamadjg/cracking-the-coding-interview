# Given two strings, write a function to check if they are at most, one edit away (inserting, removing, replacing a char)


def oneWay(baseStr, checkStr):
    # type check, if baseStr or checkStr aren't strings, return False
    if type(baseStr) != str or type(checkStr) != str:
        return False

    # length check, if baseStr and checkStr aren't at most 1 character length diff, return False (empty strings count)
    if len(baseStr) > len(checkStr) + 1 or len(baseStr) < len(checkStr) - 1:
        return False

    # find the smaller of the two strings to loop through
    smallerStr = len(baseStr) if len(baseStr) < len(checkStr) else len(checkStr)

    # count how many characters are different if there are any
    diffCount = 0
    for i in range(smallerStr):
        if baseStr[i] != checkStr[i]:
            diffCount += 1

    # different lengths, indicating insertion or removal, but there are also character differences, return False
    if len(baseStr) != len(checkStr) and diffCount > 0:
        return False

    # same length, more than one replacement or no replacements, return False
    if len(baseStr) == len(checkStr) and (diffCount > 1 or diffCount == 0):
        return False

    return True


def test_oneWay():

    # non-string inputs
    assert oneWay(["abc"], "abc") == False
    assert oneWay(123, "abc") == False

    # empty base or check string
    assert oneWay("", "abc") == False
    assert oneWay("abc", "") == False

    # nothing was changed between both strings, fail
    assert oneWay("abc", "abc") == False

    # one character replacement
    assert oneWay("abc", "abd") == True
    # one character removal
    assert oneWay("abc", "ab") == True
    # one character removal with empty strings
    assert oneWay("a", "") == True
    # one character insertion
    assert oneWay("abc", "abcd") == True
    # one character insertion with empty strings
    assert oneWay("", "a") == True

    # multiple character replacement, fail
    assert oneWay("abc", "axy") == False
    # multiple character replacement, same characters, different order, fail
    assert oneWay("abc", "bca") == False
    # multiple character removal, fail
    assert oneWay("abc", "a") == False
    # multiple character insertion, fail
    assert oneWay("abc", "abcde") == False

    # multi-case failure: insert + replacement
    assert oneWay("abc", "axcd") == False
    # multi-case failure: removal + replacement
    assert oneWay("abc", "ax") == False
