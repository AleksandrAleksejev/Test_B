import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

def test_unique_sorted_basic():
    assert unique_sorted([3,1,2,2,3]) == [1,2,3]
    assert unique_sorted([]) == []
    assert unique_sorted([5,5,5]) == [5]

def test_count_words_basic():
    text = "tere tere tulemast koju"
    out = count_words(text)
    assert out == {"tere": 2, "tulemast": 1, "koju": 1}

def test_merge_dicts_overwrite_and_original_not_changed():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 20, "c": 3}
    before = d1.copy()
    merged = merge_dicts(d1, d2)
    assert merged == {"a": 1, "b": 20, "c": 3}
    assert d1 == before  # merge shouldn't mutate d1

def test_find_max_pair_empty_and_count():
    with pytest.raises(ValueError):
        find_max_pair([])
    assert find_max_pair([1, 3, 2, 3, 3]) == (3, 3)

def test_flatten_one_level_only():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([[], [5], []]) == [5]
    # only one level flattened: nested deeper should stay nested
    assert flatten([[1, [2]], [[3]]]) == [1, [2], [3]]

def test_read_write_file_tmp(tmp_path):
    p = tmp_path / "test.txt"
    text = "Tere maailm! äöü\n"
    written = write_file(str(p), text)
    # write_file возвращает количество символов, проверим это
    assert written == len(text)
    read = read_file(str(p))
    assert read == text

def test_safe_get_defaults():
    d = {"x": 10}
    assert safe_get(d, "x", 0) == 10
    assert safe_get(d, "y", 5) == 5
    assert safe_get(d, "z") is None

def test_top_n_behaviour_and_errors():
    nums = [5, 1, 3, 5]
    assert top_n(nums, 2) == [5, 5]
    with pytest.raises(ValueError):
        top_n(nums, 0)
    with pytest.raises(ValueError):
        top_n([1, 2], 3)

def test_chunk_list_basic_and_error():
    lst = [1, 2, 3, 4, 5]
    assert chunk_list(lst, 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list(lst, 3) == [[1, 2, 3], [4, 5]]
    with pytest.raises(ValueError):
        chunk_list(lst, 0)
