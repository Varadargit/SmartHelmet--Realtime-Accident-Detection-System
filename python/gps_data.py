"""
GPS Data Processing

This module handles GPS coordinate data received
from the embedded system.
"""


def create_google_maps_link(latitude, longitude):
    """
    Create a Google Maps link using real-time
    latitude and longitude.
    """

    return (
        f"https://maps.google.com/"
        f"?q={latitude},{longitude}"
    )


def format_location(latitude, longitude):
    """
    Format GPS coordinates for the accident alert.
    """

    location_link = create_google_maps_link(
        latitude,
        longitude
    )

    return (
        f"Latitude: {latitude}\n"
        f"Longitude: {longitude}\n"
        f"Location: {location_link}"
    )