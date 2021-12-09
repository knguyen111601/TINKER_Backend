"""GPU Migration."""

from masoniteorm.migrations import Migration


class GPU(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("gpus") as table:
            table.increments("id")
            table.string("gpu_brand")
            table.string("gpu_name")
            table.integer("gpu_price")
            table.string("gpu_img")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("gpus")
