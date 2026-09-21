from .models import PromptEntry
def find_missing_fields(entries : list[PromptEntry]) -> list[PromptEntry]:
    return [entry for entry in entries if entry.prompt == "" or entry.model == ""]

def find_duplicates(entries : list[PromptEntry]) -> list[PromptEntry]:
    seen = set()
    duplicates = []
    for entry in entries:
        if entry.prompt in seen:
            duplicates.append(entry)
        else:
            seen.add(entry.prompt)
    return duplicates

def validate(entries : list[PromptEntry]) -> dict:
    missing_fields = find_missing_fields(entries)
    duplicates = find_duplicates(entries)
    return {
        "missing_fields": missing_fields,
        "duplicates": duplicates,
        "total_issues": len(missing_fields) + len(duplicates)
    }
