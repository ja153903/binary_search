from binary_search.easy.rotate_list_left_by_k import Solution

s = Solution()

def test_rotate_list_left_by_k():
    nums = [i for i in range(1, 7)]
    k = 2

    assert s.solve(nums, k) == [3, 4, 5, 6, 1, 2]
    
    k = 6
    assert s.solve(nums, k) == [1, 2, 3, 4, 5, 6]

