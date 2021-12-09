""" A MiscController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Misc import Misc

class MiscController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", MiscController)
        """
        id = self.request.param("id")
        return Misc.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", MiscController)
        """
        return Misc.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", MiscController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", MiscController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", MiscController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", MiscController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", MiscController)
        """

        pass