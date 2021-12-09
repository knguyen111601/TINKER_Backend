"""PC Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_one

class PC(Model):
    """PC Model."""
    __table__="pcs"

    # CASE
    @has_one("id", "case_id")
    def case(self):
        from app.Case import Case
        return Case

    # Motherboard
    @has_one("id", "motherboard_id")
    def motherboard(self):
        from app.Motherboard import Motherboard
        return Motherboard

    # Cooler
    @has_one("id", "cooler_id")
    def cooler(self):
        from app.Cooler import Cooler
        return Cooler

    # CPU
    @has_one("id", "cpu_id")
    def cpu(self):
        from app.CPU import CPU
        return CPU

    # RAM
    @has_one("id", "ram_id")
    def ram(self):
        from app.RAM import RAM
        return RAM

    # GPU
    @has_one("id", "gpu_id")
    def gpu(self):
        from app.GPU import GPU
        return GPU

    # PSU
    @has_one("id", "psu_id")
    def psu(self):
        from app.PSU import PSU
        return PSU

    # Storage
    @has_one("id", "storage_id")
    def storage(self):
        from app.Storage import Storage
        return Storage

    # misc
    # @has_one("id", "misc_id")
    # def misc(self):
    #     from app.Misc import Misc
    #     return Misc
