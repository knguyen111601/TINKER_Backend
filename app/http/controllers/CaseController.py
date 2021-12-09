""" A CaseController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Case import Case

class CaseController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request


    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", CaseController)
        """
        id = self.request.param("id")
        return Case.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", CaseController)
        """
        return Case.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", CaseController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", CaseController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", CaseController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", CaseController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", CaseController)
        """

        pass