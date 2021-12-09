"""ThirdStorage Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class ThirdStorage(Model):
    """ThirdStorage Model."""
    __table__ = "thirdstorages"
    @has_many("id", "thirdstorage_id")
    def pcs(self):
        from app.PC import PC
        return PC