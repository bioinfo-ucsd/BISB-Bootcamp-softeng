from bootcamp.contrib.student_17 import do_something


def test_function_when_same():
    input_1 = 1
    input_2 = 1

    expected_result = 'Danny'
    observed_result = do_something(input_1, input_2)
    assert expected_result == observed_result


def test_function_when_different():
    input_1 = '1'
    input_2 = 1

    expected_result = 'DeVito'
    observed_result = do_something(input_1, input_2)
    assert expected_result == observed_result
