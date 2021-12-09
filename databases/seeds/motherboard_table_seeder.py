"""MotherboardTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Motherboard import Motherboard

class MotherboardTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        

        # AMD ITX
        Motherboard.create({
            "motherboard_size": "ITX",
            "motherboard_type": "B550",
            "motherboard_name": "ASUS ROG Strix B550-i",
            "motherboard_ram_slots": 2,
            "motherboard_price": 220,
            "motherboard_img": "https://i.imgur.com/mWWqwBL.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ITX",
            "motherboard_type": "B550",
            "motherboard_name": "MSI MPG B550I Gaming Edge WiFi",
            "motherboard_ram_slots": 2,
            "motherboard_price": 186,
            "motherboard_img": "https://i.imgur.com/OMEYfdM.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ITX",
            "motherboard_type": "B550",
            "motherboard_name": "ASRock B550M-ITX/AC",
            "motherboard_ram_slots": 2,
            "motherboard_price": 129,
            "motherboard_img": "https://i.imgur.com/Yv6IG1w.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ITX",
            "motherboard_type": "x570",
            "motherboard_name": "GIGABYTE X570 I AORUS Pro Wi-Fi",
            "motherboard_ram_slots": 2,
            "motherboard_price": 209,
            "motherboard_img": "https://i.imgur.com/8AhjE9O.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ITX",
            "motherboard_type": "x570",
            "motherboard_name": "ASUS ROG Strix X570-I Gaming",
            "motherboard_ram_slots": 2,
            "motherboard_price": 279,
            "motherboard_img": "https://i.imgur.com/gfmRTBI.jpg"
        })

        # AMD ATX
        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "x570",
            "motherboard_name": "Asus ROG Crosshair VIII Dark Hero",
            "motherboard_ram_slots": 4,
            "motherboard_price": 449,
            "motherboard_img": "https://i.imgur.com/bMi6Y7h.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "x570",
            "motherboard_name": "MSI MPG X570 Gaming Pro Carbon WIFI",
            "motherboard_ram_slots": 4,
            "motherboard_price": 264,
            "motherboard_img": "https://i.imgur.com/apoQ5qZ.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "x570",
            "motherboard_name": "Gigabyte X570S Aorus Master",
            "motherboard_ram_slots": 4,
            "motherboard_price": 389,
            "motherboard_img": "https://i.imgur.com/MyrrNaD.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "x570",
            "motherboard_name": "Asus ROG Crosshair VIII Hero (Wi-Fi)",
            "motherboard_ram_slots": 4,
            "motherboard_price": 254,
            "motherboard_img": "https://i.imgur.com/Ip4LqQk.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "x570",
            "motherboard_name": "Asus ROG Crosshair VIII Hero (Wi-Fi)",
            "motherboard_ram_slots": 4,
            "motherboard_price": 254,
            "motherboard_img": "https://i.imgur.com/Ip4LqQk.jpg"
        })

        # Z690 (12gen intel)
        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "Z690",
            "motherboard_name": "Asus ROG Crosshair VIII Hero (Wi-Fi)",
            "motherboard_ram_slots": 4,
            "motherboard_price": 599,
            "motherboard_img": "https://i.imgur.com/7G2JAdI.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "Z690",
            "motherboard_name": "Gigabyte Z690 Aorus Xtreme",
            "motherboard_ram_slots": 4,
            "motherboard_price": 899,
            "motherboard_img": "https://i.imgur.com/VTlUuUL.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "Z690",
            "motherboard_name": "MSI MPG Z690 Carbon WiFi DDR5",
            "motherboard_ram_slots": 4,
            "motherboard_price": 399,
            "motherboard_img": "https://i.imgur.com/HD4RM2D.jpg"
        })

        # Z590

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "Z590",
            "motherboard_name": "ASUS ROG Strix Z590-E Gaming",
            "motherboard_ram_slots": 4,
            "motherboard_price": 377,
            "motherboard_img": "https://i.imgur.com/Uf4JtEw.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "Z590",
            "motherboard_name": "Gigabyte Z590 AORUS ELITE AX",
            "motherboard_ram_slots": 4,
            "motherboard_price": 232,
            "motherboard_img": "https://i.imgur.com/YntumYn.jpg"
        })

        Motherboard.create({
            "motherboard_size": "ATX",
            "motherboard_type": "Z590",
            "motherboard_name": "NZXT N7 Z590",
            "motherboard_ram_slots": 4,
            "motherboard_price": 284,
            "motherboard_img": "https://i.imgur.com/p6cIycc.jpg"
        })