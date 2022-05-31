// libs required for bmp 280 sensor
#include <Arduino.h>
#include <Wire.h>
#include <BMx280I2C.h>

// bmp i2c port
BMx280I2C bmx280(0x76);

// libs required for DHT 22 , UV sensor
#include "DHT.h"
#include <LiquidCrystal_I2C.h>
#include <SPI.h>

// init dht 22 sensor
DHT dht(9, DHT22);

// serial port for LCD
LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup()
{
  ''
      // start serial at boud rate of 9600
      Serial.begin(9600);
  Serial.println(F("Welcome to my project"));

  // start msg on display
  lcd.setCursor(0, 0);
  lcd.print("Welcome to my project");
  delay(3000);
  lcd.clear();

  // BMP 280 Initial Setup
  while (!Serial)
    ;
  Wire.begin();
  if (!bmx280.begin())
  {
    Serial.println("check your Interface and I2C Address.");
    while (1)
      ;
  }
  if (bmx280.isBME280())
    Serial.println("BME280 detected");
  else
    Serial.println("BMP280 detected");
  bmx280.resetToDefaults();
  bmx280.writeOversamplingPressure(BMx280MI::OSRS_P_x16);
  bmx280.writeOversamplingTemperature(BMx280MI::OSRS_T_x16);
  if (bmx280.isBME280())
  {
    bmx280.writeOversamplingHumidity(BMx280MI::OSRS_H_x16);
  }

  // init LCD board
  lcd.init();
  lcd.backlight();

  // init DHT 22 sensor
  dht.begin();

  // init IR sensor
  pinMode(10, INPUT);
}

void loop()
{

  // =========================================== DHT 22 calculations =======================
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t))
  {
    Serial.println(F("Failed to read from DHT"));
    return;
  }

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print("\n");

  lcd.setCursor(0, 0);
  lcd.print(F("Humidity : "));
  lcd.setCursor(0, 1);
  lcd.print(h);
  lcd.print("  %");
  delay(4000);
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print(F("Temperature : "));
  lcd.setCursor(0, 1);
  lcd.print(t);
  lcd.print(" C");
  delay(4000);
  lcd.clear();

  // ============= IR sensor data gathering from pin 10 ====================

  if (digitalRead(10) == LOW)
  {
    lcd.setCursor(0, 0);
    lcd.print(F("Door is Closed"));
    Serial.println("Door is Closed");
    delay(4000);
    lcd.clear();
  }
  else
  {
    lcd.setCursor(0, 0);
    lcd.print(F("Door is Open"));
    Serial.println("Door is Open");
    delay(4000);
    lcd.clear();
  }

  // ======================= UV sensor data from A0 analog pin ==============
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.print("UV Sensor : ");
  Serial.print("Voltage = ");
  Serial.print(voltage);
  Serial.print(" | UV index = ");
  Serial.print(voltage / 0.1);
  Serial.print("\n");

  lcd.setCursor(0, 0);
  lcd.print("UV index : ");
  lcd.print(voltage / 0.1);
  delay(4000);
  lcd.clear();

  //==================================== bmp calculations =======================

  // start a measurement
  if (!bmx280.measure())
  {
    Serial.println("could not start measurement, is a measurement already running?");
    return;
  }

  // wait for the measurement to finish
  do
  {
  } while (!bmx280.hasValue());

  Serial.print("Pressure: ");
  Serial.println(bmx280.getPressure());
  Serial.print("Pressure (64 bit): ");
  Serial.println(bmx280.getPressure64());

  lcd.setCursor(0, 0);
  lcd.print("Pressure reading");
  lcd.setCursor(0, 1);
  lcd.print(bmx280.getPressure64() / 100000);
  // lcd.setCursor(0,1);
  // lcd.print("Temperature : ");
  // lcd.print(bmx280.getTemperature());
  delay(4000);
  lcd.clear();
}