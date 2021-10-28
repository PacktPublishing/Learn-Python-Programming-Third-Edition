# HTTP queries

These are example queries that exercise the API.

Try all of them, especially those that create or delete resources,
should be tried twice, consecutively, so you can also see the error
messages that the API will return.

 *Note*: You must install [httpie](https://httpie.io) to run the
 queries below.


## Root

### GET

    http http://localhost:8000


## Users

### GET

    http http://localhost:8000/users

    http http://localhost:8000/users/0

    http http://localhost:8000/users/0/tickets

### POST

    http POST http://localhost:8000/users full_name="John Doe" email="john.doe@example.com" password="johndoe" role="passenger"

    http POST http://localhost:8000/users/authenticate email="fabrizio.romano@example.com" password="f4bPassword"

    http POST http://localhost:8000/users/validate_token token="..."

### PUT

    http PUT http://localhost:8000/users/101 full_name="Fabrizio Romano" email="fab109@example.com" password="something" role="admin"

Also available partial updates:

    http PUT http://localhost:8000/users/101 role="passenger"

### DELETE

    http DELETE http://localhost:8000/users/101


## Stations

### GET

    http http://localhost:8000/stations

    http http://localhost:8000/stations?code=LDN

    http http://localhost:8000/stations/0

    http http://localhost:8000/stations/0/departures

    http http://localhost:8000/stations/0/arrivals

### POST

    http POST http://localhost:8000/stations code=TMP country=Temporary-Country city=tmp-city

### PUT

    http PUT http://localhost:8000/stations/12 code=SMC country=Some-Country city=Some-city

Also available partial updates:

    http PUT http://localhost:8000/stations/12 code=xxx

### DELETE

    http DELETE http://localhost:8000/stations/12


## Trains

### GET

    http http://localhost:8000/trains

    http http://localhost:8000/trains?station_from_code=BCR
    http http://localhost:8000/trains?station_to_code=STK
    http "http://localhost:8000/trains?station_from_code=STK&station_to_code=AMD"
    http "http://localhost:8000/trains?station_from_code=STK&station_to_code=AMD&include_all=True"

    http http://localhost:8000/trains/0

### POST

    http POST http://localhost:8000/trains name="Pendolino" first_class=2 second_class=4 seats_per_car=8 station_from_id=0 station_to_id=3 arrives_at="2021-08-18T11:33:20" departs_at="2021-08-18T09:55:20"

### DELETE

    http DELETE http://localhost:8000/trains/300


## Tickets

### GET

    http http://localhost:8000/tickets

    http http://localhost:8000/tickets/0

### POST

    http POST http://localhost:8000/tickets user_id=0 train_id=0 price=19.84 car_class="first"

### DELETE

    http DELETE http://localhost:8000/tickets/300


## Admin

### GET

    http DELETE http://localhost:8000/admin/stations/10 Authorization:"Bearer admin.token.here"
