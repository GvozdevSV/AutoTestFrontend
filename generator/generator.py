import random

from data.data import Person, Colors, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('EN')
Faker.seed()
def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + "" + faker_ru.last_name() + "" + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(14,90),
        salary=random.randint(20000,100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile_namber=faker_ru.msisdn(),
    )
def generated_file():
    path = rf'C:\Users\ПК\PycharmProjects\AvtoTestFrontend\testfile{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path

def generated_color():
    yield Colors(
        color_name=['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Voilet', 'Indigo', 'Magenta', 'Aqua']
    )

def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:15"

    )