from .models import PromptEntry

def count_by_category(entries : list[PromptEntry]) -> dict[str , int]:
    """
    Count the number of PromptEntry objects in each category.

    Args:
        entries (list[PromptEntry]): A list of PromptEntry objects.

    Returns:
        dict[str, int]: A dictionary where keys are categories and values are counts.
    """
    category_count = {}
    for entry in entries:
        category = entry.category
        if category in category_count:
            category_count[category] +=1
        else:
            category_count[category] = 1
    return category_count

def count_by_model(entries : list[PromptEntry]) -> dict[str , int]:
    model_count = {}
    for entry in entries:
        model = entry.model
        if model in model_count:
            model_count[model] += 1
        else:
            model_count[model] = 1
    return model_count

def get_word_counts(entries : list[PromptEntry]) -> list[int]:
    return [len(entry.prompt.split()) for entry in entries]
    
def average_word_count(entries : list[PromptEntry]) -> float:
    word_counts = get_word_counts(entries)
    if not word_counts:
        return 0.0
    return sum(word_counts) / len(word_counts)

def analyze(entries :list[PromptEntry]) -> dict:
    return {
        "category_count": count_by_category(entries),
        "model_count": count_by_model(entries),
        "average_word_count": average_word_count(entries)
    }
    