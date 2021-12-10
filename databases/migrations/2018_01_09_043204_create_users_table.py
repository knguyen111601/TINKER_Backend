from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        self.schema.drop_table("users")
        with self.schema.create("users") as table:
            table.increments("id")
            table.string("pfp")
            table.string("username").unique()
            table.string("password")
            table.string("remember_token").nullable()
            table.timestamp("verified_at").nullable()
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop("users")