"""PSU Migration."""

from masoniteorm.migrations import Migration


class PSU(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("psus") as table:
            table.increments("id")
            table.string("psu_name")
            table.string("psu_type")
            table.string("psu_watts")
            table.string("psu_rating")
            table.integer("psu_price")
            table.string("psu_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("psus")
