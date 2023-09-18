def count_substring(string, substring):
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
    
    dict = {"A":"a", "T":"t", "C":"c", "G":"g"}
    
    for i in range(n_subsequences):
        left_bound = i
        right_bound = i + substring_length
        candidate_substring = string[left_bound:right_bound]
        if candidate_substring == substring:
            count += 1
        else for j in range(substring_length):
            nucleotide = {n for n in dic if dic[subtring[j]]==subtring[j]}
            candidate_substring = can
    return count


