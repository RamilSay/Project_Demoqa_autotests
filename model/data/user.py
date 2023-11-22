from dataclasses import dataclass
from enum import StrEnum
import datetime


class Gender(StrEnum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(StrEnum):
    Sports = 'Sports'
    Music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    birth_date: datetime.date
    subjects: list
    hobbies: list
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
    birth_date=datetime.date(2000, 10, 1),
    subjects=['Maths', 'Physics'],
    hobbies=[Hobby.Sports, Hobby.Music],
    upload_filename='IMG_1.jpg',
    address='1-street, 7-house, 7-apartment',
    state='NCR',
    city='Delhi')
