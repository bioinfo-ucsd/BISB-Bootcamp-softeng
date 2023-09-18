from bootcamp.contrib.student_19 import dna_seq_one_hot_encode # noqa


def test_encoding_1():
    test_string = "ATcGN"
    expected_output = [[0, 0, 0, 1], [0, 0, 1, 0],
                       [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]

    observed_output = dna_seq_one_hot_encode(test_string)
    assert expected_output == observed_output
