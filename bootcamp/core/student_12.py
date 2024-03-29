def count_substring(string: str, substring: str) -> int:
    """Counts the number of occurrences of `substring` in `string`

    Parameters
    ----------
    string : str
        The string to count within
    substring : str
        The value to count in string

    Returns
    -------
    int
        The number of times `substring` occurs in `string`

    """
    count = 0

    string_length = len(string)
    substring_length = len(substring)
    n_subsequences = string_length - substring_length + 1
    string_lower = string.lower()
    substring_lower = substring.lower()

    for i in range(n_subsequences):
        left_bound = i
        right_bound = i + substring_length
        candidate_substring = string_lower[left_bound:right_bound]
        if candidate_substring == substring_lower:
            count += 1

    return count
