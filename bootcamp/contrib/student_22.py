def reverse_comp(string):
    result = ""
    for c in string[::-1]:
        if c == "A" or c == 'a':
            result += "T"
        elif c == "C" or c == 'c':
            result += "G"
        elif c == "G" or c == "g":
            result += "C"
        elif c == "T" or c == "t":
            result += "A"
        else:
            result += "N"
    return result
