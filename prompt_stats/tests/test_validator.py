import pytest
from prompt_stats.loader import load_csv
from prompt_stats.models import PromptEntry
from prompt_stats.validator import find_missing_fields, find_duplicates, validate


def make_entry(id = 1 , prompt = "What is ML?" , category = "education" , model = "gemini") -> PromptEntry:
    return PromptEntry(id=id, prompt=prompt, category=category, model=model)

def test_no_issues_on_clean_data():
    entries = [
        make_entry(id=1, prompt="What is ML?", category="education", model="gemini"),
        make_entry(id=2, prompt="What is AI?", category="education", model="gemini")
    ]
    result = validate(entries)
    assert result["total_issues"] == 0
    assert result["missing_fields"] == []
    assert result["duplicates"] == []

def test_finds_empty_prompt():
    entries = [
        make_entry(id=1, prompt="", category="education", model="gemini"),
        make_entry(id=2, prompt="What is AI?", category="education", model="gemini")
    ]
    result = validate(entries)
    assert result["total_issues"] == 1
    assert len(result["missing_fields"]) == 1
    assert result["missing_fields"][0].id == 1
    
def test_finds_empty_model():
    entries = [
        make_entry(id=1, prompt="What is ML?", category="education", model=""),
        make_entry(id=2, prompt="What is AI?", category="education", model="gemini")
    ]
    result = validate(entries)
    assert result["total_issues"] == 1
    assert len(result["missing_fields"]) == 1
    assert result["missing_fields"][0].id == 1

def test_finds_duplicate_prompt():
    entries = [
        make_entry(id=1, prompt="What is ML?", category="education", model="gemini"),
        make_entry(id=2, prompt="What is ML?", category="education", model="gemini")
    ]
    result = validate(entries)
    assert result["total_issues"] == 1
    assert len(result["duplicates"]) == 1
    assert result["duplicates"][0].id == 2