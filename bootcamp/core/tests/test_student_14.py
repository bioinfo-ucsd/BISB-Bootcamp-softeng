from bootcamp.core.student_14 import count_substring  # noqa


def test_count_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "TAG"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "AGC"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "AGTCCCCTAGA"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_case_cap():
    test_string = "CGCTAGCGT"
    test_substring = "CGT"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_case_lower():
    test_string = "CGCTAGCGT"
    test_substring = "cgt"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_case_mix():
    test_string = "CGCTAGCGT"
    test_substring = "CgT"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count
