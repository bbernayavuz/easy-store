from enum import Enum


class Status(Enum):
    CANCELED = 0
    WAITING = 1
    PAYMENT_WAITING = 2
    APPROVED = 3
    PREPARING = 4
    ONSHIPPING =5
    SHIPPED=6
    DELIVERED=7
    REFUNDED=8

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
