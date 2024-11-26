import pathlib

from enum import StrEnum

PathList = list[pathlib.Path]
HashDict = dict[str, PathList]


class UserResponse(StrEnum):
    YES = 'yes'
    NO = 'no'
    CANCEL = 'cancel'
    ALL = 'all'
