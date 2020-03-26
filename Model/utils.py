import json


def load_keys(file = '../Icons/keys.json'):
    """
    loads in the notebook keys dictionary
    """

    with open(file,'r') as f:
        key = json.load(f)
    return key

def load_status(file = '../Icons/status.json'):
    """
    loads in the notebook status dictionary
    """

    with open(file,'r') as f:
        status = json.load(f)
    return status


def valid_entry_type_options(key):
        output = ''
        for k,v in key.items():
            output+=(f'{k}: {v}\n')
        return output
    
        
def valid_entry_status_options(status):
        output = ''
        for k,v in status.items():
            output+=(f'{k}: {v}\n')
        return output