"""Cooler Migration."""

from masoniteorm.migrations import Migration


class Cooler(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("coolers") as table:
            table.increments("id")
            table.string("cooler_type")
            table.string("cooler_size")
            table.string("cooler_name")
            table.integer("cooler_price")
            table.string("cooler_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("coolers")
