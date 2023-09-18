from bootcamp.contrib.student_04 import loc_substring  # noqa


def test_loc_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "TAG"

    expected_result = 3
    observed_result = loc_substring(test_string, test_substring)
    assert expected_result == observed_result


def test_loc_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "AGC"

    expected_result = 0
    observed_result = loc_substring(test_string, test_substring)
    assert expected_result == observed_result


def test_loc_substring_none():
    test_string = "AGTCCCCTAGA"
    test_substring = "AAA"

    expected_result = -1
    observed_result = loc_substring(test_string, test_substring)
    assert expected_result == observed_result


def test_loc_substring_insensitive():
    test_string = "AGCTAGCAGT"
    test_substring = "agc"

    expected_result = 0
    observed_result = loc_substring(test_string, test_substring)
    assert expected_result == observed_result
