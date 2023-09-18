def weave(s1, s2):
    # determine the shorter and longer strings
    min_len = min(len(s1), len(s2))

    # weave the two strings together
    result = []
    for i in range(min_len):
        result.append(s1[i])
        result.append(s2[i])

    # append the remaining characters from the longer string
    result.extend(s1[min_len:])
    result.extend(s2[min_len:])

    return ''.join(result)
