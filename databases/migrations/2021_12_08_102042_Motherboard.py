"""Motherboard Migration."""

from masoniteorm.migrations import Migration


class Motherboard(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("motherboards") as table:
            table.increments("id")
            table.string("motherboard_size")
            table.string("motherboard_type")
            table.string("motherboard_name")
            table.integer("motherboard_ram_slots")
            table.integer("motherboard_price")
            table.string("motherboard_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("motherboards")
