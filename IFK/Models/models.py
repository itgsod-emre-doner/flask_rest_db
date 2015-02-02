from pony.orm import PrimaryKey, Required, Set,Optional
from IFK import db



class Member(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    phone = Optional(str, nullable=True)

    sections = Set("Section", reverse="leader")
    sectionsMember = Set("Section", reverse="members")

class Section(db.Entity):
    code = PrimaryKey(str)
    name = Required(str)
    leader = Required(Member, reverse="sections")

    members = Set(Member, reverse="sectionsMember")




