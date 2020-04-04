import json
from collections import defaultdict

class Get:
    """
    Returns the notebook.
    -- Eventually filters will be here to extract all notes that adhere to the specified filter
    """
    notebook =[]
    def load_notebook(self,file = '../Data/notebook.json'):
            return [json.loads(i) for i in open(file,'r').readlines()]
    
    
    def group_by(key):
        
        grouped_notebook = defaultdict(list)
        for note in notebook: #self.notebook:
            grouped_notebook[note[key]] += [note]
        return dict(grouped_notebook)
    
    def display(self):
        print_notebook = """"""
        def format_note(note):
            return  f"{note['entry_type']}  {note['entry']}\n"

        notebook = sorted(self.notebook, key= lambda x:x['ID'])
        for date,note in group_by('date').items():

            print_notebook+=f"{date}\n"
            for i in note:
                print_notebook+=format_note(i)
            print_notebook+='\n'
        return print_notebook
    # filter functions here

if __name__ == "__main__":
    get = Get()
    notebook = get.load_notebook()
    print(get.display())