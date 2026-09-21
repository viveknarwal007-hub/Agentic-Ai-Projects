class PromptEntry:
    def __init__(self , id : int, prompt : str , category : str , model : str):
        self.id = id 
        self.prompt = prompt 
        self.category = category
        self.model = model
        
    def __repr__(self) -> str:
        return f"PromptEntry(id = {self.id} , prompt = '{self.prompt}' , category = '{self.category}' ,model = '{self.model}')"