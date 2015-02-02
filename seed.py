
from pony.orm import db_session
from IFK.Models.models import Member,Section


with db_session:

    olle = Member(name="Olle", phone='260088')
    stina = Member(name="Stina", phone='282677')
    saddam = Member(name="Saddam", phone='260088')
    lotta = Member(name="Lotta", phone='174590')

    Bowling = Section(code="A", name="Bowling", leader=lotta)
    Simning = Section(code="C", name="Simning", leader=stina)
    Kickboxing = Section(code="B", name="Kickboxing", leader=lotta)

    Bowling.members = [olle, saddam]
    Kickboxing.members = [olle]
    Simning.members = [olle, stina]


