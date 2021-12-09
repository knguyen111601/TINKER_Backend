"""ThirdStorageTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.ThirdStorage import ThirdStorage

class ThirdStorageTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        ThirdStorage.create({
            "thirdstorage_name": "blank",
            "thirdstorage_brand": "blank",
            "thirdstorage_type": "blank",
            "thirdstorage_size": "0",
            "thirdstorage_price": 0,
            "thirdstorage_img": "blank"
        })
        # NVMe

        ThirdStorage.create({
            "thirdstorage_name": "WD Black SN850",
            "thirdstorage_brand": "Western Digital",
            "thirdstorage_type": "NVMe SSD",
            "thirdstorage_size": "1TB",
            "thirdstorage_price": 164,
            "thirdstorage_img": "https://i.imgur.com/QJVjs8j.jpg"
        })

        ThirdStorage.create({
            "thirdstorage_name": "Samsung 970 Evo Plus",
            "thirdstorage_brand": "Samsung",
            "thirdstorage_type": "NVMe SSD",
            "thirdstorage_size": "1TB",
            "thirdstorage_price": 138,
            "thirdstorage_img": "https://i.imgur.com/lhV4mhF.jpg"
        })

        ThirdStorage.create({
            "thirdstorage_name": "Sabrent Rocket 4 Plus",
            "thirdstorage_brand": "Sabrent",
            "thirdstorage_type": "NVMe SSD",
            "thirdstorage_size": "1TB",
            "thirdstorage_price": 159,
            "thirdstorage_img": "https://i.imgur.com/Ax9v8w4.jpg"
        })

        ThirdStorage.create({
            "thirdstorage_name": "Samsung 980 Pro",
            "thirdstorage_brand": "Samsung",
            "thirdstorage_type": "NVMe SSD",
            "thirdstorage_size": "1TB",
            "thirdstorage_price": 184,
            "thirdstorage_img": "https://i.imgur.com/HEWuIQF.jpg"
        })

        ThirdStorage.create({
            "thirdstorage_name": "Crucial P5 Plus",
            "thirdstorage_brand": "Crucial",
            "thirdstorage_type": "NVMe SSD",
            "thirdstorage_size": "1TB",
            "thirdstorage_price": 149,
            "thirdstorage_img": "https://i.imgur.com/XI7G1bA.jpg"
        })

        # SATA SSD
        ThirdStorage.create({
            "thirdstorage_name": "Samsung 870 EVO",
            "thirdstorage_brand": "Samsung",
            "thirdstorage_type": "SATA SSD",
            "thirdstorage_size": "1TB",
            "thirdstorage_price": 119,
            "thirdstorage_img": "https://i.imgur.com/N2CWMLW.jpg"
        })

        ThirdStorage.create({
            "thirdstorage_name": "Crucial MX500",
            "thirdstorage_brand": "Crucial",
            "thirdstorage_type": "SATA SSD",
            "thirdstorage_size": "1TB",
            "thirdstorage_price": 99,
            "thirdstorage_img": "https://i.imgur.com/MUvepKg.jpg"
        })

