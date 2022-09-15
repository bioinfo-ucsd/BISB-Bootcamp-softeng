def hamming_distance(string1, string2):
    """Counts the Hamming Distance between `string1` and `string2`.
    The Hamming Distance is the number of different nucleotides
    between the two strings.

    Parameters
    ----------
    string1: str
        The first string to compare
    string2: str
        The second string to compare

    Returns
    ----------
    int
        The Hamming Distance between `string1` and `string2`


    """
    h_distance = 0
    string_length = len(string1)

    for i in range(string_length):
        if string1[i] != string2[i]:
            h_distance += 1

    return h_distance
