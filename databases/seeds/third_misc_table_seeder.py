"""ThirdMiscTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.ThirdMisc import ThirdMisc

class ThirdMiscTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

    ThirdMisc.create({
        "thirdmisc_name": "Lian Li Strimer RGB Cable",
        "thirdmisc_img": "https://i.imgur.com/ayi84sv.jpg",
        "thirdmisc_price": 55
    })

    ThirdMisc.create({
        "thirdmisc_name": "Corsair Premium Sleeved PSU Cables (Black)",
        "thirdmisc_img": "https://i.imgur.com/q4zA5g6.jpg",
        "thirdmisc_price": 65
        })

    ThirdMisc.create({
        "thirdmisc_name": "Corsair Premium Sleeved PSU Cables (White)",
        "thirdmisc_img": "https://i.imgur.com/fI6Rjn3.jpg",
        "thirdmisc_price": 65
        })

    ThirdMisc.create({
        "thirdmisc_name": "Corsair LL120 RGB",
        "thirdmisc_img": "https://i.imgur.com/12YPspO.jpg",
        "thirdmisc_price": 119
    })

    ThirdMisc.create({
        "thirdmisc_name": "Corsair QL Series QL120",
        "thirdmisc_img": "https://i.imgur.com/2LQooGS.jpg",
        "thirdmisc_price": 109
    })

    ThirdMisc.create({
        "thirdmisc_name": "Noctua NF-A12x25 PWM",
        "thirdmisc_img": "https://i.imgur.com/LuV5XIb.jpg",
        "thirdmisc_price": 29
    })

    ThirdMisc.create({
        "thirdmisc_name": "NZXT Aer RGB 2 120mm",
        "thirdmisc_img": "https://i.imgur.com/mPf1kCL.jpg",
        "thirdmisc_price": 28
    })

    ThirdMisc.create({
        "thirdmisc_name": "Thermaltake ToughFan 12",
        "thirdmisc_img": "https://i.imgur.com/fZhhVIZ.jpg",
        "thirdmisc_price": 24
    })

    ThirdMisc.create({
        "thirdmisc_name": "Thermaltake ToughFan 14",
        "thirdmisc_img": "https://i.imgur.com/dJbIWKT.jpg",
        "thirdmisc_price": 34
    })

    ThirdMisc.create({
        "thirdmisc_name": "Scythe Kaze Flex 120 PWM",
        "thirdmisc_img": "https://i.imgur.com/oKXNz5t.jpg",
        "thirdmisc_price": 14
    })

    ThirdMisc.create({
        "thirdmisc_name": "be quiet! Silent Wings 3",
        "thirdmisc_img": "https://i.imgur.com/I3McZ0S.jpg",
        "thirdmisc_price": 25
    })