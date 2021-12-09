"""Storage Migration."""

from masoniteorm.migrations import Migration


class Storage(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("storages") as table:
            table.increments("id")
            table.string("storage_name")
            table.string("storage_brand")
            table.string("storage_type")
            table.integer("storage_size")
            table.integer("storage_price")
            table.string("storage_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("storages")
