"""SecondStorageTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.SecondStorage import SecondStorage

class SecondStorageTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
# NVMe

        # SecondStorage.create({
        #     "secondstorage_name": "WD Black SN850",
        #     "secondstorage_brand": "Western Digital",
        #     "secondstorage_type": "NVMe SSD",
        #     "secondstorage_size": "1TB",
        #     "secondstorage_price": 164,
        #     "secondstorage_img": "https://i.imgur.com/QJVjs8j.jpg"
        # })

        # SecondStorage.create({
        #     "secondstorage_name": "Samsung 970 Evo Plus",
        #     "secondstorage_brand": "Samsung",
        #     "secondstorage_type": "NVMe SSD",
        #     "secondstorage_size": "1TB",
        #     "secondstorage_price": 138,
        #     "secondstorage_img": "https://i.imgur.com/lhV4mhF.jpg"
        # })

        # SecondStorage.create({
        #     "secondstorage_name": "Sabrent Rocket 4 Plus",
        #     "secondstorage_brand": "Sabrent",
        #     "secondstorage_type": "NVMe SSD",
        #     "secondstorage_size": "1TB",
        #     "secondstorage_price": 159,
        #     "secondstorage_img": "https://i.imgur.com/Ax9v8w4.jpg"
        # })

        # SecondStorage.create({
        #     "secondstorage_name": "Samsung 980 Pro",
        #     "secondstorage_brand": "Samsung",
        #     "secondstorage_type": "NVMe SSD",
        #     "secondstorage_size": "1TB",
        #     "secondstorage_price": 184,
        #     "secondstorage_img": "https://i.imgur.com/HEWuIQF.jpg"
        # })

        # SecondStorage.create({
        #     "secondstorage_name": "Crucial P5 Plus",
        #     "secondstorage_brand": "Crucial",
        #     "secondstorage_type": "NVMe SSD",
        #     "secondstorage_size": "1TB",
        #     "secondstorage_price": 149,
        #     "secondstorage_img": "https://i.imgur.com/XI7G1bA.jpg"
        # })

        # # SATA SSD
        # SecondStorage.create({
        #     "secondstorage_name": "Samsung 870 EVO",
        #     "secondstorage_brand": "Samsung",
        #     "secondstorage_type": "SATA SSD",
        #     "secondstorage_size": "1TB",
        #     "secondstorage_price": 119,
        #     "secondstorage_img": "https://i.imgur.com/N2CWMLW.jpg"
        # })

        # SecondStorage.create({
        #     "secondstorage_name": "Crucial MX500",
        #     "secondstorage_brand": "Crucial",
        #     "secondstorage_type": "SATA SSD",
        #     "secondstorage_size": "1TB",
        #     "secondstorage_price": 99,
        #     "secondstorage_img": "https://i.imgur.com/MUvepKg.jpg"
        # })

        SecondStorage.create({
            "secondstorage_name": "blank",
            "secondstorage_brand": "blank",
            "secondstorage_type": "blank",
            "secondstorage_size": "0",
            "secondstorage_price": 0,
            "secondstorage_img": "blank"
        })