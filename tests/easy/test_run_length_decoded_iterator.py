from binary_search.easy.run_length_decoded_iterator import RunLengthDecodedIterator


def test_run_length_decoded_iterator():
    iterator = RunLengthDecodedIterator("2a1b")

    assert iterator.next() == "a"
    assert iterator.next() == "a"
    assert iterator.hasnext() is True
    assert iterator.next() == "b"
    assert iterator.hasnext() is False
