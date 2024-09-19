def get_complement(string):
    """Reverse complements the DNA string input

    Parameters
    ----------
    string : str
        The DNA string to reverse complement

    Returns
    -------
    string_reverse
        The reverse complement of the DNA string

    """
    string = string.upper()
    rev_dna = string[::-1]
    dna_dict = {"A": "T", "G": "C", "C": "G", "T": "A"}
    string_reverse = ''.join([dna_dict[x] for x in rev_dna if x in dna_dict])
    return string_reverse
