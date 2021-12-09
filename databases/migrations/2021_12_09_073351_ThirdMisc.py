"""ThirdMisc Migration."""

from masoniteorm.migrations import Migration


class ThirdMisc(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("thirdmiscs") as table:
            table.increments("id")
            table.string("thirdmisc_name")
            table.string("thirdmisc_img")
            table.integer("thirdmisc_price")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("thirdmiscs")
