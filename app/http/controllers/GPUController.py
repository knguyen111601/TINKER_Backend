""" A GPUController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.GPU import GPU

class GPUController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", GPUController)
        """
        id = self.request.param("id")
        return GPU.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", GPUController)
        """
        return GPU.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", GPUController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", GPUController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", GPUController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", GPUController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", GPUController)
        """

        pass