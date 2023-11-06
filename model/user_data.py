from dataclasses import dataclass
from enum import Enum


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
    gender: str
    mobile: int
    birth_year: str
    birth_month: str
    birth_day: str
    subjects: Subject
    hobbies: Hobby
    upload_filename: str
    address: str
    state: str
    city: str
