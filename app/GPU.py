"""GPU Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class GPU(Model):
    """GPU Model."""
    __table__ = "gpus"
    @has_many("id", "gpu_id")
    def pcs(self):
        from app.PC import PC
        return PC