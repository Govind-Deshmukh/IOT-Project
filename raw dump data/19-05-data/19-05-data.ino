#include "DHT.h"
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

#include <SPI.h>

DHT dht(9, DHT22);

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display


void setup() {
  Serial.begin(9600);
  Serial.println(F("Welcome to my project"));

  lcd.init();
  lcd.backlight();
  
  dht.begin();

  pinMode(10,INPUT);
  pinMode(11,INPUT);
}

void loop() {
  // Wait a few seconds between measurements.

  float h = dht.readHumidity();
  float t = dht.readTemperature();


  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT"));
    return;
  }


  lcd.setCursor(0,0);
  lcd.print(F("Humidity : "));
  lcd.setCursor(0,1);
  lcd.print(h);
  lcd.print("  %");
  delay(4000);
  lcd.clear();

  lcd.setCursor(0,0);
  lcd.print(F("Temperature : "));
  lcd.setCursor(0,1);
  lcd.print(t);
  lcd.print(" C");
  delay(4000);
  lcd.clear();



  if (digitalRead(10)==LOW){
    lcd.setCursor(0,0);
    lcd.print(F("Door is Closed"));
    delay(4000);
    lcd.clear();
  }
  else{
    lcd.setCursor(0,0);
    lcd.print(F("Door is Open"));
    delay(4000);
    lcd.clear();
  }

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print("\n");

  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.print("UV Sensor : ");
  Serial.print("Voltage = ");
  Serial.print(voltage);
  Serial.print(" | UV index = ");
  Serial.print(voltage/0.1);
  Serial.print("\n");
  
  lcd.setCursor(0,0);
  lcd.print("UV index : ");
  lcd.print(voltage/0.1);
  delay(4000);
  lcd.clear();
}
