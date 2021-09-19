from binary_search.easy.generate_primes import Solution

s = Solution()

def test_generate_primes_small_case():
    assert s.solve(3) == [2, 3]

def test_generate_primes_medium_case():
    assert s.solve(10) == [2, 3, 5, 7]

def test_generate_primes_large_case():
    assert s.solve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
