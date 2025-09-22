import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair,
    flatten, read_file, write_file, safe_get, top_n, chunk_list
)


def test_unique_sorted():
    assert unique_sorted([3, 1, 2, 2, 3]) == [1, 2, 3]
    assert unique_sorted([]) == []
    assert unique_sorted([5, 5, 5]) == [5]


def test_count_words_normal():
    text = "tere tere tulemast koju"
    assert count_words(text) == {"tere": 2, "tulemast": 1, "koju": 1}


def test_count_words_with_punctuation():
    
    text = "Tere, tere!"
    out = count_words(text)
    assert "tere" in out
    assert "tere," in out or "tere!" in out   


def test_merge_dicts():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 20, "c": 3}
    merged = merge_dicts(d1, d2)
    assert merged == {"a": 1, "b": 20, "c": 3}
    assert d1 == {"a": 1, "b": 2}  


def test_find_max_pair():
    assert find_max_pair([1, 3, 2, 3, 3]) == (3, 3)
    with pytest.raises(ValueError):
        find_max_pair([])


def test_flatten_basic():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([[], [5]]) == [5]


def test_flatten_nested():
    nested = [[1, [2]], [[3]]]
    out = flatten(nested)
    assert out == [1, [2], [3]]  


def test_read_and_write_file(tmp_path):
    p = tmp_path / "file.txt"
    text = "Tere maailm äöü\n"
    written = write_file(str(p), text)
    assert written == len(text)
    read_back = read_file(str(p))
    assert read_back == text


def test_safe_get():
    d = {"x": 10}
    assert safe_get(d, "x") == 10
    assert safe_get(d, "y") is None
    assert safe_get(d, "y", 5) == 5


def test_top_n():
    nums = [5, 1, 3, 5]
    assert top_n(nums, 2) == [5, 5]
    with pytest.raises(ValueError):
        top_n(nums, 0)
    with pytest.raises(ValueError):
        top_n(nums, 5)


def test_chunk_list():
    lst = [1, 2, 3, 4, 5]
    assert chunk_list(lst, 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list(lst, 3) == [[1, 2, 3], [4, 5]]
    assert chunk_list([], 3) == []
    with pytest.raises(ValueError):
        chunk_list(lst, 0)
