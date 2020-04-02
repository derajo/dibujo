import json

class Get:
    """
    Returns the notebook.
    -- Eventually filters will be here to extract all notes that adhere to the specified filter
    """
    def notebook(self,file = '../Data/notebook.json'):
            return [json.loads(i) for i in open(file,'r').readlines()]
        
    # filter functions here

if __name__ == "__main__":
    get = Get()
    notebook = get.notebook()