#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include "DHT.h"

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600);
  
  // initialize the lcd 
  lcd.init();
  
  //  init dht 22
  dht.begin();
  
  // start LCD backlight.
  lcd.backlight();
  


}


void loop()
{
  
  delay(1000);
  
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();


  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;


  Serial.print(F("Humidity: ")); Serial.print(h);
  Serial.print(F("Temp (°C): ")); Serial.print(t);


  }
  
}
