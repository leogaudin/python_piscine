import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates an ID of random chars.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """The class representing a Student.
    """
    name: str = field(init=True, repr=True)
    surname: str = field(init=True, repr=True)
    active: bool = field(init=False, repr=True, default=True)
    login: bool = field(init=False, repr=True)
    id: str = field(init=False, repr=True, default=generate_id())

    def __post_init__(self):
        self.login = self.name[:1] + self.surname[0:]
