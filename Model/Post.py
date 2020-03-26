import time as t
from datetime import date,datetime

import json
import os

from utils import *

class Post:
    """
    Posts a new note to your notebook

    """

    entry_type= '.'
    entry=''
    tags = ''
    subnote = ['']
    entry_status=''
    
    key = load_keys()
    key_format = valid_entry_type_options(key)
    status = load_status() # status's will be handled by user interaction
    #status_format = valid_entry_status_options(status)
    

    def format_post(self):
        # Post a note with all required features
        self.entry_type        = '.' if self.entry_type == '' else self.entry_type
        self.entry_type        = str(self.entry_type).strip()
        
        self.entry             = str(self.entry).strip()
        
        if type(self.tags)    != list:
            self.tags          = str(self.tags).strip().split(',') # make a list with a , delimiter
        self.tags              = [str(i).strip().replace(" ","_") for i in self.tags]
        
        
        if type(self.subnote) != list:
            self.subnote       = self.subnote.split(';')
        self.subnote           = [str(i).strip() for i in self.subnote]
        
        #self.date              = datetime.now().strftime("%d %B %Y")
        
        #self.time              = datetime.now().strftime("%H:%M:%S")
        
        assert self.entry_type in self.key.keys() or self.entry_type in self.key.values(), f"Entry Type: {self.entry_type} is not a valid journal entry. Valid entry types include:\n {self.key_format}" 
        #assert self.entry_status in self.status.keys() or self.entry_status in self.status.values(), f"Status Type: {self.entry_status} is not a valid status. Valid statuses include:\n {self.status_format}" 

    
    def write_post(self):
        notebook_entry = {
            'ID'        : t.time(),
            'date'      : datetime.now().strftime("%d %B %Y"),
            'time'      : datetime.now().strftime("%H:%M:%S"), 
            'entry_type': self.entry_type,
            'entry'     : self.entry,
            'subnote'   : self.subnote,
            'tags'      : self.tags

        }
        
        with open('../Data/notebook.json', 'a') as f:
            json.dump(notebook_entry, f)
            f.write(os.linesep)
    
    def first_post(self):
        notebook_entry = {
            'ID'        : t.time(),
            'date'      : datetime.now().strftime("%d %B %Y"),
            'time'      : datetime.now().strftime("%H:%M:%S"), 
            'entry_type': '.',
            'entry'     : 'Welcome to Digital Bullet Journal!',
            'subnote'   : ['Tutorial and introduction coming soon!','Come back soon!'],
            'tags'      : ['dibujo']

        }
        
        with open('../Data/notebook.json', 'a') as f:
            json.dump(notebook_entry, f)
            f.write(os.linesep)
    
if __name__ == "__main__":
    # here is where I would write a bunch of helper functions
    post = Post()
    if os.path.exists("../Data/notebook.json") == False:
        post.first_post()
    post.entry = input('Note Entry: ')
    post.entry_type=input('Entry Type: ')
    # write a helper for when the user inputs 'options' to list the entry options
    if post.entry_type.lower() == 'options':
        print(valid_entry_type_options(post.key)) 
        post.entry_type = input('Entry Type: ')

    post.tags = input('Entry Tags (separated by a ","): ')
    post.subnote = input('Entry Subnote (separated by a ";"): ') # will need some work. Maybe not have an option for this, but have it only be possible to go edit after it is posted?
    post.format_post()
    post.write_post()