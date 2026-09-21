# 1. load_csv("data/prompts.csv")            → entries (full list)
# 2. validate(entries)                        → validation_results
# 3. print_validation_report(...)             → show problems
# 4. filter out the bad entries               → clean_entries
# 5. analyze(clean_entries)                   → analysis_results
# 6. print_analysis_report(...)               → show stats


from prompt_stats.loader    import load_csv
from prompt_stats.validator import validate
from prompt_stats.analyzer  import analyze
from prompt_stats.reporter  import print_validation_report, print_analysis_report
    # Step 1: Load the CSV file
def run():
    entries = load_csv("data/prompts.csv")

    # Step 2: Validate the entries
    validation_results = validate(entries)

    # Step 3: Print the validation report
    print_validation_report(validation_results)

    # Step 4: Filtered out entries with missing fields or duplicate prompts
    missing_field_ids = {
        entry.id for entry in validation_results["missing_fields"]
    }
    duplicate_ids = {
        entry.id for entry in validation_results["duplicates"]
    }
    bad_ids = missing_field_ids | duplicate_ids

    clean_entries = [
        entry for entry in entries
        if entry.id not in bad_ids
    ]
    # Step 5: we analysing the clean entries
    analysis_results = analyze(clean_entries)

    # Step 6: Printed the analysis report
    print_analysis_report(analysis_results)

if __name__ == "__main__":
    run()
