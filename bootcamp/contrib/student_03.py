def calc_gc_content(string):
    """Calculate the GC content of `string`

    Parameters
    ----------
    string : str
        The string to calcualte within

    Returns
    -------
    float
        The GC content of `string`

    """
    count_gc = 0
    string_length = len(string)

    for i in range(string_length):
        if string[i].upper() == 'G' or string[i].upper() == 'C':
            count_gc += 1

    gc_content = count_gc/string_length

    return gc_content
