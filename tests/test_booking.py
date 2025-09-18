from models.booking import  CreateBookingResponse
from src.constant import BookingData


def test_created_booking(created_booking):
    try:
        result = CreateBookingResponse(**created_booking)
    except Exception as e:
        raise AssertionError(f"Структура не соотвествует данным: {e}")
    assert result.booking.bookingdates.checkin == "2025-01-01"
    assert created_booking['booking']['firstname'] == BookingData.FIRSTNAME.value
    assert created_booking['booking']['lastname'] == BookingData.LASTNAME.value


def test_update_booking(booking_clients, created_booking, auth_token, headers, valid_booking_payload):
    booking_id = created_booking['bookingid']
    headers.update({f"Cookie":f"token={auth_token}"})
    result = valid_booking_payload.build()
    result.update({"firstname": BookingData.UPDATES_FIRSTNAME.value, "lastname": BookingData.UPDATES_LASTNAME.value})
    update_response = booking_clients.update_booking(booking_id, result, headers)
    assert update_response.json()['firstname'] == BookingData.UPDATES_FIRSTNAME.value
    assert update_response.json()['lastname'] == BookingData.UPDATES_LASTNAME.value


def test_get_booking_id(booking_clients, auth_token, valid_booking_payload, params, headers):
    created_booking_ids = []
    for i in range(3):
        result = booking_clients.create_booking(valid_booking_payload.build(), headers=headers).json()
        created_booking_ids.append(result['bookingid'])
    result = booking_clients.get_booking_ids(params=params).json()
    get_booking_ids = [item['bookingid'] for item in result]
    headers.update({"Cookie": f"token={auth_token}"})
    for item in created_booking_ids:
        booking_clients.delete_booking(booking_id=item, headers=headers)
    assert sorted(created_booking_ids) == sorted(get_booking_ids)
