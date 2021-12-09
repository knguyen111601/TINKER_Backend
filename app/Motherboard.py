"""Motherboard Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Motherboard(Model):
    """Motherboard Model."""
    __table__ = "motherboards"
    @has_many("id", "motherboard_id")
    def pcs(self):
        from app.PC import PC
        return PC