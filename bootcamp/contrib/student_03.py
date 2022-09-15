def has_atcg(string):
    """Check if `string` contains all 4 different letters

    Parameters
    ----------
    string : str
        The string to count within

    Returns
    -------
    bool
        Return if `string` contains all 4 different letters

    """
    string = string.upper()

    for i in ['A', 'T', 'C', 'G']:
        if i not in string:
            return False

    return True
