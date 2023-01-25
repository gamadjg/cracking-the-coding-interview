# Implement a method to perform string compression using the counts of repeated characters


def stringCompression(strInput):
    # type check, if strInput not a string, return None
    if type(strInput) != str:
        return None

    # lenght check, if strInput is empty or 1 character, return strInput
    if len(strInput) < 2:
        return strInput

    # whitespace removal
    strInput = strInput.replace(" ", "")

    # loop through string, on every element, add to a charDict if new (=1), else increment counter (+=1)
    charDict = {}
    for val in strInput:
        print(val)
        if val in charDict:
            charDict[val] += 1
        else:
            charDict[val] = 1

    # loop through dict, append the dict key and its value to the return string
    strReturn = ""
    for key in charDict:
        strReturn += key + str(charDict[key])

    # if returnStr length is larger than str, return str
    print(strInput, strReturn)
    if len(strInput) <= len(strReturn):
        return strInput
    return strReturn


def test_stringCompression():
    # not a string
    assert stringCompression([1, 2, 3]) == None
    # empty string
    assert stringCompression("") == ""
    # string too small to compress
    assert stringCompression("a") == "a"
    # no compression available
    assert stringCompression("abc") == "abc"
    # regular compression success
    assert stringCompression("aabbcc") == "aabbcc"
    # string compression with one element type
    assert stringCompression("aaaaaaaa") == "a8"
    # string compression with one element type in the double digits
    assert stringCompression("aaaaaaaaaaaa") == "a12"
    # no string compression with same element in upper and lowercase
    assert stringCompression("aaAA") == "aaAA"
    # string compression with same element in upper and lowercase
    assert stringCompression("aaAAA") == "a2A3"
    # string compression with spaces
    assert stringCompression("aaa bbb") == "a3b3"
