# __init__.py

class House:
    def __init__(self, address, price, num_rooms):
        self.address = address
        self.price = price
        self.num_rooms = num_rooms

    def __repr__(self):
        return f"House(address={self.address}, price={self.price}, num_rooms={self.num_rooms})"

class Review:
    def __init__(self, house, user, rating, comment):
        self.house = house
        self.user = user
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return f"Review(house={self.house}, user={self.user}, rating={self.rating}, comment={self.comment})"

class Booking:
    def __init__(self, house, user, start_date, end_date):
        self.house = house
        self.user = user
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"Booking(house={self.house}, user={self.user}, start_date={self.start_date}, end_date={self.end_date})"

# Define any package-level variables or functions if necessary
PACKAGE_VERSION = "1.0.0"

__all__ = ["House", "Review", "Booking"]
