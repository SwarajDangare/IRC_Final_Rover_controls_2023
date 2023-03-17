void MotorCode(int x, int y, int M)
{
  // STOP
  if (abs(x) < 100 && abs(y) < 100)
  {
    Serial.println("Stop");
    digitalWrite(Ldir, LOW);
    digitalWrite(Rdir, LOW);
    ledcWrite(Lchannel, 0);
    ledcWrite(Rchannel, 0);
  }

  // FORWARD MAX
  else if (abs(x) < 100 && y > 100)
  {
    Serial.println("FM");

    digitalWrite(Ldir, HIGH);
    digitalWrite(Rdir, HIGH);
    int i = map(abs(y) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(y) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // BACKWARD MAX
  else if (abs(x) < 100 && y < 100)
  {
    Serial.println("BM");

    digitalWrite(Ldir, LOW);
    digitalWrite(Rdir, LOW);
    int i = map(abs(y) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(y) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
    ledcWrite(Lchannel, (uint32_t)(abs(y) * (M * 0.1) * fact));
    ledcWrite(Rchannel, (uint32_t)(abs(y) * (M * 0.1) * fact));
  }

  // SPOT LEFT
  else if (x < 100 && abs(y) <= 100)
  {
    Serial.println("SL");

    digitalWrite(Ldir, LOW);
    digitalWrite(Rdir, HIGH);
    int i = map(abs(x) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(x) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // SPOT RIGHT
  else if (x > 100 && abs(y) <= 100)
  {
    Serial.println("SR");

    digitalWrite(Ldir, HIGH);
    digitalWrite(Rdir, LOW);
    int i = map(abs(x) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(x) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // OCTET 1
  else if (x > 100 && y > 100 && x > y)
  {
    Serial.println("O1");

    digitalWrite(Ldir, HIGH);
    digitalWrite(Rdir, LOW);
    int i = map(abs(x) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(abs(x) - abs(y)) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // OCTET 2
  else if (x > 100 && y > 100 && x < y)
  {
    Serial.println("O2");

    digitalWrite(Ldir, HIGH);
    digitalWrite(Rdir, HIGH);
    int i = map(abs(y) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(abs(x) - abs(y)) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // OCTET 3
  else if (x < 100 && y > 100 && abs(x) < y)
  {
    Serial.println("O3");

    digitalWrite(Ldir, HIGH);
    digitalWrite(Rdir, HIGH);
    int i = map(abs(abs(x) - abs(y)) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(y) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // OCTET 4
  else if (x < 100 && y > 100 && abs(x) >= y)
  {
    Serial.println("O4");

    digitalWrite(Ldir, LOW);
    digitalWrite(Rdir, HIGH);
    int i = map(abs(abs(x) - abs(y)) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(x) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }
  // OCTET 5
  else if (x < 100 && y < 100 && abs(x) > abs(y))
  {
    Serial.println("O5");

    digitalWrite(Ldir, LOW);
    digitalWrite(Rdir, HIGH);
    int i = map(abs(x) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(abs(x) - abs(y)) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // OCTET 6
  else if (x < 100 && y < 100 && abs(x) < abs(y))
  {
    Serial.println("O6");

    digitalWrite(Ldir, LOW);
    digitalWrite(Rdir, LOW);
    int i = map(abs(y) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(abs(x) - abs(y)) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // OCTET 7
  else if (x > 100 && y < 100 && abs(x) < abs(y))
  {
    Serial.println("O7");

    digitalWrite(Ldir, LOW);
    digitalWrite(Rdir, LOW);
    int i = map(abs(abs(x) - abs(y)) * (M * 0.1), 100, 1023, 0, 255);
    int j = map(abs(y) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }

  // OCTET 8
  else if (x > 100 && y < 100 && abs(x) > abs(y))
  {
    Serial.println("O8");

    digitalWrite(Ldir, HIGH);
    digitalWrite(Rdir, LOW);
    int i = map(abs(abs(x) - abs(y)), 100, 1023, 0, 255);
    int j = map(abs(x) * (M * 0.1), 100, 1023, 0, 255);
    ledcWrite(Lchannel, i);
    ledcWrite(Rchannel, j);
  }
}
