"""Case Migration."""

from masoniteorm.migrations import Migration


class Case(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("cases") as table:
            table.increments("id")
            table.string("case_name")
            table.string("case_type")
            table.integer("case_price")
            table.string("case_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("cases")
