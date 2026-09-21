import csv 
from pathlib import Path
from .models import PromptEntry

def load_csv(file_path : str) -> list[PromptEntry]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"file not found : {file_path}")
    with open(path , mode= "r" , encoding="utf-8") as file:
        reader = csv.DictReader(file)  
        #  reader gives you each row as a dict: {"id": "1", "prompt": "What is ML?", "category": "education", "model": "gemini"}
        entries = []
        for row in reader:
            Entry =PromptEntry(id = int(row["id"]) , prompt = row["prompt"] , category = row["category"] , model = row["model"])
            entries.append(Entry)
        if not entries:
            raise ValueError(f"CSV file is empty : {file_path}")
    return entries