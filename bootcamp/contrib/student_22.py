def sequence_fasta(sequence, name='sequence'):
    """Prints a sequence in fasta format

    Parameters
    ----------
    sequence : str
        The string to count within
    name : str
        The name of your sequence

    Returns
    -------
    str
        The fasta formatted sequence

    """

    fasta = '>' + name + '\n' + sequence + '\n'

    return fasta
