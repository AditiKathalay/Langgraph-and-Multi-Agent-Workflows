from datetime import datetime

class TravelPlanner:
    def __init__(self, city: str, start_date: str, end_date: str):
        self.city = city
        self.start_date = start_date
        self.end_date = end_date
        self.trip_days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days + 1