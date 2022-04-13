import json

def read_local_json(name):
    with open(f"app/stocks/{name}", "r") as _file:
        data = json.load(_file)
    return data

def write_local_json(name, data):
    with open(f"app/stocks/{name}", "w") as _file:
        data = json.dump(data, _file, indent=4)

class JsonHandler:
    def __init__(self, file_name, read_only=False):
        self.file_name = file_name
        self.read_only = read_only
        self.data = read_local_json(file_name)
    
    def read_data(self):
        return self.data
    
    def write_data(self, data):
        if self.read_only:
            print(f"Warning: {self.file_name} is read-only")
        else:
            self.data = data
            write_local_json(self.file_name, data)

    def update_data(self):
        self.data = read_local_json(self.file_name)