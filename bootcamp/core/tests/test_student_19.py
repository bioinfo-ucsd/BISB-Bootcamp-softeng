from bootcamp.core.student_19 import count_substring  # noqa


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


def test_count_substring_case_insensitive_lower():
    test_string = 'AGACC'
    test_substring = 'ag'

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_case_insensitive_upper():
    test_string = 'agacc'
    test_substring = 'AG'

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_case_insensitive_mix():
    test_string = 'aGACc'
    test_substring = 'Ag'

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count
