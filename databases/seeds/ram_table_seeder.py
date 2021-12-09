"""RAMTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.RAM import RAM

class RAMTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        # 2 Sticks 16GB
        RAM.create({
            "ram_name": "TeamGroup T-Force Xtreem ARGB DDR4-3600 (2 x 8GB)",
            "ram_number_of": "2",
            "ram_size": "16GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 164,
            "ram_img": "https://i.imgur.com/lxOhGI0.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Dominator Platinum RGB DDR4-3600 (2 x 8GB) (Black)",
            "ram_number_of": "2",
            "ram_size": "16GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 129,
            "ram_img": "https://i.imgur.com/vju0qtW.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Dominator Platinum RGB DDR4-3600 (2 x 8GB) (White)",
            "ram_number_of": "2",
            "ram_size": "16GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 129,
            "ram_img": "https://i.imgur.com/qNSOj7R.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Vengeance RGB Pro DDR4-3600 (2 x 8GB) (Black)",
            "ram_number_of": "2",
            "ram_size": "16GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 91,
            "ram_img": "https://i.imgur.com/b6KB8OZ.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Vengeance RGB Pro DDR4-3600 (2 x 8GB) (White)",
            "ram_number_of": "2",
            "ram_size": "16GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 91,
            "ram_img": "https://i.imgur.com/tVohjsI.jpg"
        })

        RAM.create({
            "ram_name": "G.Skill Trident Z Neo DDR4-3600 (2 x 8GB)",
            "ram_number_of": "2",
            "ram_size": "16GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 110,
            "ram_img": "https://i.imgur.com/3XExaFb.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Vengeance LPX DDR4 (2 x 8GB)",
            "ram_number_of": "2",
            "ram_size": "16GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 104,
            "ram_img": "https://i.imgur.com/8qs9W5D.jpg"
        })

        # 2 Sticks 32gb
        RAM.create({
            "ram_name": "Corsair Vengeance LPX DDR4 (2 x 16GB)",
            "ram_number_of": "2",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 139,
            "ram_img": "https://i.imgur.com/8qs9W5D.jpg"
        })

        RAM.create({
            "ram_name": "G.Skill Trident Z Neo DDR4-3600 (2 x 16GB)",
            "ram_number_of": "2",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 141,
            "ram_img": "https://i.imgur.com/3XExaFb.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Vengeance RGB Pro DDR4-3600 (2 x 16GB) (White)",
            "ram_number_of": "2",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 152,
            "ram_img": "https://i.imgur.com/tVohjsI.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Vengeance RGB Pro DDR4-3600 (2 x 16GB) (Black)",
            "ram_number_of": "2",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 152,
            "ram_img": "https://i.imgur.com/b6KB8OZ.jpg"
        })

        RAM.create({
            "ram_name": "Team T-Force XTREEM ARGB DDR4 (2 x 16GB)",
            "ram_number_of": "2",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 289,
            "ram_img": "https://i.imgur.com/tTLpROZ.jpg"
        })

        # 4 sticks 32GB
        RAM.create({
            "ram_name": "Corsair Dominator Platinum (4 x 8GB)",
            "ram_number_of": "4",
            "ram_size": "32GB",
            "ram_speed": "3200 Mhz",
            "ram_price": 229,
            "ram_img": "https://i.imgur.com/SjOBx4h.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Vengeance RGB Pro DDR4-3200 (4 x 8GB) (Black)",
            "ram_number_of": "4",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 164,
            "ram_img": "https://i.imgur.com/6NKEwMZ.jpg"
        })

        RAM.create({
            "ram_name": "Corsair Vengeance RGB Pro DDR4-3200 (4 x 8GB) (White)",
            "ram_number_of": "4",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 164,
            "ram_img": "https://i.imgur.com/8W6mAXe.jpg"
        })

        RAM.create({
            "ram_name": "G.Skill Trident Z RGB DDR4 (4 x 8GB)",
            "ram_number_of": "4",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 174,
            "ram_img": "https://i.imgur.com/IDPgbHf.jpg"
        })

        RAM.create({
            "ram_name": "G.Skill Trident Z Neo DDR4 (4 x 8GB)",
            "ram_number_of": "4",
            "ram_size": "32GB",
            "ram_speed": "3600 Mhz",
            "ram_price": 364,
            "ram_img": "https://i.imgur.com/LIQkspK.jpg"
        })