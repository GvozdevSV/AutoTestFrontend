from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    first_name: str = None
    last_name: str = None
    age: int = None
    salary: int = None
    department: int = None
    mobile_namber: int = None


@dataclass
class Colors:
    color_name: list = None


@dataclass
class Date:
    year: str = None
    month: str = None
    day: str = None
    time: str = None
