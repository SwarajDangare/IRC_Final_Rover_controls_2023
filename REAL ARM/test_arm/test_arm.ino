#define dir_swivel 4
#define pwm_swivel 18
#define dir_link1 12
#define pwm_link1 27
#define dir_link2 16
#define pwm_link2 17

int freq = 8000;
int L1channel = 2;
int L2channel = 3;
int Swchannel = 4;
int resolution = 8;

const int pwm_pin[] = {pwm_swivel, pwm_link1, pwm_link2};
const int dir_pin[] = {dir_swivel, dir_link1, dir_link2};


void setup()
{
  Serial.begin(115200);
  ledcSetup(L1channel, freq, resolution);
  ledcSetup(L2channel, freq, resolution);
  ledcSetup(Swchannel, freq, resolution);
  ledcAttachPin(pwm_pin[0], L1channel);
  ledcAttachPin(pwm_pin[1], L2channel);
  ledcAttachPin(pwm_pin[2], Swchannel);
  pinMode(dir_pin[0], OUTPUT);
  pinMode(dir_pin[1], OUTPUT);
  pinMode(dir_pin[2], OUTPUT);

}

void loop() {

  digitalWrite(dir_swivel, HIGH);
  ledcWrite(L1channel, 200);
  digitalWrite(dir_link1, HIGH);
  ledcWrite(L2channel, 200);
  digitalWrite(dir_link2, HIGH);
  ledcWrite(Swchannel, 200);
  delay(200);
  Serial.println("cw");
  digitalWrite(dir_swivel, LOW);
  ledcWrite(L1channel, 200);
  digitalWrite(dir_link1, LOW);
  ledcWrite(L2channel, 200);
  digitalWrite(dir_link2, LOW);
  ledcWrite(Swchannel, 200);
  Serial.println("ccw");

}
