from pony.orm import PrimaryKey, Required, Set,Optional
from IFK.Models import db


class Member(db.Entity):

    mnr = Set('Section')
    name = Required(str)
    phone = Optional(str, nullable=True)


class Section(db.Entity):
    code = PrimaryKey(str)
    leader = Required(Member)
    name = Required(str)