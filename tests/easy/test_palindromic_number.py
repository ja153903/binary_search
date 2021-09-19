import pytest

from binary_search.easy.palindromic_number import Solution

@pytest.fixture
def palindromic_number():
    return 121

@pytest.fixture
def large_palindromic_number():
    return 20200202

@pytest.fixture
def non_palindromic_number():
    return 43

s = Solution()

def test_small_palindromic_number(palindromic_number):
    assert s.solve(palindromic_number) is True

def test_large_palindromic_number(large_palindromic_number):
    assert s.solve(large_palindromic_number) is True

def test_non_palindromic_number(non_palindromic_number):
    assert s.solve(non_palindromic_number) is False
