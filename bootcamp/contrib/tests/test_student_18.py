from bootcamp.contrib.student_18 import hamming_distance


def test_hamming_distance_zero():
    string1 = "ACGT"
    string2 = "ACGT"

    expected_count = 0
    observed_count = hamming_distance(string1, string2)
    assert expected_count == observed_count


def test_hamming_distance_one():
    string1 = "ACGT"
    string2 = "ACGA"

    expected_count = 1
    observed_count = hamming_distance(string1, string2)
    assert expected_count == observed_count
