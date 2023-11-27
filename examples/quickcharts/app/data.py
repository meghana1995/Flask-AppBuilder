import datetime
import logging

from . import db
from .models import Country, CountryStats, PoliticalType
import secrets

log = logging.getLogger(__name__)


def fill_data():
    countries = [
        "Portugal",
        "Germany",
        "Spain",
        "France",
        "USA",
        "China",
        "Russia",
        "Japan",
    ]
    politicals = ["Democratic", "Authorative"]
    for country in countries:
        c = Country(name=country)
        try:
            db.session.add(c)
            db.session.commit()
        except Exception as e:
            log.error("Update ViewMenu error: {0}".format(str(e)))
            db.session.rollback()
    for political in politicals:
        c = PoliticalType(name=political)
        try:
            db.session.add(c)
            db.session.commit()
        except Exception as e:
            log.error("Update ViewMenu error: {0}".format(str(e)))
            db.session.rollback()
    try:
        for x in range(1, 20):
            cs = CountryStats()
            cs.population = secrets.SystemRandom().randint(1, 100)
            cs.unemployed = secrets.SystemRandom().randint(1, 100)
            cs.college = secrets.SystemRandom().randint(1, 100)
            year = secrets.SystemRandom().choice(range(1900, 2012))
            month = secrets.SystemRandom().choice(range(1, 12))
            day = secrets.SystemRandom().choice(range(1, 28))
            cs.stat_date = datetime.datetime(year, month, day)
            cs.country_id = secrets.SystemRandom().randint(1, len(countries))
            cs.political_type_id = secrets.SystemRandom().randint(1, len(politicals))
            db.session.add(cs)
            db.session.commit()
    except Exception as e:
        log.error("Update ViewMenu error: {0}".format(str(e)))
        db.session.rollback()
