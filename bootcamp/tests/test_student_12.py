"""
test_student_12.py
"""
import os
import pytest
from bootcamp.core.student_12 import count_substring

def test_bad_input():
    """
    Tests for a non-string input
    """
    with pytest.raises(Exception) as e_info:
        bigstring = 12338
        substring = "Gd"
        occured = count_substring(bigstring, substring)

def test_all_caps_input():
    """
    tests for an all caps input: AGAGAGAG
    """
    bigstring = "AGAGAGAGAG"
    substring = "AG"
    expected = 5
    occured = count_substring(bigstring, substring)
    assert(expected == occured)
    
    

def test_all_lowercase_input():
    """
    Example input: agagagag
    """
    bigstring = "agagagag"
    substring = "ag"
    expected = 4
    occured = count_substring(bigstring, substring)
    assert(expected == occured)

    
def test_mixed_input():
    """
    Example input: AGagAGAGag
    """
    bigstring = "AGagAGAGag"
    substring = "Ag"
    expected = 5
    occured = count_substring(bigstring, substring)
    assert(expected == occured)
