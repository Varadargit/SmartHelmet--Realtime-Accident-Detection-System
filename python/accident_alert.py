"""
Smart Helmet Accident Alert Controller

Responsible for:
- Receiving accident event information
- Processing GPS coordinates
- Creating the alert message
- Sending the notification through the configured API
"""

from gps_data import format_location
from whatsapp_alert import create_accident_message
from whatsapp_alert import send_whatsapp_alert


def process_accident(latitude, longitude, recipient):

    print("Accident event received.")

    print()
    print("GPS Information")
    print("----------------")

    print(format_location(
        latitude,
        longitude
    ))

    message = create_accident_message(
        latitude,
        longitude
    )

    send_whatsapp_alert(
        recipient,
        message
    )


if __name__ == "__main__":

    print("Smart Helmet Alert System")
    print("-------------------------")

    # Replace these with real-time GPS data
    # received from the embedded system.

    latitude = 12.9716
    longitude = 77.5946

    recipient = "+91XXXXXXXXXX"

    process_accident(
        latitude,
        longitude,
        recipient
    )