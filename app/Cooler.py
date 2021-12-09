"""Cooler Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Cooler(Model):
    """Cooler Model."""
    __table__ = "coolers"
    @has_many("id", "cooler_id")
    def pcs(self):
        from app.PC import PC
        return PC