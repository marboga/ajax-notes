
from system.core.model import Model

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def get_all_notes(self):
        return self.db.query_db("SELECT * FROM notes")

    def add_new_title(self, info):
        query = "INSERT INTO notes (title, created_at) VALUES (%s, NOW())"
        data = [info['title']]
        return self.db.query_db(query, data)

    def add_new_description(self, info):
        query = "UPDATE notes SET notes.description = %s, notes.updated_at = NOW() WHERE notes.id = %s"
        data = [info['description'], info['id']]
        print data
        return self.db.query_db(query, data)

    def delete_note(self, info):
        query = "DELETE FROM notes WHERE notes.id = %s"
        data = [info]
        return self.db.query_db(query, data)
