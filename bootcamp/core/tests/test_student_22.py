from bootcamp.core.student_22 import count_substring  # noqa
from bootcamp.contrib.student_22 import sequence_fasta


def test_count_substring_single():
    test_string = "CgCtAGCGt"
    test_substring = "TAG"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "agc"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "agtcccctaga"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_fasta_fun():
    test_string = "agtcccctaga"
    test_name = "test1"

    expected_out = ">test1\nagtcccctaga\n"
    observed_out = sequence_fasta(sequence=test_string, name=test_name)
    assert expected_out == observed_out
