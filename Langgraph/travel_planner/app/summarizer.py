from langchain_core.tools import tool
from datetime import datetime
from .tools.base_tools import (
    get_attractions_and_activities,
    get_weather_forecast,
    get_hotels_and_transport,
    generate_itinerary,
)

@tool
def summarize_trip(city: str, start_date: str, end_date: str) -> str:
    """One tool to summarize the entire trip, including attractions, weather, hotels, and itinerary."""
    trip_days = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days + 1
    attractions = get_attractions_and_activities(city)
    weather = get_weather_forecast(city, start_date, end_date)
    hotels = get_hotels_and_transport(city, trip_days)
    itinerary = generate_itinerary(city, start_date, end_date)

    return f"""
--- Trip Summary ---
🏙️ Attractions: {attractions}
🌦️ Weather: {weather}
🏨 Hotels: {hotels}
🗺️ Itinerary: {itinerary}
--------------------
""".strip()