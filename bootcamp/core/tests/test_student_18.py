from bootcamp.core.student_18 import count_substring  # noqa
from bootcamp.contrib.student_18 import count_substring_but_i_express_pain


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


def test_count_substring_case_insensitive():
    test_string = "AGTCCCCTAGA"
    test_substring_upper = "CCC"
    test_substring_lower = "ccc"

    expected_count = 2
    count_upper = count_substring(test_string, test_substring_upper)
    count_lower = count_substring(test_string, test_substring_lower)
    assert expected_count == count_upper and expected_count == count_lower
    
def make_it_hurt():
    test_string = "AGTCCCCTAGA"
    test_substring_lower = "ccc"
    expected_ouch = "GAH"
    assert count_substring_but_i_express_pain(test_string, test_substring) == expected_ouch
