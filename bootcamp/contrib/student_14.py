def getAverageLength(string, string2):
    """ Get the average length of two strings

    Parameters
    ----------
    string : str
        The first string to count
    string2 : str
        The second string to count

    Returns
    -------
    float
        Average of length
    """

    avg = (len(string) + len(string2)) / 2

    return avg
