""" A MotherboardController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Motherboard import Motherboard

class MotherboardController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", MotherboardController)
        """
        id = self.request.param("id")
        return Motherboard.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", MotherboardController)
        """
        return Motherboard.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", MotherboardController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", MotherboardController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", MotherboardController)
        """

        pass