#include "drive.h"
#include <HardwareSerial.h>

HardwareSerial SerialPort(0); // use UART0
HardwareSerial Sender(1);
const int BUFFER_SIZE = 128;
char rxBuffer[BUFFER_SIZE];
int bufferIndex = 0;
const int Rdir = 5;
const int Ldir = 25;
const int Rpwm = 18;
const int Lpwm = 33;

const int freq = 8000;
const int Lchannel = 0;
const int Rchannel = 1;
const int resolution = 8;


int x = 0, y = 0;
float M = 1.0;
char c;




void setup()
{
  Serial.begin(115200);
  SerialPort.begin(115200) ;   // Use default serial for debug output
  Sender.begin(115200, SERIAL_8N1, 0, 2);//(baud rate,protocol,Tx,Rx)

  ledcSetup(Lchannel, freq, resolution);
  ledcSetup(Rchannel, freq, resolution);
  ledcAttachPin(Lpwm, Lchannel);
  ledcAttachPin(Rpwm, Rchannel);
  pinMode(Ldir, OUTPUT);
  pinMode(Rdir, OUTPUT);
}

void loop()
{
  if (SerialPort.available())
  {
    // read the data into the buffer
    while (SerialPort.available())
    {
      rxBuffer[bufferIndex] = (char)SerialPort.read();
      bufferIndex++;
      // Make sure we don't overflow the buffer
      if (bufferIndex >= BUFFER_SIZE)
        bufferIndex = 0;
    }

    // Find the positions of the "M","X", "Y", "S" and "E" characters in the buffer
    char *M_index = strchr(rxBuffer, 'M');
    char *x_index = strchr(rxBuffer, 'X');
    char *y_index = strchr(rxBuffer, 'Y');
    char *P_index = strchr(rxBuffer, 'P');
    char *Q_index = strchr(rxBuffer, 'Q');
    char *A_index = strchr(rxBuffer, 'A');
    char *S_index = strchr(rxBuffer, 'S');
    char *E_index = strchr(rxBuffer, 'E');

    if (M_index != NULL && x_index != NULL && y_index != NULL && P_index != NULL && Q_index != NULL && A_index != NULL&& S_index != NULL&& E_index != NULL)
    {
      // Extract the values from the packet
      char m = *(M_index + 1);
      int M = m - '0';
      int x = atoi(x_index + 1);
      int y = atoi(y_index + 1);
      int l2 = atoi(P_index + 1);
      int l1 = atoi(Q_index + 1);
      int grip = atoi(A_index + 1);
      int swivel = atoi(S_index + 1);
      MotorCode(x, y, M);
      delay(10);

    }
    else
    {
      Serial.println("Invalid Packet received");
    }
  }
  bufferIndex = 0;
}
