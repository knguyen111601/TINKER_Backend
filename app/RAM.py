"""RAM Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class RAM(Model):
    """RAM Model."""
    __table__ = "rams"
    @has_many("id", "ram_id")
    def pcs(self):
        from app.PC import PC
        return PC
