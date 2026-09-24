# Smart Helmet – Real-Time Accident Detection System

## Overview

The Smart Helmet is an embedded IoT safety system designed to detect abnormal vibration associated with a possible accident and communicate the rider's real-time location to a predefined contact.

* An analog vibration sensor continuously monitors vibration levels.
* Arduino Uno reads the vibration signal and performs threshold-based detection.
* The vibration threshold is determined through calibration under different helmet-use and impact conditions.
* When the vibration value exceeds the configured threshold, the system identifies a possible accident event.
* The GPS module is then used to obtain the rider's real-time latitude and longitude.
* A GSM module with a SIM card provides cellular communication.
* Arduino IDE is used for coordinating the embedded hardware.
* Python is used separately for GPS/location processing and API integration.
* The resulting accident notification contains the real-time GPS location and is delivered through the configured WhatsApp communication mechanism.
* The system achieved an approximate 7–11 second response time under the tested setup and network conditions.

---

## Key Features

* Analog vibration sensing using Arduino Uno.
* Threshold-based accident-event detection.
* Calibration of vibration readings under different conditions.
* Real-time GPS coordinate acquisition.
* GPS latitude and longitude processing.
* GSM-based cellular communication.
* SIM-based communication.
* Python API integration.
* WhatsApp accident notification.
* Google Maps location link generation.
* Predefined emergency contact notification.

---

## System Architecture

```text
                         SMART HELMET
                              │
                              ▼
                    ┌───────────────────┐
                    │  Vibration Sensor │
                    │    Analog Output  │
                    └─────────┬─────────┘
                              │
                         Analog Reading
                           0 – 1023
                              │
                              ▼
                    ┌───────────────────┐
                    │    Arduino Uno    │
                    │                   │
                    │ Sensor Reading    │
                    │ Threshold Check   │
                    │ Event Detection   │
                    └─────────┬─────────┘
                              │
                     Threshold Exceeded
                              │
                              ▼
                    ┌───────────────────┐
                    │    GPS Module     │
                    │                   │
                    │ Latitude          │
                    │ Longitude         │
                    └─────────┬─────────┘
                              │
                     Real-Time Location
                              │
                              ▼
                    ┌───────────────────┐
                    │    GSM Module     │
                    │                   │
                    │ SIM Card          │
                    │ Cellular Network  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Python / API      │
                    │ Integration Layer │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ WhatsApp Alert    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Predefined Contact│
                    └───────────────────┘
```

---

## How the System Works

The system continuously monitors vibration data while the rider is using the helmet.

### 1. Vibration Monitoring

The vibration sensor provides an analog signal to the Arduino Uno.

The Arduino's ADC converts the signal into a numerical value between:

```text
0 ───────────────────────────── 1023
```

The system continuously samples this value.

```cpp
int vibrationValue = analogRead(VIBRATION_PIN);
```

### 2. Threshold Detection

A threshold is used to distinguish abnormal vibration from normal operating conditions.

```text
Vibration Reading
       │
       ▼
Compare with Threshold
       │
       ├── Below Threshold
       │        │
       │        └── Continue Monitoring
       │
       └── Above Threshold
                │
                ▼
       Possible Accident Event
```

The threshold is not treated as a universal fixed value. It should be established experimentally by collecting sensor readings under different conditions.

---

## Vibration Sensor Calibration

The project considers the fact that vibration characteristics can vary depending on how the helmet is being used.

Sensor readings can be collected for:

* Helmet in a stationary condition.
* Helmet being worn.
* Normal rider movement.
* Normal riding conditions.
* Helmet falling from a surface.
* Controlled impact simulations.

The recorded values can then be analyzed to determine a suitable threshold for abnormal vibration detection.

### Calibration Concept

```text
Normal Conditions
       │
       ▼
Collect Sensor Readings
       │
       ▼
Determine Normal Range
       │
       ▼
Test Impact Conditions
       │
       ▼
Compare Sensor Ranges
       │
       ▼
Select Detection Threshold
```

This approach helps reduce false detections caused by ordinary helmet movement or vibration.

---

## Accident Detection Algorithm

```text
START
  │
  ▼
Initialize Arduino
  │
  ▼
Read Analog Vibration Value
  │
  ▼
Compare Value With Threshold
  │
  ├─────────────── No ───────────────┐
  │                                  │
  │                                  ▼
  │                           Continue Monitoring
  │                                  │
  │                                  └──────┐
  │                                         │
  └────────────── Yes                       │
                 │                          │
                 ▼                          │
       Possible Accident Detected           │
                 │                          │
                 ▼                          │
          Obtain GPS Data                   │
                 │                          │
                 ▼                          │
       Read Latitude/Longitude              │
                 │                          │
                 ▼                          │
        GSM Communication                   │
                 │                          │
                 ▼                          │
       Python/API Processing                │
                 │                          │
                 ▼                          │
        WhatsApp Notification               │
                 │                          │
                 ▼                          │
         Predefined Contact                │
                 │                          │
                 └──────────────────────────┘
```

---

## Real-Time GPS Location

After the vibration threshold is exceeded, the system obtains the rider's current geographical coordinates from the GPS module.

The location consists of:

* Latitude
* Longitude

The coordinates can be converted into a Google Maps link:

```text
https://maps.google.com/?q=<latitude>,<longitude>
```

Example notification structure:

```text
ACCIDENT DETECTED

A possible accident event has been detected.

Latitude: <real-time latitude>
Longitude: <real-time longitude>

GPS Location:
https://maps.google.com/?q=<latitude>,<longitude>
```

The coordinates are obtained at runtime from the GPS system rather than being predefined in the actual accident-detection workflow.

---

## GSM Communication

The GSM module contains a SIM card and provides cellular communication.

The communication flow is:

```text
Arduino Uno
     │
     ▼
GSM Module
     │
     ▼
SIM Card
     │
     ▼
Cellular Network
     │
     ▼
Communication / API Layer
     │
     ▼
Notification
```

The exact GSM commands and API implementation depend on the specific GSM module and communication service used.

---

## Python Integration

Python is used separately from the Arduino embedded-control layer.

### Arduino responsibilities

* Read vibration sensor.
* Process the sensor value.
* Compare the value with the threshold.
* Detect a possible accident event.
* Coordinate the embedded hardware.

### Python responsibilities

* Process GPS/location information.
* Generate the location link.
* Integrate with the configured API.
* Prepare the accident notification.
* Support WhatsApp notification delivery.

This separation keeps the embedded hardware control and external API processing as distinct software layers.

---

## End-to-End Communication Flow

```text
Vibration Sensor
       │
       ▼
Analog Sensor Value
       │
       ▼
Arduino Uno
       │
       ▼
Threshold Exceeded
       │
       ▼
Accident Event
       │
       ▼
GPS Module
       │
       ▼
Real-Time Coordinates
       │
       ▼
GSM Module + SIM
       │
       ▼
Python API Integration
       │
       ▼
WhatsApp Notification
       │
       ▼
Predefined Contact
```

---

## Response Time

During testing, the system achieved an approximate response time of:

```text
7–11 seconds
```

This represents the observed time under the tested hardware, software, and network conditions.

The actual response time can vary depending on factors such as:

* GPS location acquisition time.
* GSM network availability.
* API response time.
* Internet/network conditions.
* WhatsApp communication latency.

---

## Hardware Components

| Component               | Function                                               |
| ----------------------- | ------------------------------------------------------ |
| Arduino Uno             | Main controller and embedded hardware coordination     |
| Analog Vibration Sensor | Measures vibration levels for accident-event detection |
| GPS Module              | Provides real-time latitude and longitude              |
| GSM Module              | Provides cellular communication using a SIM card       |
| Helmet                  | Physical platform for the system                       |
| Battery / Power Supply  | Powers the embedded system                             |
| Connecting Wires        | Electrical interconnections                            |

---

## Hardware-to-Software Mapping

| Hardware                           | Software Responsibility                   |
| ---------------------------------- | ----------------------------------------- |
| Vibration Sensor                   | Analog sensor acquisition                 |
| Arduino Uno                        | Sensor processing and threshold detection |
| GPS Module                         | Real-time coordinate acquisition          |
| GSM Module                         | Cellular communication                    |
| SIM Card                           | Cellular network connectivity             |
| Python                             | Location processing and API integration   |
| WhatsApp API / Communication Layer | Accident notification                     |

---

## Repository Structure

```text
Smart-Helmet-Accident-Detection/
│
├── README.md
│
├── Arduino/
│   └── SmartHelmet/
│       └── SmartHelmet.ino
│
├── Python/
│   ├── gps_data.py
│   ├── whatsapp_alert.py
│   ├── accident_alert.py
│   └── requirements.txt
│
├── components/
│   ├── README.md
│   ├── arduino-uno.jpg
│   ├── vibration-sensor.jpg
│   ├── gps-module.jpg
│   ├── gsm-module.jpg
│   ├── helmet.jpg
│   ├── battery.jpg
│   └── wires.jpg
│
├── docs/
│   ├── system-architecture.md
│   ├── accident-detection.md
│   ├── communication.md
│   └── wiring.md
│
├── images/
│   ├── helmet.jpg
│   ├── architecture.png
│   ├── accident-detection-flow.png
│   ├── communication-flow.png
│   └── circuit.png
│
└── .gitignore
```

---

## Arduino Code

The core Arduino program continuously reads the analog vibration sensor and compares the reading against the calibrated threshold.

```cpp
const int VIBRATION_PIN = A0;

const int VIBRATION_THRESHOLD = 700;

bool accidentDetected = false;

void setup() {

    Serial.begin(9600);

    pinMode(VIBRATION_PIN, INPUT);

    Serial.println("Smart Helmet System Started");
    Serial.println("Monitoring vibration...");
}

void loop() {

    int vibrationValue = analogRead(VIBRATION_PIN);

    Serial.print("Vibration Value: ");
    Serial.println(vibrationValue);

    if (vibrationValue > VIBRATION_THRESHOLD &&
        !accidentDetected) {

        accidentDetected = true;

        Serial.println("Possible accident detected!");

        /*
         * GPS location acquisition
         * and GSM communication
         * are initiated here.
         */

        Serial.println("Requesting GPS location...");

        delay(1000);

        Serial.println("Preparing accident notification...");
    }

    delay(50);
}
```

> The `700` value is an example calibration value for the code structure. The actual threshold should be replaced with the experimentally determined value from sensor testing.

---

## Python Components

The Python layer is organized into separate modules for location processing and notification handling.

### GPS Data Processing

```python
def create_google_maps_link(latitude, longitude):

    return (
        f"https://maps.google.com/"
        f"?q={latitude},{longitude}"
    )


def format_location(latitude, longitude):

    location_link = create_google_maps_link(
        latitude,
        longitude
    )

    return (
        f"Latitude: {latitude}\n"
        f"Longitude: {longitude}\n"
        f"Location: {location_link}"
    )
```

### Accident Message

```python
def create_accident_message(latitude, longitude):

    location_link = (
        f"https://maps.google.com/"
        f"?q={latitude},{longitude}"
    )

    return (
        "ACCIDENT DETECTED\n\n"
        "A possible accident event has been detected.\n\n"
        f"Latitude: {latitude}\n"
        f"Longitude: {longitude}\n\n"
        f"GPS Location:\n{location_link}"
    )
```

---

## Testing

### 1. Vibration Sensor Testing

* Record readings while the helmet is stationary.
* Record readings while the helmet is worn.
* Record readings during normal movement.
* Record readings during normal riding.
* Record readings during controlled fall/impact tests.
* Compare the recorded ranges.
* Determine and validate the threshold.

### 2. GPS Testing

* Verify that the GPS module obtains valid coordinates.
* Verify latitude and longitude values.
* Verify that the generated location link points to the expected position.

### 3. GSM Testing

* Verify SIM registration.
* Verify cellular connectivity.
* Verify communication between Arduino and GSM module.

### 4. End-to-End Testing

```text
Sensor Event
     ↓
Threshold Detection
     ↓
GPS Coordinates
     ↓
GSM Communication
     ↓
API Integration
     ↓
WhatsApp Alert
```

---

## Challenges

* Distinguishing normal helmet vibration from abnormal impact.
* Establishing a suitable vibration threshold.
* Avoiding false detection from helmet movement or accidental drops.
* Obtaining GPS coordinates after an event.
* Coordinating multiple embedded modules.
* Managing GSM communication.
* Integrating real-time location information with an external notification service.
* Maintaining reliable communication under different network conditions.

---

## Technologies and Concepts

* Arduino Uno
* Arduino IDE
* C/C++
* Analog Sensor Reading
* ADC
* Threshold-Based Detection
* GPS
* GSM
* SIM-Based Communication
* Serial Communication
* Python
* API Integration
* WhatsApp
* Real-Time Location Tracking
* Embedded Systems
* IoT

---

## Future Improvements

* Multi-sample impact confirmation.
* Adaptive vibration thresholding.
* Additional sensors for improved accident classification.
* Helmet-wear detection.
* Battery-level monitoring.
* Cloud-based event logging.
* Web/mobile monitoring dashboard.
* Improved false-positive filtering.
* Emergency-contact management.
* Event history and timestamp logging.

---

## Key Learning Outcomes

* Interfacing analog sensors with Arduino Uno.
* Reading and processing real-time sensor data.
* Designing threshold-based event detection.
* Performing sensor calibration.
* Integrating GPS modules with embedded systems.
* Working with GSM communication.
* Processing real-time geographical coordinates.
* Using Python for API integration.
* Designing an end-to-end IoT safety system.
* Coordinating multiple hardware and software components.

---

Bengaluru, India
