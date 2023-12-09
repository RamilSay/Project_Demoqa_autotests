from dataclasses import dataclass
from enum import StrEnum
from datetime import date
from typing import List


class Gender(StrEnum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(StrEnum):
    SPORTS = 'Sports'
    MUSIC = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    birth_date: date
    subjects: list
    hobbies: List[Hobby]
    upload_filename: str
    address: str
    state: str
    city: str

    @property
    def birth_date_str(self):
        return self.birth_date.strftime('%d %B,%Y')

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
    gender=Gender.female,
    mobile='9995557777',
    birth_date=date(2000, 11, 1),
    subjects=['Maths', 'Physics'],
    hobbies=[Hobby.SPORTS, Hobby.MUSIC],
    upload_filename='IMG_1.jpg',
    address='1-street, 7-house, 7-apartment',
    state='NCR',
    city='Delhi')
