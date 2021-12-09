"""ThirdMisc Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class ThirdMisc(Model):
    """ThirdMisc Model."""
    __table__ = "thirdmiscs"
    @has_many("id", "thirdmisc_id")
    def pcs(self):
        from app.PC import PC
        return PC   