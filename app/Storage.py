"""Storage Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Storage(Model):
    """Storage Model."""
    __table__ = "storages"
    @has_many("id", "storage_id")
    def pcs(self):
        from app.PC import PC
        return PC