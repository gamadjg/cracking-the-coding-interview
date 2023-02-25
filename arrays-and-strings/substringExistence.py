# Check to see if case-sensitive substring exists within a string
def count_substring(string, sub_string):
    subCount = 0
    # Loop through base string
    for i in range(len(string) - len(sub_string)):
        # Check to see if the first character in the sub_string matches
        if string[i] == sub_string[0]:
            for j in range(len(sub_string)):
                if sub_string[j] != string[i + j]:
                    break
                else:
                    subCount += 1
            if subCount == len(sub_string):
                return i
            else:
                subCount = 0
    return False

    # # Loop through base string
    # while i < len(string):
    #     # Check to see if the first character in the sub_string matches
    #     if string[i] == sub_string[0]:
    #         # if the i + len of sub_string is less than len(string)
    #         if i + len(sub_string) <= len(string):

    #             for j in range(len(sub_string)):
    #                 # print(string[i + j], sub_string[j])
    #                 if sub_string[j] == string[i + j]:
    #                     subLen += 1
    #                 else:
    #                     break
    #             if subLen == len(sub_string):
    #                 count += 1
    #             subLen = 0
    #         else:
    #             return count
    #     # else:
    #     #     print(string[i])
    #     i += 1
    return count


print(count_substring("I am birtt Hispanic, by birth.", "birth"))
