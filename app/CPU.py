"""CPU Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class CPU(Model):
    """CPU Model."""
    __table__="cpus"
    @has_many("id", "cpu_id")
    def pcs(self):
        from app.PC import PC
        return PC