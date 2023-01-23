# Given two strings, write a method to decide if one is a permuation of the other


def checkPermutations(baseStr, checkStr):
    # Check if inputs are both strings
    if type(baseStr) != str or type(checkStr) != str:
        return False

    # trim and strip any whitespace
    baseStr = baseStr.replace(" ", "")
    checkStr = checkStr.replace(" ", "")

    # if lengths of both strings are not the same, strings will cannot be permutations of each other
    if len(baseStr) != len(checkStr):
        return False

    # convert the second string into an enumerated dict, denoting # of each letter
    dict = {}
    for val in checkStr:
        if val in dict:
            dict[val] += 1
        else:
            dict[val] = 1

    # for each letter in in the first string, check to see if there is a letter in the dict
    #   if letter exists, and count is greater than 0,  -1 from letter in dict
    #   else, return False
    for val in baseStr:
        if val in dict:
            if dict[val] >= 1:
                dict[val] -= 1
            else:
                return False
        else:
            return False
    return True


def test_checkPermutations():
    # check whitespace removal before permutation comparison
    assert checkPermutations("abb ac ", "a bbac ") == True
    # check string length differences
    assert checkPermutations("abc", " ") == False
    assert checkPermutations("", "abc") == False
    # check if letters exist in dictionary
    assert checkPermutations("abc", "abd") == False
    # check for type differences
    assert checkPermutations(["a", "b", "d"], "abd") == False
    assert checkPermutations("abd", ["a", "b", "d"]) == False
    # check for successful permutation check
    assert checkPermutations("abbac ", " cbaab ") == True
