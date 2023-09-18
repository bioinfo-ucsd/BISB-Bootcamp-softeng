from bootcamp.contrib.student_22 import reverse_comp


def test_reverse_comp():
    string = "ATGCTGT"
    expected_result = "ACAGCAT"

    observed_result = reverse_comp(string)
    assert observed_result == expected_result


def test_empty():
    string = ""
    expected_result = ""

    observed_result = reverse_comp(string)
    assert observed_result == expected_result
