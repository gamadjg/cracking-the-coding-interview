# Given a String, write a function to check if it's a permutation of a palindrome.


def palindromePermutation(pCheck):
    # if pCheck is not a string, return false
    if type(pCheck) != str:
        return False

    # remove all whitespace/spaces
    pCheck = pCheck.replace(" ", "")

    # if string is 1 character or empty, return false
    if len(pCheck) < 2:
        return False

    # make all elements lowercase
    pCheck = pCheck.lower()

    # pass all elements into a dictionary as keys and count the number of times the element appears as the value
    dict = {}
    for val in pCheck:
        if val in dict:
            dict[val] += 1
        else:
            dict[val] = 1

    # create list of dictionary values
    dictValues = dict.values()

    # at most one value in all dictionary values should be odd, and only by 1
    counter = 0
    for val in dictValues:
        if val % 2 == 1:
            counter += 1
    if counter > 1:
        return False

    return True


def test_palindromePermutation():
    # successful fail, arg not a string
    assert palindromePermutation(123) == False
    # successful fail, arg is not a string
    assert palindromePermutation(["a", "b", "b", "a"]) == False
    # successful fail, arg is empty
    assert palindromePermutation("") == False
    # successful fail, arg empty after whitespace strip
    assert palindromePermutation("   ") == False
    # successful palindrome permutation
    assert palindromePermutation("ab ba") == True
    # successful palindrome permutation
    assert palindromePermutation("Taco cat") == True
