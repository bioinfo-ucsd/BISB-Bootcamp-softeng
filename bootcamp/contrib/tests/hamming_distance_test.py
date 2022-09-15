from bootcamp.contrib.hamming_distance import calc_hamming_distance # noqa


def test_hamming_distance1():
    test_string = "TAG"
    test_string2 = "TAG"

    expected_count = 0
    observed_count = calc_hamming_distance(test_string, test_string2)
    assert expected_count == observed_count


def test_hamming_distance2():
    test_string = "TAC"
    test_string2 = "TAG"

    expected_count = 1
    observed_count = calc_hamming_distance(test_string, test_string2)
    assert expected_count == observed_count


def test_hamming_distance3():
    test_string = "TAGG"
    test_string2 = "TAG"

    expected_count = None
    observed_count = calc_hamming_distance(test_string, test_string2)
    assert expected_count == observed_count
