""" A CPUController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.CPU import CPU

class CPUController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request


    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", CPUController)
        """
        id = self.request.param("id")
        return CPU.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", CPUController)
        """
        return CPU.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", CPUController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", CPUController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", CPUController)
        """

        pass