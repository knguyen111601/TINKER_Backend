"""MiscTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Misc import Misc

class MiscTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        Misc.create({
            "misc_name": "Lian Li Strimer RGB Cable",
            "misc_img": "https://i.imgur.com/ayi84sv.jpg",
            "misc_price": 55
        })

        Misc.create({
            "misc_name": "Corsair Premium Sleeved PSU Cables (Black)",
            "misc_img": "https://i.imgur.com/q4zA5g6.jpg",
            "misc_price": 65
        })

        Misc.create({
            "misc_name": "Corsair Premium Sleeved PSU Cables (White)",
            "misc_img": "https://i.imgur.com/fI6Rjn3.jpg",
            "misc_price": 65
        })

        Misc.create({
            "misc_name": "Corsair QL Series QL120",
            "misc_img": "https://i.imgur.com/2LQooGS.jpg",
            "misc_price": 109
        })

        Misc.create({
            "misc_name": "Corsair LL120 RGB",
            "misc_img": "https://i.imgur.com/12YPspO.jpg",
            "misc_price": 119
        })

        Misc.create({
            "misc_name": "Noctua NF-A12x25 PWM",
            "misc_img": "https://i.imgur.com/LuV5XIb.jpg",
            "misc_price": 29
        })

        Misc.create({
            "misc_name": "NZXT Aer RGB 2 120mm",
            "misc_img": "https://i.imgur.com/mPf1kCL.jpg",
            "misc_price": 28
        })

        Misc.create({
            "misc_name": "Thermaltake ToughFan 12",
            "misc_img": "https://i.imgur.com/fZhhVIZ.jpg",
            "misc_price": 24
        })

        Misc.create({
            "misc_name": "Thermaltake ToughFan 14",
            "misc_img": "https://i.imgur.com/dJbIWKT.jpg",
            "misc_price": 34
        })

        Misc.create({
            "misc_name": "Scythe Kaze Flex 120 PWM",
            "misc_img": "https://i.imgur.com/oKXNz5t.jpg",
            "misc_price": 14
        })

        Misc.create({
            "misc_name": "be quiet! Silent Wings 3",
            "misc_img": "https://i.imgur.com/I3McZ0S.jpg",
            "misc_price": 25
        })

