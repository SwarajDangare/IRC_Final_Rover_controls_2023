#include <WiFi.h>

const int freq = 5000;
const int channel1 = 0;
const int channel2 = 1;
const int channel3 = 2;
const int resolution = 8;

#define relay1 21
#define relay2 19
#define relay3 18
#define relay4 5
#define water_heater 17
#define stepper_step 23
#define stepper_dir 22 ///
#define auger_pwm 33
#define auger_rot_pwm 26
#define senser_suit_pwm 14
#define auger_dir 32
#define auger_rot_dir 25
#define senser_suit_dir 27
const char *ssid = "MRM@BASE_MI";
const char *password = "mrm@2023";
IPAddress local_IP(10, 0, 0, 7);
IPAddress subnet(255, 255, 255, 254);
IPAddress gateway(10, 0, 0, 0);
IPAddress primaryDNS(8, 8, 8, 8);
IPAddress secondaryDNS(4, 4, 4, 4);

WiFiServer wifiServer(5005);

char rxData = 'd';
int sm = 0;

void setup()
{
    Serial.begin(115200);
    delay(1000);
    WiFi.config(local_IP, subnet, gateway, primaryDNS, secondaryDNS);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Please connection lagja...");
    }
    Serial.println("Data is in the air!");
    Serial.println(WiFi.localIP());
    wifiServer.begin();

    pinMode(relay1, OUTPUT); // relay 1
    pinMode(relay2, OUTPUT);  // relay 2
    pinMode(relay3, OUTPUT); // relay 3
    pinMode(relay4, OUTPUT);  // relay 4
    pinMode(water_heater, OUTPUT);  // water heater
    pinMode(stepper_step, OUTPUT); // stepper step
    pinMode(stepper_dir, OUTPUT); // stepper direction
    pinMode(auger_dir, OUTPUT); // auger actuation direction
    pinMode(auger_rot_dir, OUTPUT); // auger rotation direction
    pinMode(senser_suit_dir, OUTPUT); // sensor suite direction

    ledcSetup(channel1, freq, resolution);
    ledcSetup(channel2, freq, resolution);
    ledcSetup(channel3, freq, resolution);

    ledcAttachPin(auger_pwm, channel1); // auger actuation PWM
    ledcAttachPin(auger_rot_pwm, channel2); // auger rotation PWM
    ledcAttachPin(senser_suit_pwm, channel3); // sensor suite PWM
}

void SMControl(int sm)
{
    switch (sm)
    {
    case 0: // safety
        ledcWrite(channel1, 0);
        ledcWrite(channel2, 0);
        ledcWrite(channel3, 0);
        digitalWrite(relay1, LOW);
        digitalWrite(relay2, LOW);
        digitalWrite(relay3, LOW);
        digitalWrite(relay4, LOW);
        digitalWrite(water_heater, LOW);
        digitalWrite(stepper_step, LOW);
        digitalWrite(stepper_dir, LOW);
        digitalWrite(auger_dir, LOW);
        digitalWrite(auger_rot_dir, LOW);
        digitalWrite(senser_suit_dir, LOW);
        break;

    case 1: // relay 1,2,3,4
        digitalWrite(relay1, HIGH);
        digitalWrite(relay2, HIGH);
        digitalWrite(relay3, HIGH);
        digitalWrite(relay4, HIGH);
        break;

    case 2: // water heater
        digitalWrite(water_heater, HIGH);
        break;

    case 3: // servo rotate
        digitalWrite(stepper_step, HIGH);
        delay(100);
        digitalWrite(stepper_step, LOW);
        delay(100);
        break;

    case 4: // servo direction toggle
        digitalWrite(stepper_dir, !digitalRead(stepper_dir));
        delay(100);
        //may have to add delay
        break;

    case 5: // auger down with rotation
        digitalWrite(auger_dir, HIGH);
        digitalWrite(auger_rot_dir, HIGH);
        ledcWrite(channel1, 255);
        ledcWrite(channel2, 255);
        break;

    case 6: // auger up
        digitalWrite(auger_dir, LOW);
        digitalWrite(auger_rot_dir, LOW);
        ledcWrite(channel1, 255);
        ledcWrite(channel2, 0);
        break;

    case 7: // auger rotation for deposition
        digitalWrite(auger_dir, LOW);
        digitalWrite(auger_rot_dir, LOW);
        ledcWrite(channel1, 0);
        ledcWrite(channel2, 255);
        break;

    case 8: // sensor suite up
        digitalWrite(senser_suit_dir, HIGH);
        ledcWrite(channel3, 255);
        break;

    case 9: // sensor suite down
        digitalWrite(senser_suit_dir, LOW);
        ledcWrite(channel3, 255);
        break;

//    case 10: // sensor suite down
//        digitalWrite(senser_suit_dir, LOW);
//        ledcWrite(channel3, 255);
//        break;

    default:
        ledcWrite(channel1, 0);
        ledcWrite(channel2, 0);
        ledcWrite(channel3, 0);
        break;
    }
}

void loop()
{
    WiFiClient client = wifiServer.available();
    if (client)
    {
        while (client.connected())
        {
            while (client.available() > 0)
            {
                rxData = client.read();
                sm = rxData - '0';
                client.write(rxData);
            }
            delay(10);
            SMControl(sm);
            Serial.println(sm);
        }
        client.stop();
        Serial.println("Khatam bhencho...");
    }
}
