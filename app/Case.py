"""Case Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Case(Model):
    """Case Model."""
    __table__ = "cases"
    @has_many("id", "case_id")
    def pcs(self):
        from app.PC import PC
        return PC