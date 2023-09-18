def CaseConversion(string):
    """
    Change Upper Case to Lower Case; Vise versa
    """
    CaseDict = {
        'a': 'A', 'c': 'C', 'g': 'G', 't': 'T',
        'A': 'a', 'C': 'c', 'G': 'g', 'T': 't'
    }
    conversionString = ''
    for base in string:
        conversionString = conversionString + CaseDict[base]
    return conversionString
