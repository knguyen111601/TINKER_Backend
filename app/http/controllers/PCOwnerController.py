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
        return PC.joins("cpu", "case", "motherboard", "ram", "gpu", "cooler", "psu", "storage", "secondstorage", "thirdstorage", "misc", "secondmisc", "thirdmisc").all()

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
        secondstorage_id = self.request.input("secondstorage_id")
        thirdstorage_id = self.request.input("thirdstorage_id")
        misc_id = self.request.input("misc_id")
        secondmisc_id = self.request.input("secondmisc_id")
        thirdmisc_id = self.request.input("thirdmisc_id")
        public = self.request.input("public")
        user = self.request.user()
        print(user)
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
            "secondstorage_id":secondstorage_id,
            "thirdstorage_id":thirdstorage_id,
            "misc_id": misc_id,
            "secondmisc_id": secondmisc_id,
            "thirdmisc_id": thirdmisc_id,
            "public": public,
            "user_id": user["id"]
        })
        print(pc)
        return pc

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", PCOwnerController)
        """
        user = self.request.user()
        id = self.request.param("id")
        return PC.joins("cpu", "case", "motherboard", "ram", "gpu", "cooler", "psu", "storage", "secondstorage", "thirdstorage", "misc", "secondmisc", "thirdmisc").where("id", id).all()

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", PCOwnerController)
        """
        user = self.request.user()
        id = self.request.param("id")
        pc_name = self.request.input("pc_name")
        case_id = self.request.input("case_id")
        motherboard_id = self.request.input("motherboard_id")
        cooler_id = self.request.input("cooler_id")
        cpu_id = self.request.input("cpu_id")
        ram_id = self.request.input("ram_id")
        gpu_id = self.request.input("gpu_id")
        psu_id = self.request.input("psu_id")
        storage_id = self.request.input("storage_id")
        secondstorage_id = self.request.input("secondstorage_id")
        thirdstorage_id = self.request.input("thirdstorage_id")
        misc_id = self.request.input("misc_id")
        secondmisc_id = self.request.input("secondmisc_id")
        thirdmisc_id = self.request.input("thirdmisc_id")
        PC.where("id", id).where("user_id", user["id"]).update({
            "pc_name": pc_name,
            "case_id": case_id,
            "motherboard_id": motherboard_id,
            "cooler_id": cooler_id,
            "cpu_id": cpu_id,
            "ram_id": ram_id,
            "gpu_id": gpu_id,
            "psu_id": psu_id,
            "storage_id":storage_id,
            "secondstorage_id":secondstorage_id,
            "thirdstorage_id":thirdstorage_id,
            "misc_id": misc_id,
            "secondmisc_id": secondmisc_id,
            "thirdmisc_id": thirdmisc_id
        })
        return PC.where("id", id).where("user_id", user["id"]).get()

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", PCOwnerController)
        """
        user = self.request.user()
        id = self.request.param("id")
        pc = PC.where("id", id).where("user_id", user["id"])
        PC.where("id", id).where("user_id", user["id"]).delete()
        return pc