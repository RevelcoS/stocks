import json
from flask import current_app
from app.errors import ReadOnlyError

def read_local_json(name):
    with open(f"json/{name}", "r") as _file:
        data = json.load(_file)
    return data

def write_local_json(name, data):
    with open(f"json/{name}", "w") as _file:
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
            raise(ReadOnlyError(self.file_name))

        self.data = data
        write_local_json(self.file_name, data)

    def update_data(self, validator=None):
        '''If the data is updated successfully, returns True (False otherwise)'''
        try:
            data = read_local_json(self.file_name)
        except json.decoder.JSONDecodeError as exception:
            current_app.logger.error(f"SyntaxError in {self.file_name}: {exception}")
            return False
        
        if data == self.data:
            return False

        if validator:
            try:
                validator(data)
            except Exception as exception:
                current_app.logger.error(f"FormatError in {self.file_name}: {exception}")
                return False

        self.data = data
        return True