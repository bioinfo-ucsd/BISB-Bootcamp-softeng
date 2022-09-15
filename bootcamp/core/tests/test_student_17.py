from bootcamp.core.student_17 import count_substring  # noqa


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


def test_count_substring_not_case_sensitive():
    test_string1 = "AGCTAGCAGT"
    test_substring1 = "AGC"

    test_string2 = "AGCTAGCAGT"
    test_substring2 = "agc"

    expected_count1 = 2
    expected_count2 = 2

    observed_count1 = count_substring(test_string1, test_substring1)
    observed_count2 = count_substring(test_string2, test_substring2)

    assert observed_count1 == observed_count2
    assert observed_count1 == expected_count1
    assert observed_count2 == expected_count2
