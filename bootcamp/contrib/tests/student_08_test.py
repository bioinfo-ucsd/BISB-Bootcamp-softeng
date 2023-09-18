from bootcamp.contrib.student_08 import weave # noqa


def test_weave_short():
    s1 = "apple"
    s2 = "banana"

    expected_result = "abpapnlaena"
    observed_result = weave(s1, s2)
    assert expected_result == observed_result


def test_weave_long():
    s1 = "refrigerator"
    s2 = "magnificent"

    expected_result = "rmeafgrniigfeircaetnotr"
    observed_result = weave(s1, s2)
    assert expected_result == observed_result
