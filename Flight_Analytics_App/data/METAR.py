import httpx
from ..state import RouteState


def current_weather_status(origin_airport, destination_airport):

    origin_airport = httpx.get(
        "https://aviationweather.gov/api/data/metar",
        params={"ids": RouteState.source_airport, "format": "json"},
        headers={"User-Agent": "wx-test"},
        timeout=10,
    )

    destination_airport = httpx.get(
        "https://aviationweather.gov/api/data/metar",
        params={"ids": RouteState.dest_airport, "format": "json"},
        headers={"User-Agent": "wx-test"},
        timeout=10,
    )

    return (origin_airport.json()[0]["fltCat"]), (
        destination_airport.json()[0]["fltCat"]
    )
