from binary_search.easy.range_query_on_a_list import RangeSum


def test_range_query_on_a_list():
    rs = RangeSum([1, 2, 5, 0, 3, 7])
    assert rs.total(0, 3) == 8
    assert rs.total(1, 5) == 10
