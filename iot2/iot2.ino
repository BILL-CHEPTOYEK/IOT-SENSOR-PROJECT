#include <DHT.h>

// Pin configuration
#define DHTPIN 8         // DHT22 data pin connected to digital pin 8
#define DHTTYPE DHT22    // Define sensor type DHT22
#define RELAY_PIN 7      // Relay control pin
#define LED_PIN 9        // LED for temperature alert
#define LDR_PIN A0       // Analog pin for LDR (light sensor)

// DHT sensor setup
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Initialize Serial Monitor
  Serial.begin(9600);

  // Set up pins
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);

  // Initialize DHT sensor
  dht.begin();
}

void readAndDisplayData() {
  // Read temperature and humidity from DHT22
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Read light level from LDR
  int light_value = analogRead(LDR_PIN);
  float light_percentage = map(light_value, 0, 1023, 0, 100);

  // Control relay based on light level
  if (light_percentage < 30) {
    digitalWrite(RELAY_PIN, HIGH);  // Turn on relay
  } else {
    digitalWrite(RELAY_PIN, LOW);   // Turn off relay
  }

  // Turn on LED if temperature exceeds threshold
  if (temperature > 30) {
    digitalWrite(LED_PIN, HIGH);    // Temperature alert
  } else {
    digitalWrite(LED_PIN, LOW);
  }

  // Display sensor data on Serial Monitor
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print("°C, Humidity: ");
  Serial.print(humidity);
  Serial.print("%, Light Level: ");
  Serial.print(light_percentage);
  Serial.println("%");
}

void loop() {
  // Read sensors and display data every 5 seconds
  readAndDisplayData();
  delay(5000);
}
