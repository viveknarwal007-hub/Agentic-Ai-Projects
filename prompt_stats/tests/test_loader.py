import pytest
from prompt_stats.loader import load_csv
from prompt_stats.models import PromptEntry

def test_load_returns_a_list():
    result = load_csv("data/prompts.csv")
    assert isinstance(result, list)

def test_each_item_is_prompt_entry():
    result = load_csv("data/prompts.csv")
    for item in result:
        assert isinstance(item, PromptEntry)

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_csv("data/non_existent_file.csv")
        
def test_empty_file_raises(tmp_path):
    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")
    with pytest.raises(ValueError):
        load_csv(empty_file)
        