from bootcamp.contrib.student_03 import has_atcg  # noqa


def test_has_atcg():
    test_string = "CGCTAGCGT"

    expected_result = True
    observed_result = has_atcg(test_string)
    assert expected_result == observed_result
