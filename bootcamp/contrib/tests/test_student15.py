from bootcamp.contrib.student_15 import CaseConversion


def test_AllUpper():
    test_string = "CGCTAGCGT"

    expected_output = "cgctagcgt"
    observed_output = CaseConversion(test_string)
    assert expected_output == observed_output


def test_AllLower():
    test_string = "cgctagcgt"

    expected_output = "CGCTAGCGT"
    observed_output = CaseConversion(test_string)
    assert expected_output == observed_output


def test_Mix():
    test_string = "ACtgGtAC"

    expected_output = "acTGgTac"
    observed_output = CaseConversion(test_string)
    assert expected_output == observed_output
