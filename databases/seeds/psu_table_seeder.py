"""PSUTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.PSU import PSU

class PSUTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        # # SFX

        # PSU.create({
        #     "psu_name": "EVGA SuperNOVA 650GM",
        #     "psu_type": "SFX",
        #     "psu_watts": "650w",
        #     "psu_rating": "https://i.imgur.com/D2scG0d.png",
        #     "psu_price": 129,
        #     "psu_img": "https://i.imgur.com/Txeyd24.jpg"
        # })

        # PSU.create({
        #     "psu_name": "Corsair SF450",
        #     "psu_type": "SFX",
        #     "psu_watts": "450w",
        #     "psu_rating": "https://i.imgur.com/D2scG0d.png",
        #     "psu_price": 84,
        #     "psu_img": "https://i.imgur.com/LnCO6Fk.jpg"
        # })

        # PSU.create({
        #     "psu_name": "Corsair SF600",
        #     "psu_type": "SFX",
        #     "psu_watts": "600w",
        #     "psu_rating": "https://i.imgur.com/D2scG0d.png",
        #     "psu_price": 104,
        #     "psu_img": "https://i.imgur.com/ZY6j6EZ.jpg"
        # })

        # PSU.create({
        #     "psu_name": "Corsair SF750",
        #     "psu_type": "SFX",
        #     "psu_watts": "600w",
        #     "psu_rating": "https://i.imgur.com/sPQ8toE.png",
        #     "psu_price": 178,
        #     "psu_img": "https://i.imgur.com/gGcn9bD.jpg"
        # })

        # PSU.create({
        #     "psu_name": "SilverStone ST45SF-V3",
        #     "psu_type": "SFX",
        #     "psu_watts": "450w",
        #     "psu_rating": "https://i.imgur.com/Y9BQ6RQ.png",
        #     "psu_price": 136,
        #     "psu_img": "https://i.imgur.com/TkK50ea.jpg"
        # })

        # PSU.create({
        #     "psu_name": "Thermaltake Toughpower SFX450W",
        #     "psu_type": "SFX",
        #     "psu_watts": "450w",
        #     "psu_rating": "https://i.imgur.com/D2scG0d.png",
        #     "psu_price": 89,
        #     "psu_img": "https://i.imgur.com/DgkUQEY.jpg"
        # })

        # # ATX
        # PSU.create({
        #     "psu_name": "Corsair RM750x (Black)",
        #     "psu_type": "ATX",
        #     "psu_watts": "750w",
        #     "psu_rating": "https://i.imgur.com/D2scG0d.png",
        #     "psu_price": 119,
        #     "psu_img": "https://i.imgur.com/UzCzVI4.jpg"
        # })

        # PSU.create({
        #     "psu_name": "Corsair RM750x (White)",
        #     "psu_type": "ATX",
        #     "psu_watts": "750w",
        #     "psu_rating": "https://i.imgur.com/D2scG0d.png",
        #     "psu_price": 119,
        #     "psu_img": "https://i.imgur.com/h0fFSID.jpg"
        # })

        # PSU.create({
        #     "psu_name": "Thermaltake Toughpower Grand RGB 1050W Platinum",
        #     "psu_type": "ATX",
        #     "psu_watts": "1050w",
        #     "psu_rating": "https://i.imgur.com/sPQ8toE.png",
        #     "psu_price": 252,
        #     "psu_img": "https://i.imgur.com/1qA6b2I.jpg"
        # })

        # PSU.create({
        #     "psu_name": "Seasonic Prime Titanium TX-1000",
        #     "psu_type": "ATX",
        #     "psu_watts": "1000w",
        #     "psu_rating": "https://i.imgur.com/sPQ8toE.png",
        #     "psu_price": 299,
        #     "psu_img": "https://i.imgur.com/gvchDEZ.jpg"
        # })

        PSU.create({
            "psu_name": "blank",
            "psu_type": "blank",
            "psu_watts": "blank",
            "psu_rating": "blank",
            "psu_price": 0,
            "psu_img": "blank"
        })