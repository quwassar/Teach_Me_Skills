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

class Power:
    default_average = '120 W'

    @classmethod
    def change_average(cls):
        cls.default_average = '240 W'
    

intel_i7 = Processor('Coffee Lake i7', 'Intel', 2018)
intel_i9 = Processor('Rocket Lake i9', 'Intel', 2021)

print(Processor.fresh_status(intel_i7.release_year, intel_i9.release_year))

power = Power()
print(power.default_average)

Power.change_average()

power_1 = Power()

print(power.default_average)


