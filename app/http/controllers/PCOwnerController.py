""" A PCOwnerController Module """

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.PC import PC

class PCOwnerController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request


    def get_user_pcs(self):
        user = self.request.user()
        return PC.joins("cpu", "case", "motherboard", "ram", "gpu", "cooler", "psu", "storage").all()

    def create(self):
        pc_name = self.request.input("pc_name")
        case_id = self.request.input("case_id")
        motherboard_id = self.request.input("motherboard_id")
        cooler_id = self.request.input("cooler_id")
        cpu_id = self.request.input("cpu_id")
        ram_id = self.request.input("ram_id")
        gpu_id = self.request.input("gpu_id")
        psu_id = self.request.input("psu_id")
        storage_id = self.request.input("storage_id")
        misc_id = self.request.input("misc_id")
        user = self.request.user()
        pc = PC.create({
            "pc_name": pc_name,
            "case_id": case_id,
            "motherboard_id": motherboard_id,
            "cooler_id": cooler_id,
            "cpu_id": cpu_id,
            "ram_id": ram_id,
            "gpu_id": gpu_id,
            "psu_id": psu_id,
            "storage_id":storage_id,
            "misc_id": misc_id,
            "user_id": user["id"]
        })
        return pc

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", PCOwnerController)
        """

        pass

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", PCOwnerController)
        """

        pass

    def store(self):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", PCOwnerController)
        """

        pass

    def edit(self):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", PCOwnerController)
        """

        pass

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", PCOwnerController)
        """

        pass

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", PCOwnerController)
        """

        pass