# IoT-Based Sensor Monitoring and Control System

## Overview
This project is an Internet of Things (IoT) system for monitoring environmental parameters such as temperature, humidity, and light levels. The system uses an **Arduino** to collect sensor data and send it to the cloud for real-time visualization and analysis. A **DHT22** sensor measures temperature and humidity, while a **LDR (Light Dependent Resistor)** measures light intensity. The system also includes a **Relay** for controlling devices based on light levels and an **LED** for temperature alerts.

The data is uploaded to **ThingSpeak** using a Python script, allowing you to monitor the system remotely and visualize the data through time-series graphs and real-time gauges.


## Hardware Components
- **Arduino Board (e.g., Arduino Uno)**
- **DHT22 Temperature and Humidity Sensor**
- **LDR (Light Dependent Resistor)**
- **Relay Module** (for controlling external devices based on light level)
- **LED** (for visual temperature alert)
- **Resistors, Jumper Wires, Breadboard**


## Features
- Monitor temperature, humidity, and light levels in real-time.
- Control external devices (e.g., light) based on light levels.
- Visualize data on ThingSpeak using graphs and gauges.
- Trigger alerts for abnormal temperature values (e.g., temperature exceeds 30°C).
- Send sensor data to ThingSpeak using a Python script.


## Hardware Connections
1. **DHT22 Sensor:**
   - VCC → 5V
   - GND → GND
   - DATA → Digital Pin 8 (Arduino)

2. **LDR (Light Sensor):**
   - One end to analog pin A0
   - The other end to GND with a pull-down resistor.

3. **Relay Module:**
   - VCC → 5V
   - GND → GND
   - IN → Digital Pin 7 (Arduino)

4. **LED:**
   - Anode → Digital Pin 9 (Arduino)
   - Cathode → GND


## Software Components
### Arduino Code
The Arduino code reads data from the **DHT22** and **LDR**, controls the **Relay** based on light levels, and triggers the **LED** for temperature alerts. The data is printed to the Serial Monitor and is read by a Python script for uploading to ThingSpeak.

[Link to Arduino Code](Arduino/arduino_code.ino)

### Python Script (`connectcloud.py`)
The Python script reads data from the Arduino’s Serial Monitor, parses it, and uploads it to ThingSpeak. It sends the data at regular intervals and handles connectivity to the ThingSpeak API.

[Link to Python Script](Python/connectcloud.py)


## Cloud Integration - ThingSpeak
- **ThingSpeak** is used to store and visualize the data from the IoT system. Create a **ThingSpeak channel** to collect data from the sensors. The Python script sends data to this channel via its API.
- The data is visualized using real-time gauges and time-series graphs for each parameter.

### ThingSpeak API Key:
- You will need to create a channel on ThingSpeak to get an **API write key**. Once you have the key, update the `API_KEY` variable in the Python script.

## How to Run the Project

### Step 1: Set Up the Hardware
- Connect the sensors (DHT22, LDR, Relay, and LED) to the Arduino as described in the hardware connections section.
  
### Step 2: Upload the Arduino Code
- Open the Arduino IDE.
- Select the correct board and port in the Tools menu.
- Upload the `arduino_code.ino` to the Arduino.

### Step 3: Install Python Dependencies
Make sure you have Python installed, and install the required libraries:
```bash
pip install pyserial requests
```
### Step 4: Run the python script
Open your terminal then run the script
```bash
python connectcloud.py
```
if you have python3 installed
run
```bash
python3 connectcloud.py
```
Now you can view your visualizations in your thingspeak acccount