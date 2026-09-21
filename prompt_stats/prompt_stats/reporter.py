def print_validation_report(validation_results : dict) -> None:
    print("------VALIDATION REPORT------")
    print(f"Total Issues Found: {validation_results['total_issues']}")
    
    print("Missing Fields:")
    for entry in validation_results['missing_fields']:
        empty_fields = []
        if entry.prompt == "":
            empty_fields.append("prompt")
        if entry.model == "":
            empty_fields.append("model")
        print(f"  - Entry ID {entry.id}: {' and '.join(empty_fields)} is empty.")
    print("Duplicate Prompts:")
    for entry in validation_results['duplicates']:
        print(f"-Entry ID: {entry.id}, Prompt: '{entry.prompt}' is a duplicate.")
        
def print_analysis_report(analysis_results : dict) -> None:
    print("------ANALYSIS REPORT------")
    print(f"average prompt length: {analysis_results['average_word_count']:.2f} words")
    
    print("Prompt Count by Category:")
    for category, count in analysis_results['category_count'].items():
        print(f"-{category}: {count}")
    
    print("Prompt Count by Model:")
    for model, count in analysis_results['model_count'].items():
        print(f"-{model}: {count}")
