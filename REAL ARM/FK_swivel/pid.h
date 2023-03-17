class PID 
{
  private:
    float kp, kd, ki, umax, umin; // Parameters
    float prev_error, I; // Storage

  public:
    // Constructor
    PID() : kp(1), kd(0), ki(0), umax(255), umin(0), prev_error(0.0), I(0.0) {}

    // A function to set the parameters
    void setParams(float kpIn, float kdIn, float kiIn, float umaxIn, float uminIn) {
      kp = kpIn;
      kd = kdIn;
      ki = kiIn;
      umax = umaxIn;
      umin = uminIn;
    }

    // A function to compute the control signal
    void getpid(int currentPose, int target, float deltaT, int &pwr, int &dir) 
    {
      // error
      int error = target - currentPose;

      // derivative
      float D = (error - prev_error) / (deltaT);

      // integral
      I = I + (error * deltaT);

      // control signal
      pwr = abs(kp * error + kd * D + ki * I);

      // motor power
      if ( pwr > umax )
      {
        pwr = umax;
      }
      else if ( pwr < umin )
      {
        pwr = umin;
      }
      
      // HOLD PAYLOAD
      if (abs(error) < 1)
      {
        pwr = 0;

      }
      // motor direction
      if (error > 0) {
        dir = HIGH;
      }
      else dir = LOW;

      // store previous error
      prev_error = error;
    }

};
