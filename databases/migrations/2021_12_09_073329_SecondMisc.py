"""SecondMisc Migration."""

from masoniteorm.migrations import Migration


class SecondMisc(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("secondmiscs") as table:
            table.increments("id")
            table.string("secondmisc_name")
            table.string("secondmisc_img")
            table.integer("secondmisc_price")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("secondmiscs")
