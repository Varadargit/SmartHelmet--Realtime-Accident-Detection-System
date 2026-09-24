"""
WhatsApp Alert Module

This module prepares the accident notification
containing the real-time GPS location.

The actual API request should be implemented
according to the WhatsApp API/service used.
"""


def create_accident_message(latitude, longitude):

    location_link = (
        f"https://maps.google.com/"
        f"?q={latitude},{longitude}"
    )

    message = (
        "ACCIDENT DETECTED\n\n"
        "A possible accident event has been "
        "detected by the Smart Helmet.\n\n"
        f"Latitude: {latitude}\n"
        f"Longitude: {longitude}\n\n"
        f"GPS Location:\n{location_link}"
    )

    return message


def send_whatsapp_alert(recipient, message):

    """
    Integrate the actual WhatsApp API here.

    The API endpoint and authentication method
    depend on the service used by the project.
    """

    print("Preparing WhatsApp alert...")
    print(f"Recipient: {recipient}")
    print()
    print(message)


if __name__ == "__main__":

    # Example values for testing only.
    # In the actual system these values should
    # come from the real-time GPS data.

    latitude = 12.9716
    longitude = 77.5946

    recipient = "+91XXXXXXXXXX"

    message = create_accident_message(
        latitude,
        longitude
    )

    send_whatsapp_alert(
        recipient,
        message
    )