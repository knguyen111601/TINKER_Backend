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
            table.string("pc_name").default("No Name")
            
            # Case
            table.integer("case_id").default(20)
            table.foreign("case_id").references("id").on("cases")
            
            # Motherboard
            table.integer("motherboard_id").default(17)
            table.foreign("motherboard_id").references("id").on("motherboards")
            
            # Cooler 
            table.integer("cooler_id").default(21)
            table.foreign("cooler_id").references("id").on("coolers")

            # CPU
            table.integer("cpu_id").default(22)
            table.foreign("cpu_id").references("id").on("coolers")

            # RAM
            table.integer("ram_id").default(18)
            table.foreign("ram_id").references("id").on("rams")

            # GPU
            table.integer("gpu_id").default(24)
            table.foreign("gpu_id").references("id").on("gpus")

            # PSU
            table.integer("psu_id").default(11)
            table.foreign("psu_id").references("id").on("psus")

            # Storage
            table.integer("storage_id").default(8)
            table.foreign("storage_id").references("id").on("storages")

            # Storage2
            table.integer("secondstorage_id").default(8)
            table.foreign("secondstorage_id").references("id").on("secondstorages")

            # Storage2
            table.integer("thirdstorage_id").default(8)
            table.foreign("thirdstorage_id").references("id").on("thirdstorages")


            #misc
            table.integer("misc_id").default(12)
            table.foreign("misc_id").references("id").on("miscs")

            #misc2
            table.integer("secondmisc_id").default(12)
            table.foreign("secondmisc_id").references("id").on("secondmiscs")

            #misc3
            table.integer("thirdmisc_id").default(12)
            table.foreign("thirdmisc_id").references("id").on("thirdmiscs")

            
            # User
            ## Field to track which user created the item
            # table.integer("user_id")
            # ## Defining the field as a foreign key
            # table.foreign("user_id").references("id").on("users")
            # table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("pcs")
