from datetime import datetime

from .app import db
from .app.models import Contact, ContactGroup, Gender
import secrets


def get_random_name(names_list, size=1):
    name_lst = [
        names_list[secrets.SystemRandom().randrange(0, len(names_list))].decode("utf-8").capitalize()
        for i in range(0, size)
    ]
    return " ".join(name_lst)


try:
    db.session.add(ContactGroup(name="Friends"))
    db.session.add(ContactGroup(name="Family"))
    db.session.add(ContactGroup(name="Work"))
    db.session.commit()
except:
    db.session.rollback()

try:
    db.session.add(Gender(name="Male"))
    db.session.add(Gender(name="Female"))
    db.session.commit()
except:
    db.session.rollback()

f = open("NAMES.DIC", "rb")
names_list = [x.strip() for x in f.readlines()]

f.close()

for i in range(1, 50):
    c = Contact()
    c.name = get_random_name(names_list, secrets.SystemRandom().randrange(2, 6))
    c.address = "Street " + names_list[secrets.SystemRandom().randrange(0, len(names_list))].decode(
        "utf-8"
    )
    c.personal_phone = secrets.SystemRandom().randrange(1111111, 9999999)
    c.personal_celphone = secrets.SystemRandom().randrange(1111111, 9999999)
    c.contact_group_id = secrets.SystemRandom().randrange(1, 4)
    c.gender_id = secrets.SystemRandom().randrange(1, 3)
    year = secrets.SystemRandom().choice(range(1900, 2012))
    month = secrets.SystemRandom().choice(range(1, 12))
    day = secrets.SystemRandom().choice(range(1, 28))
    c.birthday = datetime(year, month, day)
    db.session.add(c)
    try:
        db.session.commit()
        print("inserted {0}".format(c))
    except Exception as e:
        db.session.rollback()
