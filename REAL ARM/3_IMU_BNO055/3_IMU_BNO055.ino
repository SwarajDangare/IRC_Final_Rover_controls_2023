#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

/* This driver uses the Adafruit unified sensor library (Adafruit_Sensor),
   which provides a common 'type' for sensor data and some helper functions.

   To use this driver you will also need to download the Adafruit_Sensor
   library and include it in your libraries folder.

   You should also assign a unique ID to this sensor for use with
   the Adafruit Sensor API so that you can identify this particular
   sensor in any data logs, etc.  To assign a unique ID, simply
   provide an appropriate value in the constructor below (12345
   is used by default in this example).

   Connections
   ===========
   Connect SCL to analog 5
   Connect SDA to analog 4
   Connect VDD to 3.3-5V DC
   Connect GROUND to common ground

   History
   =======
   2015/MAR/03  - First release (KTOWN)
*/

/* Set the delay between fresh samples */

Adafruit_BNO055 bno2 = Adafruit_BNO055(55, 0x28);
Adafruit_BNO055 bno1 = Adafruit_BNO055(55, 0x29);

void setBNO0551()
{
  if (!bno1.begin())
  {
    Serial.print("Ooops, no BNO055-1 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }
  Serial.println("BNO055-1 detected!!");
}

void setBNO0552()
{
  if (!bno2.begin())
  {
    Serial.print("Ooops, no BNO055-2 detected ... Check your wiring or I2C ADDR!");
    while (1);
  }
  Serial.println("BNO055-2 detected!!");
}

float yBNO0551()
{
  sensors_event_t orientationData;
  bno1.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  float y = orientationData.orientation.z;

  return (y);
}
float yBNO0552()
{
  sensors_event_t orientationData;
  bno2.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  float y = orientationData.orientation.z;

  return (y);
}
float zBNO0552()
{
  sensors_event_t orientationData;
  bno2.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  float z = orientationData.orientation.x;
  if(z>180)
  {
    z=z-360;
  }
  return (z);
}

void setup(void)
{
  Serial.begin(115200);
  Serial.println("Orientation Sensor Test");
  Serial.println("");
  delay(1000);

   //---BNO055-1---
  setBNO0551();
  delay(500);

  //---BNO055-2---
  setBNO0552();
  delay(500);
  pinMode(33,INPUT_PULLUP);


}

void loop(void)
{
  //---BNO055-2---
  Serial.print("y1: ");
  Serial.print(yBNO0551());
  Serial.print(" ");
  delay(10);

  //---BNO055-1---
  Serial.print("y2: ");
  Serial.print(yBNO0552());
  Serial.print(" ");
  delay(10);

  Serial.print("z2: ");
  Serial.println(zBNO0552());
  delay(10);
  
  if(digitalRead(33)==LOW)
  {
    setBNO0551();
    delay(10);
    setBNO0552();
    delay(10);
  }
}
