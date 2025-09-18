from pydantic import BaseModel
from typing import Optional



class BookingDates(BaseModel):
    checkin: str
    checkout: str

    def build(self):
        return self.model_dump()


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None

    def build(self):
        return self.model_dump()


class CreateBookingResponse(BaseModel):
    bookingid: int
    booking: Booking

    def build(self):
        return self.model_dump()


class GetParams(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    checkin: Optional[str] = None
    checkout: Optional[str] = None

    def build(self):
        return self.model_dump(exclude_none=True)


class BookingId(BaseModel):
    bookingid: int

    def build(self):
        return self.model_dump()