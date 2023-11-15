from dataclasses import dataclass
from enum import Enum
from datetime import date


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(Enum):
    sport = 'Sport'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    birth_date: date
    subjects: list
    hobbies: list
    upload_filename: str
    address: str
    state: str
    city: str

    @property
    def subjects_str(self):
        return ", ".join(self.subjects)

    @property
    def hobbies_str(self):
        return ", ".join(self.hobbies)


user = User(
    first_name='Natali',
    last_name='Ivanova',
    email='fortest@gmail.com',
    gender=Gender.female.value,
    mobile='9995557777',
    birth_date=date(2000, 10, 1),
    subjects=['Maths', 'Physics'],
    hobbies=[Hobby.sport, Hobby.music],
    upload_filename='IMG_1.jpg',
    address='1-street, 7-house, 7-apartment',
    state='NCR',
    city='Delhi')
