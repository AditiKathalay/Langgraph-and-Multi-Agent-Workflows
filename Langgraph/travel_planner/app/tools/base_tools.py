from langchain_core.tools import tool

@tool
def get_attractions_and_activities(city: str) -> str:
    """Get top attractions and activities for a given city."""
    return f"Top attractions and activities in {city} include..."

@tool
def get_weather_forecast(city: str, start_date: str, end_date: str) -> str:
    """Get weather forecast for a given city and date range."""
    return f"Weather in {city} from {start_date} to {end_date} will be..."

@tool
def get_hotels_and_transport(city: str, trip_days: int) -> str:
    """Estimate hotel and transport costs for the trip duration."""
    return f"Estimated hotel and transport cost in {city} for {trip_days} days is..."

@tool
def generate_itinerary(city: str, start_date: str, end_date: str) -> str:
    """Generate an itinerary plan for the travel duration."""
    return f"Day-wise itinerary for {city} from {start_date} to {end_date} is..."