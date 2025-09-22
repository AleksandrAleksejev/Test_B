import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_unique_sorted_basic():
    """Test unikaalsete sorteeritud arvude funktsiooni."""
    assert unique_sorted([3,1,2,2,3]) == [1,2,3]
    assert unique_sorted([]) == []
    assert unique_sorted([5,5,5]) == [5]

def test_count_words_basic():
    """Test sõnade loendamise funktsiooni."""
    text = "tere tere tulemast koju"
    out = count_words(text)
    assert out == {"tere": 2, "tulemast": 1, "koju": 1}

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!

def test_merge_dicts_basic():
    """Test merge_dicts: d2 väärtused varjutavad d1 omad ja d1 ei muutu"""
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 20, "c": 3}
    merged = merge_dicts(d1, d2)
    assert merged == {"a": 1, "b": 20, "c": 3}
    assert d1 == {"a": 1, "b": 2}  
def test_find_max_pair_normal_and_empty():
    """Test find_max_pair: õige maksimaalse väärtuse ja korduste arv"""
    assert find_max_pair([1, 3, 2, 3, 3]) == (3, 3)
    assert find_max_pair([5]) == (5, 1)
    with pytest.raises(ValueError):
        find_max_pair([])  

def test_flatten_basic_and_nested():
    """Test flatten: lameddab ainult ühe taseme"""
    assert flatten([[1,2],[3,4]]) == [1,2,3,4]
    assert flatten([[], [5]]) == [5]
   
    nested = [[1,[2]], [[3]]]
    out = flatten(nested)
    assert out == [1,[2],[3]]  

def test_read_write_file(tmp_path):
    """Test read_file ja write_file"""
    p = tmp_path / "test.txt"
    text = "Tere maailm äöü\n"
    written = write_file(str(p), text)
    assert written == len(text)
    read_back = read_file(str(p))
    assert read_back == text

def test_safe_get_basic():
    """Test safe_get: olemasolev ja vaikimisi väärtus"""
    d = {"x": 10}
    assert safe_get(d, "x") == 10
    assert safe_get(d, "y") is None
    assert safe_get(d, "y", 5) == 5

def test_top_n_normal_and_errors():
    """Test top_n: suurimad n väärtust ja vead"""
    nums = [5, 1, 3, 5]
    assert top_n(nums, 2) == [5,5]
    with pytest.raises(ValueError):
        top_n(nums, 0)
    with pytest.raises(ValueError):
        top_n([1,2], 5)

def test_chunk_list_normal_and_errors():
    """Test chunk_list: jagab õigesti ja viskab ValueError vigasel suurusel"""
    lst = [1,2,3,4,5]
    assert chunk_list(lst,2) == [[1,2],[3,4],[5]]
    assert chunk_list(lst,3) == [[1,2,3],[4,5]]
    assert chunk_list([],3) == []
    with pytest.raises(ValueError):
        chunk_list(lst,0)

def test_count_words_with_punctuation():
    """Test count_words: näitab vigadest, et kirjavahemärke ei eemaldata"""
    text = "tere, tere!"
    out = count_words(text)
    
    assert "tere" in out or "tere," in out or "tere!" in out

