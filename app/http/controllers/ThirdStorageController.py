""" A ThirdControllerController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.ThirdStorage import ThirdStorage

class ThirdStorageController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
        self.request = request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", ThirdControllerController)
        """
        id = self.request.param("id")
        return ThirdStorage.find(id)


    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", ThirdControllerController)
        """
        return ThirdStorage.all()

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", ThirdControllerController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", ThirdControllerController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", ThirdControllerController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", ThirdControllerController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", ThirdControllerController)
        """
        id = self.request.param("id")
        storage = ThirdStorage.where("id", id)
        ThirdStorage.where("id", id).delete()
        return storage