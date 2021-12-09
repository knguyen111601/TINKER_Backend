"""RAM Migration."""

from masoniteorm.migrations import Migration


class RAM(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("rams") as table:
            table.increments("id")
            table.string("ram_name")
            table.string("ram_number_of")
            table.string("ram_size")
            table.string("ram_speed")
            table.integer("ram_price")
            table.string("ram_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("rams")
