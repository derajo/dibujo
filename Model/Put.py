from Get import Get
from Delete import Delete
import json
import os

class Put:
    """
    Update a note entry
    """
    
    ID = float()
    notebook = Get().notebook()
    note = [note for note in self.notebook if note['ID'] == self.ID]
    
    date = note['date']
    time = note['time']
    entry_type = note['entry_type']
    entry = note['entry']
    subnote = note['subnote']
    tags = note['tags']
    
    def edit(self):
        delete = Delete()
        delete.ID = self.ID
        delete.delete_entry()
        
        
        edited_notebook_entry = {
            'ID'        : self.ID
            'date'      : self.date
            'time'      : self.time
            'entry_type': self.entry_type,
            'entry'     : self.entry,
            'subnote'   : self.subnote,
            'tags'      : self.tags

        }
        
        with open('Data/notebook.json', 'a') as f:
            json.dump(edited_notebook_entry, f)
            f.write(os.linesep)
    