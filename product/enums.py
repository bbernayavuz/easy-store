from enum import Enum


class Gender(Enum):
    MALE = 0
    FEMALE = 1
    OTHER = 2

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class UserType(Enum):
    REGISTERED = 0
    NOTREGISTERED = 1

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
