"""GPUTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.GPU import GPU

class GPUTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        #  RTX 3090
        GPU.create({
            "gpu_brand": "ASUS",
            "gpu_name": "ASUS RTX 3090 ROG STRIX Gaming OC",
            "gpu_price": 1800,
            "gpu_img": "https://i.imgur.com/kZFLWVk.jpg"
        })

        GPU.create({
            "gpu_brand": "ASUS",
            "gpu_name": "ASUS RTX 3090 TUF Gaming & TUF Gaming OC",
            "gpu_price": 1599,
            "gpu_img": "https://i.imgur.com/W5FkoGs.jpg"
        })

        GPU.create({
            "gpu_brand": "EVGA",
            "gpu_name": "EVGA RTX 3090 XC3 Ultra",
            "gpu_price": 1739,
            "gpu_img": "https://i.imgur.com/4ADApD4.jpg"
        })

        GPU.create({
            "gpu_brand": "EVGA",
            "gpu_name": "EVGA RTX 3090 FTW3 Ultra",
            "gpu_price": 1800,
            "gpu_img": "https://i.imgur.com/TCpdzfJ.jpg"
        })

        # RTX 3080

        GPU.create({
            "gpu_brand": "ASUS",
            "gpu_name": "ASUS RTX 3080 ROG STRIX Gaming OC",
            "gpu_price": 850,
            "gpu_img": "https://i.imgur.com/kZFLWVk.jpg"
        })

        GPU.create({
            "gpu_brand": "ASUS",
            "gpu_name": "ASUS RTX 3080 TUF Gaming OC",
            "gpu_price": 729,
            "gpu_img": "https://i.imgur.com/W5FkoGs.jpg"
        })

        GPU.create({
            "gpu_brand": "EVGA",
            "gpu_name": "EVGA RTX 3080 XC3 Ultra",
            "gpu_price": 779,
            "gpu_img": "https://i.imgur.com/BW0dpYg.jpg"
        })

        GPU.create({
            "gpu_brand": "EVGA",
            "gpu_name": "EVGA RTX 3080 FTW3 Ultra",
            "gpu_price": 810,
            "gpu_img": "https://i.imgur.com/TCpdzfJ.jpg"
        })

        GPU.create({
            "gpu_brand": "GIGABYTE",
            "gpu_name": "GIGABYTE RTX 3080 Eagle OC",
            "gpu_price": 1229,
            "gpu_img": "https://i.imgur.com/lQ2rsEC.jpg"
        })

        GPU.create({
            "gpu_brand": "MSI",
            "gpu_name": "MSI RTX 3080 VENTUS 3X OC",
            "gpu_price": 1069,
            "gpu_img": "https://i.imgur.com/Wb4RR3U.jpg"
        })

        GPU.create({
            "gpu_brand": "MSI",
            "gpu_name": "MSI RTX 3080 Gaming X TRIO",
            "gpu_price": 1489,
            "gpu_img": "https://i.imgur.com/7RlIAwH.jpg"
        })

        # 3070

        GPU.create({
            "gpu_brand": "EVGA",
            "gpu_name": "EVGA RTX 3070 FTW3 Ultra",
            "gpu_price": 610,
            "gpu_img": "https://i.imgur.com/TCpdzfJ.jpg"
        })

        GPU.create({
            "gpu_brand": "EVGA",
            "gpu_name": "EVGA RTX 3070 XC3 Ultra",
            "gpu_price": 609,
            "gpu_img": "https://i.imgur.com/3OAyOnS.jpg"
        })

        GPU.create({
            "gpu_brand": "ZOTAC",
            "gpu_name": "ZOTAC RTX 3070 Twin Edge (Gray)",
            "gpu_price": 619,
            "gpu_img": "https://i.imgur.com/BQKEOTS.jpg"
        })

        GPU.create({
            "gpu_brand": "ZOTAC",
            "gpu_name": "ZOTAC RTX 3070 Twin Edge (White)",
            "gpu_price": 619,
            "gpu_img": "https://i.imgur.com/aLG6mQa.jpg"
        })

        # RX 6900XT
        GPU.create({
            "gpu_brand": "PowerColor",
            "gpu_name": "PowerColor Red Devil Radeon RX 6900 XT",
            "gpu_price": 1599,
            "gpu_img": "https://i.imgur.com/wMlTFpm.jpg"
        })

        GPU.create({
            "gpu_brand": "Sapphire",
            "gpu_name": "Sapphire Nitro+ Radeon RX 6900 XT",
            "gpu_price": 1549,
            "gpu_img": "https://i.imgur.com/8wqnB8T.jpg"
        })

        GPU.create({
            "gpu_brand": "XFX",
            "gpu_name": "XFX Speedster MERC319 RX 6900 XT",
            "gpu_price": 1999,
            "gpu_img": "https://i.imgur.com/IX0yfUX.jpg"
        })

        GPU.create({
            "gpu_brand": "ASUS",
            "gpu_name": "ASUS TUF Gaming Radeon RX 6900 XT OC",
            "gpu_price": 1599,
            "gpu_img": "https://i.imgur.com/AM681f1.jpg"
        })

        # RX 6900XT

        GPU.create({
            "gpu_brand": "PowerColor",
            "gpu_name": "PowerColor Red Devil Radeon RX 6800 XT",
            "gpu_price": 800,
            "gpu_img": "https://i.imgur.com/ACKJNeR.jpg"
        })

        GPU.create({
            "gpu_brand": "Sapphire",
            "gpu_name": "Sapphire Nitro+ RX 6800 XT",
            "gpu_price": 770,
            "gpu_img": "https://i.imgur.com/Lf9As1a.jpg"
        })

        GPU.create({
            "gpu_brand": "XFX",
            "gpu_name": "XFX Speedster MERC319 RX 6800 XT",
            "gpu_price": 800,
            "gpu_img": "https://i.imgur.com/IX0yfUX.jpg"
        })

        GPU.create({
            "gpu_brand": "ASUS",
            "gpu_name": "ASUS TUF Gaming Radeon RX 6800 XT OC",
            "gpu_price": 809,
            "gpu_img": "https://i.imgur.com/AM681f1.jpg"
        })

