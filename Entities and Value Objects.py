from pydantic import BaseModel
from typing import List, Optional

# Value Object: Seat
class Seat(BaseModel):
    seat_number: str
    seat_class: str  # e.g., Economy, Business

# Entity: Flight
class Flight(BaseModel):
    flight_id: int
    flight_number: str
    departure: str
    arrival: str
    seats: List[Seat]

# Entity: Booking (Aggregate Root)
class Booking(BaseModel):
    booking_id: int
    flight: Flight
    customer_name: str
    seats: List[Seat]
    total_price: float
