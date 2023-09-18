from bootcamp.core.student_05 import count_substring  # noqa


def test_count_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "tag"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "aGCTAGcAGT"
    test_substring = "agc"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "AGTCCCCTAGAa"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count
