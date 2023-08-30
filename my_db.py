import os
import json

# Get the absolute path to the 'db.json' file
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db.json'))

class Database:
    def add_data(self, email, name, password):
        with open(file_path, 'r') as rf:
            curr_database = json.load(rf)
            if email in curr_database:
                return 0
            else:
                curr_database[email] = [name, password]
                with open(file_path, 'w') as wf:
                    json.dump(curr_database, wf)
                return 1

    def search(self, email, password):
        with open(file_path, 'r') as rf:
            curr_database = json.load(rf)
            if email in curr_database:
                if curr_database[email][-1] == password:
                    return 1
        return 0
