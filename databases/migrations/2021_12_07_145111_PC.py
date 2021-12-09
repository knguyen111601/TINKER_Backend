"""PC Migration."""

from masoniteorm.migrations import Migration


class PC(Migration):
    def up(self):
        """
        Run the migrations.
        """
        self.schema.drop_table("pcs")

        with self.schema.create("pcs") as table:
            table.increments("id")
            
            # Name
            table.string("pc_name")
            
            # Case
            table.integer("case_id")
            table.foreign("case_id").references("id").on("cases")
            
            # Motherboard
            table.integer("motherboard_id")
            table.foreign("motherboard_id").references("id").on("motherboards")
            
            # Cooler 
            table.integer("cooler_id")
            table.foreign("cooler_id").references("id").on("coolers")

            # CPU
            table.integer("cpu_id")
            table.foreign("cpu_id").references("id").on("coolers")

            # RAM
            table.integer("ram_id")
            table.foreign("ram_id").references("id").on("rams")

            # GPU
            table.integer("gpu_id")
            table.foreign("gpu_id").references("id").on("gpus")

            # PSU
            table.integer("psu_id")
            table.foreign("psu_id").references("id").on("psus")

            # Storage
            table.integer("storage_id")
            table.foreign("storage_id").references("id").on("storage")

            # Storage2
            table.integer("secondstorage_id")
            table.foreign("secondstorage_id").references("id").on("secondstorages")

            # Storage2
            table.integer("thirdstorage_id")
            table.foreign("thirdstorage_id").references("id").on("thirdstorage")


            #misc
            table.integer("misc_id")
            table.foreign("misc_id").references("id").on("miscs")

            #misc2
            table.integer("secondmisc_id")
            table.foreign("secondmisc_id").references("id").on("secondmiscs")

            #misc3
            table.integer("thirdmisc_id")
            table.foreign("thirdmisc_id").references("id").on("thirdmiscs")

            
            # User
            ## Field to track which user created the item
            table.integer("user_id")
            ## Defining the field as a foreign key
            table.foreign("user_id").references("id").on("users")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("pcs")
