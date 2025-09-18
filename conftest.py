import pytest

from clients.booking_clients import BookingClient
from models.booking import Booking, BookingDates, GetParams
from src.constant import BookingData

from src.settings import settings


@pytest.fixture
def booking_clients():
    return BookingClient(base_url=settings.base_url)


@pytest.fixture
def valid_booking_payload():
    return Booking(
        firstname=BookingData.FIRSTNAME.value,
        lastname=BookingData.LASTNAME.value,
        totalprice=1000,
        depositpaid=True,
        bookingdates=BookingDates(
            checkin="2025-01-01",
            checkout="2025-01-01"
        ),
        additionalneeds="Breakfast"
    )



@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}



@pytest.fixture
def created_booking(booking_clients, valid_booking_payload, headers, auth_token):
    response = booking_clients.create_booking(valid_booking_payload.build(), headers=headers)
    data = response.json()
    yield data
    headers.update({"Cookie": f"token={auth_token}"})
    print(booking_clients.delete_booking(data['bookingid'], headers))


@pytest.fixture
def auth_token(booking_clients):
    response = booking_clients.get_token()
    data = response.json()
    return data['token']

def test_token(auth_token):
    print(auth_token)


@pytest.fixture
def params():
    return GetParams(
        firstname=BookingData.FIRSTNAME.value
        ).build()

def test_params(params):
    print(params)

@pytest.fixture
def get_booking_fixture(booking_clients,params):
    print(params)
    response = booking_clients.get_booking_ids(params=params)
    return response.json()





