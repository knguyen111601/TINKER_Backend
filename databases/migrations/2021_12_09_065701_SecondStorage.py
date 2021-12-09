"""SecondStorage Migration."""

from masoniteorm.migrations import Migration


class SecondStorage(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("secondstorages") as table:
            table.increments("id")
            table.string("secondstorage_name")
            table.string("secondstorage_brand")
            table.string("secondstorage_type")
            table.integer("secondstorage_size")
            table.integer("secondstorage_price")
            table.string("secondstorage_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("secondstorages")
