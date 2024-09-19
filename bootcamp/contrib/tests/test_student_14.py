from bootcamp.contrib.student_14 import getAverageLength # noqa


def test_getAverageLength_diff():
    test_string = "AGTCTG"
    test_string2 = "ATCGTCGGA"

    expected_average = 7.5
    observed_average = getAverageLength(test_string, test_string2)
    assert expected_average == observed_average


def test_getAverageLength_same():
    test_string = "ACT"
    test_string2 = "ACT"

    expected_average = 3
    observed_average = getAverageLength(test_string, test_string2)
    assert expected_average == observed_average


def test_getAverageLength_zero():
    test_string = ""
    test_string2 = ""

    expected_average = 0.0
    observed_average = getAverageLength(test_string, test_string2)
    assert expected_average == observed_average
