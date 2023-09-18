def loc_substring(string, substring):
    """Locates, if any, the first occurrence of `substring` in `string`

    Parameters
    ----------
    string : str
        The string to locate substring within it
    substring : str
        The value to locate in string

    Returns
    -------
    int
        The first location of `substring` in `string`

    """
    string = string.lower()
    substring = substring.lower()

    string_length = len(string)
    substring_length = len(substring)
    n_subsequences = string_length - substring_length + 1

    for i in range(n_subsequences):
        left_bound = i
        right_bound = i + substring_length
        candidate_substring = string[left_bound:right_bound]
        if candidate_substring == substring:
            return i

    return -1
