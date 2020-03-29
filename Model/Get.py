import json

class Get:
    def notebook(self,file = '../Data/notebook.json'):
            return [json.loads(i) for i in open(file,'r').readlines()]

if __name__ == "__main__":
    get = Get()
    notebook = get.notebook()