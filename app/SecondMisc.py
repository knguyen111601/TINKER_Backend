"""SecondMisc Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class SecondMisc(Model):
    """SecondMisc Model."""
    __table__ = "secondmiscs"
    @has_many("id", "secondmisc_id")
    def pcs(self):
        from app.PC import PC
        return PC   