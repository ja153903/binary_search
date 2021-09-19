import pytest

from binary_search.easy.largest_number_by_two_times import Solution

s = Solution()


@pytest.fixture
def failing_test_case():
    return [3, 6, 9]


@pytest.fixture
def passing_test_case():
    return [3, 6, 15]


@pytest.fixture
def failing_test_case_with_equal_value():
    return [3, 6, 12]


@pytest.fixture
def tricky_edge_case():
    return [0, 0]


def test_largest_number_by_two_times_fails_with_basic_case(failing_test_case):
    assert s.solve(failing_test_case) is False


def test_largest_number_by_two_times_passes_with_basic_case(passing_test_case):
    assert s.solve(passing_test_case) is True


def test_largest_number_by_two_times_fails_with_equal_case(failing_test_case_with_equal_value):
    assert s.solve(failing_test_case_with_equal_value) is False


def test_largest_number_by_two_times_fails_with_edge_case(tricky_edge_case):
    assert s.solve(tricky_edge_case) is False
