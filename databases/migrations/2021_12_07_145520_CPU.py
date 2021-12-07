"""CPU Migration."""

from masoniteorm.migrations import Migration


class CPU(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("cpus") as table:
            table.increments("id")
            table.string("cpu_name")
            table.integer("cpu_price")
            table.string("cpu_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("cpus")
