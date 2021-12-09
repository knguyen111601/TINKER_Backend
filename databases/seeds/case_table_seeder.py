"""CaseTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Case import Case

class CaseTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        # ITX / SFF
        
        Case.create({
            "case_name": "NZXT H210i (White)",
            "case_type": "ITX",
            "case_price": 118,
            "case_img": "https://i.imgur.com/IBNca2w.jpg",
        })

        Case.create({
            "case_name": "NZXT H210i (Black)",
            "case_type": "ITX",
            "case_price": 118,
            "case_img": "https://i.imgur.com/jZ0TQmi.jpg",
        })

        Case.create({
            "case_name": "Corsair Crystal 280X RGB (White)",
            "case_type": "ITX",
            "case_price": 149,
            "case_img": "https://i.imgur.com/Biliih9.jpg",
        })

        Case.create({
            "case_name": "Corsair Crystal 280X RGB (Black)",
            "case_type": "ITX",
            "case_price": 149,
            "case_img": "https://i.imgur.com/ahqbaLH.jpg",
        })

        Case.create({
            "case_name": "Phanteks Evolv Shift",
            "case_type": "ITX",
            "case_price": 99,
            "case_img": "https://i.imgur.com/R5WFELT.jpg",
        })

        Case.create({
            "case_name": "Lian Li Q58",
            "case_type": "ITX",
            "case_price": 156,
            "case_img": "https://i.imgur.com/1vW9aip.jpg",
        })

        Case.create({
            "case_name": "Cooler Master NR200P Max (White)",
            "case_type": "ITX",
            "case_price": 129,
            "case_img": "https://i.imgur.com/Fk745kO.jpg",
        })

        Case.create({
            "case_name": "Cooler Master NR200P Max (Black)",
            "case_type": "ITX",
            "case_price": 129,
            "case_img": "https://i.imgur.com/0Gi3UZF.jpg",
        })

        # Mid Tower

        Case.create({
            "case_name": "NZXT H710i (White)",
            "case_type": "Mid",
            "case_price": 197,
            "case_img": "https://i.imgur.com/USsclxO.jpg",
        })

        Case.create({
            "case_name": "NZXT H710i (Black)",
            "case_type": "Mid",
            "case_price": 197,
            "case_img": "https://i.imgur.com/88luDrA.jpg",
        })

        Case.create({
            "case_name": "Corsair Airflow 5000D (Black)",
            "case_type": "Mid",
            "case_price": 159,
            "case_img": "https://i.imgur.com/zjrgoEI.jpg",
        })

        Case.create({
            "case_name": "Corsair Airflow 5000D (White)",
            "case_type": "Mid",
            "case_price": 165,
            "case_img": "https://i.imgur.com/qcVUcrz.jpg",
        })

        Case.create({
            "case_name": "Lian Li Lancool II Mesh",
            "case_type": "Mid",
            "case_price": 183,
            "case_img": "https://i.imgur.com/mUPJDeT.jpg",
        })

        Case.create({
            "case_name": "NZXT H510 Elite (White)",
            "case_type": "Mid",
            "case_price": 175,
            "case_img": "https://i.imgur.com/dLQWlFW.jpg",
        })

        Case.create({
            "case_name": "NZXT H510 Elite (Black)",
            "case_type": "Mid",
            "case_price": 175,
            "case_img": "https://i.imgur.com/RSZDJkg.jpg",
        })