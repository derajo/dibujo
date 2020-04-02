import json
from Get import Get
import os
import time as t

class Delete:
    """
    Deletes a note given its ID
    """
    ID = float()
    notebook = Get().notebook()
    def delete_entry(self):
        # archive the deleted note in the note archives
        deleted_note = [note for note in self.notebook if note['ID'] == self.ID]
        if len(deleted_note) > 0: 
            with open(f'../Data/archived_notes.json', 'a') as f:
                json.dump({t.time():deleted_note[0]}, f)
                f.write(os.linesep)
        # delete entry
        self.notebook = [note for note in self.notebook if note['ID'] != self.ID]
        with open('../Data/notebook.json', 'w+') as f:
            for note in self.notebook:
                json.dump(note, f)
                f.write(os.linesep)
        
#if __name__ == "__main__":
#    delete = Delete()
#    delete.ID = float()
#    delete.delete_entry()