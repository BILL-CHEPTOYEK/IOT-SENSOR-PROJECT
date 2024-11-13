import serial
import time
import requests

# Serial port configuration
SERIAL_PORT = '/dev/ttyUSB1'  # Change this if necessary (for example, COM3 for Windows)
BAUD_RATE = 9600  # Must match the Arduino's baud rate

# ThingSpeak API settings
THINGSPEAK_URL = 'https://api.thingspeak.com/update'
API_KEY = 'NNNZ8TKNSHSED9IT'  # Replace with your ThingSpeak API Write Key

# Initialize serial connection to Arduino
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)  # Wait for Arduino to initialize

def send_to_thingspeak(temperature, humidity, light_level):
    """
    Send sensor data to ThingSpeak
    """
    payload = {
        'api_key': API_KEY,
        'field1': temperature,  # Temperature field
        'field2': humidity,     # Humidity field
        'field3': light_level   # Light level field
    }
    response = requests.post(THINGSPEAK_URL, params=payload)
    
    if response.status_code == 200:
        print(f"Data sent to ThingSpeak: Temp={temperature}, Humidity={humidity}, Light={light_level}")
    else:
        print("Failed to send data to ThingSpeak")

def read_data():
    while True:
        if arduino.in_waiting > 0:  # If there is data available from Arduino
            data = arduino.readline().decode('utf-8').strip()  # Read and decode data
            print(f"Received Data: {data}")  # Print received data for debugging

            try:
                # Assuming the Arduino sends data in this format:
                # "Temperature: xx.x°C, Humidity: xx.x%, Light Level: xx.x%"
                # Example: "Temperature: 25.6°C, Humidity: 55.2%, Light Level: 72.3%"
                
                # Extract the data from the string (simple parsing)
                parts = data.split(", ")
                temp_str = parts[0].split(": ")[1].replace("°C", "")
                humidity_str = parts[1].split(": ")[1].replace("%", "")
                light_str = parts[2].split(": ")[1].replace("%", "")

                # Convert to float
                temperature = float(temp_str)
                humidity = float(humidity_str)
                light_level = float(light_str)

                # Send data to ThingSpeak
                send_to_thingspeak(temperature, humidity, light_level)

            except Exception as e:
                print(f"Error processing data: {e}")

            time.sleep(15)  # Wait 15 seconds before reading again (optional)

def main():
    print("Starting to read data from Arduino and send to ThingSpeak...")
    try:
        read_data()
    except KeyboardInterrupt:
        print("\nClosing the connection.")
        arduino.close()

if __name__ == '__main__':
    main()

