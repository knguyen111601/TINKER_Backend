"""Misc Migration."""

from masoniteorm.migrations import Migration


class Misc(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("miscs") as table:
            table.increments("id")
            table.string("misc_name")
            table.string("misc_img")
            table.integer("misc_price")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("miscs")
