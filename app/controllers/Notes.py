
from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)

        self.load_model('Note')



    def index(self):
        notes = self.models['Note'].get_all_notes()
        return self.load_view('index.html', notes=notes)

    def partialindex(self):
        notes = self.models['Note'].get_all_notes()
        return self.load_view('partialindex.html', notes=notes)

    def add(self):
        titler = {
        "title": request.form['title']
        }
        self.models['Note'].add_new_title(titler)
        notes = self.models['Note'].get_all_notes()
        return self.load_view('partialindex.html', notes=notes)

    def description(self):
        desc = {
        "description": request.form['description'],
        "id": request.form['hidden']
        }
        print "desc"
        self.models['Note'].add_new_description(desc)
        return redirect('/')

    def delete(self, id):
        self.models['Note'].delete_note(id)
        return redirect('/')
