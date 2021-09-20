import pytest

from binary_search.easy.prime_factorization import Solution

s = Solution()

test_cases = [(12, [2, 2, 3]), (3, [3])]


@pytest.mark.parametrize("n,expected", test_cases)
def test_prime_factorization(n, expected):
    assert s.solve(n) == expected
