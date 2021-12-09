""" A StorageController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Storage import Storage

class StorageController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", StorageController)
        """
        id = self.request.param("id")
        return Storage.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", StorageController)
        """
        return Storage.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", StorageController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", StorageController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", StorageController)
        """
        id = self.request.param("id")
        storage = Storage.where("id", id)
        Storage.where("id", id).delete()
        return storage