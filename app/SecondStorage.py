"""SecondStorage Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class SecondStorage(Model):
    """SecondStorage Model."""
    __table__ = "secondstorages"
    @has_many("id", "secondstorage_id")
    def pcs(self):
        from app.PC import PC
        return PC