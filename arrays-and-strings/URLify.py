"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
    has sufficient space at the end to hold sufficient characters, and that you are given the "true"
    length of the string. 
    
Example: 
    Input: "Mr John Smith     ", 13
    Output: "Mr%20John%20Smith"
"""


def urlify(str):
    # strip the outside whitespace
    str = str.strip()

    # if string is empty ("") or 1 character "a", return str
    if len(str) < 2:
        return str

    # split the string into a list on whitespace
    splitList = str.split()

    # if initial string length was >1 but no spaces were found in between any characters, we only have 1 str in the list
    if len(splitList) < 2:
        return splitList[0]

    # define returnStr with first element in the splitList
    returnStr = splitList[0]

    # for every val in the list, rejoin back into a string while concatenating '%20' in between each val
    for index in range(1, len(splitList)):
        returnStr += "%20" + splitList[index]

    return returnStr


def test_urlify():
    # string is empty and length 0 after split
    assert urlify("  ") == ""
    # if string is a single character, no spaces exists, therefore return string
    assert urlify(" a ") == "a"
    # after strip and split, splitList only has 1 element with no spaces
    assert urlify(" aaa ") == "aaa"
    # successful url conversion
    assert urlify(" url test ") == "url%20test"
    # successful url conversion with numbers
    assert urlify(" url test  2 ") == "url%20test%202"
