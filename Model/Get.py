import json
from collections import defaultdict
from utils import load_keys
import time 
import datetime 



class Get:
    """
    Returns the notebook with any user designated filters
    """
    notebook =[]
    def load_notebook(self,file = '../Data/notebook.json'):
            return [json.loads(i) for i in open(file,'r').readlines()]
    
    
    def group_by(self,key):
        
        grouped_notebook = defaultdict(list)
        for note in sorted(self.load_notebook(), key= lambda x:x['ID']): #self.notebook:
            grouped_notebook[note[key]] += [note]
        return dict(grouped_notebook)
    
    def display(self):
        print_notebook = """"""
        def format_note(note):
            return  f"{note['entry_type']}  {note['entry']}\n"

        for date,note in self.group_by('date').items():

            print_notebook+=f"{date}\n"
            for i in note:
                print_notebook+=format_note(i)
            print_notebook+='\n'
        return print_notebook
    # filter functions here
    
    # Date Filter
    def date_range_filter(self,begin_date='',end_date=''):
        """
        Filters the notebook based on a date range
        """
        if begin_date == '' and end_date == '':
            return self.notebook
        else:

            begin_date = time.mktime(datetime.datetime.strptime(begin_date,"%m/%d/%Y").timetuple())
            end_date = time.mktime((datetime.datetime.strptime(end_date,"%m/%d/%Y")+datetime.timedelta(days=1)).timetuple())

            return [i for i in self.notebook if i['ID'] >= timestamp_range[0] and i['ID'] < timestamp_range[1]]


    # time filter

    # entry_type
    def entry_type_filter(self,entry_type = list(load_keys().keys())):
        return [i for i in self.notebook if i['entry_type'] in entry_type]

    # entry
    def entry_text_filter(self,search_query = ''):
        """
        Simple search feature tokenizing the search query and checking if any of the words are in any entries
        """
        
        if search_query == '':
            return self.notebook
        else:
            search_terms = search_query.split()
            notebook_results = []  
            for term in search_terms:
                notebook_results+=[i for i in self.notebook if term.lower() in i['entry'].lower() and i not in notebook_results]                
            return notebook_results
    
    # subnote?

    #tags
    def tag_filter(self,tags = ['']):
        if tags == ['']:
            return self.notebook
        else:
            notebook_results = []
            for tag in tags:
                notebook_results+=[i for i in self.notebook if tag in i['tags'] and i not in notebook_results]                
            return notebook_results
    

# if __name__ == "__main__":
#     get = Get()
#     get.notebook = get.load_notebook()
#     get.notebook = get.tag_filter(['test','filter_testing2'])
#     get.notebook = get.entry_text_filter('dog')