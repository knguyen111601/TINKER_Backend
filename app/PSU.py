"""PSU Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class PSU(Model):
    """PSU Model."""
    __table__ = "psus"
    @has_many("id", "psu_id")
    def pcs(self):
        from app.PC import PC
        return PC