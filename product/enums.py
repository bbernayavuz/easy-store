from enum import Enum


class Gender(Enum):
    MALE = 0
    FEMALE = 1
    OTHER = 2

    # GENDER_TYPE = (
    #     (MALE, "Male"),
    #     (FEMALE, "Female"),
    #     (OTHER, "Other"),
    # )
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)









# class GenderValues(enum.Enum):
#     NONE = 0
#     MALE = 1
#     FEMALE = 2
#     BOTH = 3

# class Gender(models.Model):
#     gender = enum.EnumField(GenderValues, default=GenderValues.NONE)

#     def __str__(self):
#         return self.gender
