# api_code/dummy_data.py
from datetime import datetime, timedelta, timezone
from pathlib import Path
from random import choice, randint, random

from api.models import (
    Base,
    Classes,
    Roles,
    Station,
    Ticket,
    Train,
    User,
)
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///train.db"
engine = create_engine(DB_URL)


def new_db(filename):
    db_file = Path(filename)
    db_file.unlink(missing_ok=True)

    # then create a fresh DB
    Base.metadata.create_all(engine)


if __name__ == "__main__":

    new_db("train.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    # USERS

    NUM_USERS = 100
    NUM_TICKETS = 300
    NUM_TRAINS = 300

    class_choices = [c for c in Classes]

    users = [
        User(
            id=0,
            full_name="Fabrizio Romano",
            email="fabrizio.romano@example.com",
            password=User.hash_password("f4bPassword"),
            role=Roles.admin,
        )
    ]

    for user_id in range(1, NUM_USERS + 1):
        users.append(
            User(
                id=user_id,
                full_name=fake.name(),
                email=fake.safe_email(),
                password=User.hash_password(fake.password()),
                role=Roles.passenger,
            )
        )

    session.bulk_save_objects(users)
    session.commit()

    # STATIONS

    stations = [
        Station(id=0, code="ROM", country="Italy", city="Rome"),
        Station(id=1, code="PAR", country="France", city="Paris"),
        Station(id=2, code="LDN", country="UK", city="London"),
        Station(id=3, code="KYV", country="Ukraine", city="Kyiv"),
        Station(
            id=4, code="STK", country="Sweden", city="Stockholm"
        ),
        Station(
            id=5, code="WSW", country="Poland", city="Warsaw"
        ),
        Station(
            id=6, code="MSK", country="Russia", city="Moskow"
        ),
        Station(
            id=7,
            code="AMD",
            country="Netherlands",
            city="Amsterdam",
        ),
        Station(
            id=8, code="EDB", country="Scotland", city="Edinburgh"
        ),
        Station(
            id=9, code="BDP", country="Hungary", city="Budapest"
        ),
        Station(
            id=10, code="BCR", country="Romania", city="Bucharest"
        ),
        Station(
            id=11, code="SFA", country="Bulgaria", city="Sofia"
        ),
    ]

    session.bulk_save_objects(stations)
    session.commit()

    # TRAINS

    trains = []
    now = datetime.now(tz=timezone.utc)
    HOUR = 60 * 60
    DAY = 24 * HOUR
    TEN_DAYS = 10 * DAY

    for train_id in range(NUM_TRAINS):
        station_ids = list(range(len(stations)))
        station_from = choice(station_ids)
        station_ids.remove(station_from)
        station_to = choice(station_ids)

        name = f"{stations[station_from].city} -> {stations[station_to].city}"
        departure = now + timedelta(
            seconds=randint(-TEN_DAYS, TEN_DAYS)
        )
        arrival = departure + timedelta(
            seconds=randint(HOUR, DAY)
        )

        trains.append(
            Train(
                id=train_id,
                name=name,
                station_from_id=station_from,
                station_to_id=station_to,
                departs_at=departure,
                arrives_at=arrival,
                first_class=randint(0, 5),
                second_class=randint(1, 10),
                seats_per_car=choice([10, 25, 40]),
            )
        )

    session.bulk_save_objects(trains)
    session.commit()

    # TICKETS

    tickets = []
    classes = [c for c in Classes]
    MIN_PRICE = 5
    MAX_PRICE = 200

    for ticket_id in range(NUM_TICKETS):
        price = round(
            float(randint(MIN_PRICE, MAX_PRICE))
            + randint(0, 1) * random(),
            2,
        )
        tickets.append(
            Ticket(
                id=ticket_id,
                created_at=now
                + timedelta(seconds=randint(-TEN_DAYS, -HOUR)),
                user_id=choice(
                    range(len(users) - 1)
                ),  # last user has no tickets
                train_id=choice(
                    range(len(trains) - 1)
                ),  # last train has no tickets
                price=price,
                car_class=choice(classes),
            )
        )

    session.bulk_save_objects(tickets)
    session.commit()

    print("done")
