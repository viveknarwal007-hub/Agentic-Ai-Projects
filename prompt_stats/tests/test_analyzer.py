import pytest
from prompt_stats.loader import load_csv
from prompt_stats.models import PromptEntry
from prompt_stats.analyzer import count_by_category, count_by_model, average_word_count, analyze

def test_count_by_category():
    entries = [
        PromptEntry(id=1, prompt="What is ML?", category="education", model="gemini"),
        PromptEntry(id=2, prompt="What is AI?", category="education", model="gemini"),
        PromptEntry(id=3, prompt="What is Python?", category="programming", model="gemini")
    ]
    result = count_by_category(entries)
    assert result == {"education": 2, "programming": 1}
    
def test_count_by_model():
    entries = [
        PromptEntry(id=1, prompt="What is ML?", category="education", model="gemini"),
        PromptEntry(id=2, prompt="What is AI?", category="education", model="gemini"),
        PromptEntry(id=3, prompt="What is Python?", category="programming", model="gpt-4")
    ]
    result = count_by_model(entries)
    assert result == {"gemini": 2, "gpt-4": 1}

def test_get_word_counts():
    entries = [
        PromptEntry(id=1, prompt="What is ML?", category="education", model="gemini"),
        PromptEntry(id=2, prompt="What is AI?", category="education", model="gemini"),
        PromptEntry(id=3, prompt="What is Python programming?", category="programming", model="gpt-4")
    ]
    result = [len(entry.prompt.split()) for entry in entries]
    assert result == [3, 3, 4]

def test_average_word_count():
    entries = [
        PromptEntry(id=1, prompt="What is ML?", category="education", model="gemini"),
        PromptEntry(id=2, prompt="What is AI?", category="education", model="gemini"),
        PromptEntry(id=3, prompt="What is Python programming?", category="programming", model="gpt-4")
    ]
    result = average_word_count(entries)
    assert result == pytest.approx((3 + 3 + 4) / 3)
    
def test_average_empty_list():
    entries = []
    result = average_word_count(entries)
    assert result == 0.0