"""ThirdStorage Migration."""

from masoniteorm.migrations import Migration


class ThirdStorage(Migration):
    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_table("thirdstorages")

        with self.schema.create("thirdstorages") as table:
            table.increments("id")
            table.string("thirdstorage_name")
            table.string("thirdstorage_brand")
            table.string("thirdstorage_type")
            table.string("thirdstorage_size")
            table.integer("thirdstorage_price")
            table.string("thirdstorage_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("thirdstorages")
