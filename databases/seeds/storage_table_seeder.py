"""StorageTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Storage import Storage

class StorageTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        # NVMe

        Storage.create({
            "storage_name": "WD Black SN850",
            "storage_brand": "Western Digital",
            "storage_type": "NVMe SSD",
            "storage_size": "1TB",
            "storage_price": 164,
            "storage_img": "https://i.imgur.com/QJVjs8j.jpg"
        })

        Storage.create({
            "storage_name": "Samsung 970 Evo Plus",
            "storage_brand": "Samsung",
            "storage_type": "NVMe SSD",
            "storage_size": "1TB",
            "storage_price": 138,
            "storage_img": "https://i.imgur.com/lhV4mhF.jpg"
        })

        Storage.create({
            "storage_name": "Sabrent Rocket 4 Plus",
            "storage_brand": "Sabrent",
            "storage_type": "NVMe SSD",
            "storage_size": "1TB",
            "storage_price": 159,
            "storage_img": "https://i.imgur.com/Ax9v8w4.jpg"
        })

        Storage.create({
            "storage_name": "Samsung 980 Pro",
            "storage_brand": "Samsung",
            "storage_type": "NVMe SSD",
            "storage_size": "1TB",
            "storage_price": 184,
            "storage_img": "https://i.imgur.com/HEWuIQF.jpg"
        })

        Storage.create({
            "storage_name": "Crucial P5 Plus",
            "storage_brand": "Crucial",
            "storage_type": "NVMe SSD",
            "storage_size": "1TB",
            "storage_price": 149,
            "storage_img": "https://i.imgur.com/XI7G1bA.jpg"
        })

        # SATA SSD
        Storage.create({
            "storage_name": "Samsung 870 EVO",
            "storage_brand": "Samsung",
            "storage_type": "SATA SSD",
            "storage_size": "1TB",
            "storage_price": 119,
            "storage_img": "https://i.imgur.com/N2CWMLW.jpg"
        })

        Storage.create({
            "storage_name": "Crucial MX500",
            "storage_brand": "Crucial",
            "storage_type": "SATA SSD",
            "storage_size": "1TB",
            "storage_price": 99,
            "storage_img": "https://i.imgur.com/MUvepKg.jpg"
        })