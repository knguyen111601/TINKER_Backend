"""CPUTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.CPU import CPU

class CPUTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        # # AMD
        # CPU.create({
        #     "cpu_name": "AMD Ryzen 9 5950X",
        #     "cpu_price": 799,
        #     "cpu_img": "https://i.imgur.com/RSq9kDV.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 9 5900X",
        #     "cpu_price": 549,
        #     "cpu_img": "https://i.imgur.com/RSq9kDV.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 7 5800X",
        #     "cpu_price": 449,
        #     "cpu_img": "https://i.imgur.com/pXJutac.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 5 5600X",
        #     "cpu_price": 299,
        #     "cpu_img": "https://i.imgur.com/qTJ0S8x.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 9 3950X",
        #     "cpu_price": 749,
        #     "cpu_img": "https://i.imgur.com/eFxkkYd.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 9 3900XT",
        #     "cpu_price": 499,
        #     "cpu_img": "https://i.imgur.com/eFxkkYd.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 9 3900X",
        #     "cpu_price": 499,
        #     "cpu_img": "https://i.imgur.com/eFxkkYd.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 7 3800XT",
        #     "cpu_price": 399,
        #     "cpu_img": "https://i.imgur.com/AdtCxhe.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 7 3800X",
        #     "cpu_price": 399,
        #     "cpu_img": "https://i.imgur.com/AdtCxhe.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 7 3700X",
        #     "cpu_price": 329,
        #     "cpu_img": "https://i.imgur.com/AdtCxhe.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 5 3600XT",
        #     "cpu_price": 249,
        #     "cpu_img": "https://i.imgur.com/broSYAB.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "AMD Ryzen 5 3600X",
        #     "cpu_price": 249,
        #     "cpu_img": "https://i.imgur.com/broSYAB.jpg"
        # })


        # # Intel 
        # CPU.create({
        #     "cpu_name": "Intel Core i9-12900K",
        #     "cpu_price": 589,
        #     "cpu_img": "https://i.imgur.com/WKiFW61.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "Intel Core i7-12700K",
        #     "cpu_price": 409,
        #     "cpu_img": "https://i.imgur.com/Ili56q3.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "Intel Core i5-12600K",
        #     "cpu_price": 289,
        #     "cpu_img": "https://i.imgur.com/1eezShH.jpg"
        # })

        # # Intel 11th Gen
        # CPU.create({
        #     "cpu_name": "Intel Core i9-11900K",
        #     "cpu_price": 539,
        #     "cpu_img": "https://i.imgur.com/0gzoQft.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "Intel Core i9-11900KF",
        #     "cpu_price": 513,
        #     "cpu_img": "https://i.imgur.com/0gzoQft.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "Intel Core i7-11700K",
        #     "cpu_price": 399,
        #     "cpu_img": "https://i.imgur.com/NIuS3sN.jpg"
        # })
    
        # CPU.create({
        #     "cpu_name": "Intel Core i7-11700KF",
        #     "cpu_price": 374,
        #     "cpu_img": "https://i.imgur.com/NIuS3sN.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "Intel Core i5-11600K",
        #     "cpu_price": 262,
        #     "cpu_img": "https://i.imgur.com/WJHrhPI.jpg"
        # })

        # CPU.create({
        #     "cpu_name": "Intel Core i5-11600KF",
        #     "cpu_price": 237,
        #     "cpu_img": "https://i.imgur.com/WJHrhPI.jpg"
        # })

        CPU.create({
            "cpu_name": "blank",
            "cpu_price": 0,
            "cpu_img": "blank"
        })