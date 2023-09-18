def dna_seq_one_hot_encode(seq):
    """
    Given a the DNA sequence,
    return the one hot encoding of that sequence (hardcoded)
    """
    base_dict = {
        "a": [0, 0, 0, 1], "t": [0, 0, 1, 0],
        "c": [0, 1, 0, 0], "g": [1, 0, 0, 0], "n": [0, 0, 0, 0]
    }
    return [base_dict[base] for base in seq.lower()]
