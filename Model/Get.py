import json
from collections import defaultdict
from Model.utils import load_keys
import time 
import datetime 



class Get:
    """
    Returns the notebook.
    -- Eventually filters will be here to extract all notes that adhere to the specified filter
    """
    notebook =[]
    def load_notebook(self,file = 'Data/notebook.json'):
            return [json.loads(i) for i in open(file,'r').readlines()]
    
    
    def group_by(self,key):
        
        grouped_notebook = defaultdict(list)
        for note in sorted(self.load_notebook(), key= lambda x:x['ID']):
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

            return [i for i in notebook if i['ID'] >= timestamp_range[0] and i['ID'] < timestamp_range[1]]


    # time filter

    # entry_type
    def entry_type_filter(self,entry_type = list(load_keys().keys())):
        return [i for i in self.notebook if i['entry_type'] in entry_type]

    # entry

    # subnote?

    #tags

#if __name__ == "__main__":
    #get = Get()
    #notebook = get.load_notebook()
    #print(get.display())