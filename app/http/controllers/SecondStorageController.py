""" A SecondControllerController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.SecondStorage import SecondStorage

class SecondStorageController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", SecondControllerController)
        """
        id = self.request.param("id")
        return SecondStorage.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", SecondControllerController)
        """
        return SecondStorage.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", SecondControllerController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", SecondControllerController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", SecondControllerController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", SecondControllerController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", SecondControllerController)
        """
        id = self.request.param("id")
        storage = SecondStorage.where("id", id)
        SecondStorage.where("id", id).delete()
        return storage