""" A CoolerController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Cooler import Cooler

class CoolerController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", CoolerController)
        """
        id = self.request.param('id')
        return Cooler.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", CoolerController)
        """
        return Cooler.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", CoolerController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", CoolerController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", CoolerController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", CoolerController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", CoolerController)
        """

        pass