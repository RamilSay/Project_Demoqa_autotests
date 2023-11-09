from dataclasses import dataclass
from enum import Enum
from datetime import date


class Gender(Enum):
    male = 'Male'
    female = 'Female'


class Subject(Enum):
    maths = 'Maths'
    physics = 'Physics'


class Hobby(Enum):
    sport = 'Sport'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: int
    birth_year: str
    birth_month: str
    birth_day: str
    subjects: list[Subject]
    hobbies: list[Hobby]
    upload_filename: str
    address: str
    state: str
    city: str


student = User(
    'Natali',
    'Ivanova',
    'fortest@gmail.com',
    Gender.female.value,
    '9995557777',
    date(2000, 11, 1),
    Subject.maths.physics,
    Hobby.sport.music,
    'IMG_1.jpg',
    '1-street, 7-house, 7-apartment',
    'NCR Delhi')
