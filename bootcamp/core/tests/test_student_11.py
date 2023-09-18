from bootcamp.core.student_11 import count_substring  # noqa

def test_count_substring_case():
    test_string_caps = "CGCTAGCGT"
    test_sub_caps = "tag"
    test_sub_lows = "TAG"

    capitol_count = count_substring(test_string_caps, test_sub_lows)
    lower_count = count_substring(test_string_caps, test_sub_caps)
    assert capitol_count == lower_count

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
