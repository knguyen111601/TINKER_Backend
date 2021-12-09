"""Misc Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Misc(Model):
    """Misc Model."""
    __table__ = "miscs"
    @has_many("id", "misc_id")
    def pcs(self):
        from app.PC import PC
        return PC   