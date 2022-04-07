from dataclasses import dataclass
from datetime import datetime
from pyexpat import model

@dataclass 
class Processor:
    model: str
    company: str
    release_year: datetime

    @staticmethod
    def fresh_status(first_data, second_data):
        if first_data >= second_data:
            print('This processor is fresh')
        else:
            print('Hm, see more actuality model')
    
    @classmethod
    def change_release_year(cls):
        cls.release_year: str


intel_i7 = Processor('Coffee Lake i7', 'Intel', 2018)
intel_i9 = Processor('Rocket Lake i9', 'Intel', 2021)

print(Processor.fresh_status(intel_i7.release_year, intel_i9.release_year))

# Понимаю, что высосано из пальца. Хз, как правильнее в dataclass его использовать

Processor.change_release_year
