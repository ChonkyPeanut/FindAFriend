#include <Adafruit_MotorShield.h>
#include <NewPing.h>


Adafruit_MotorShield myMotorShield = Adafruit_MotorShield();

Adafruit_DCMotor *Motor_A = myMotorShield.getMotor(4);
Adafruit_DCMotor *Motor_B = myMotorShield.getMotor(1);
Adafruit_DCMotor *Motor_C = myMotorShield.getMotor(3);
Adafruit_DCMotor *Motor_D = myMotorShield.getMotor(2);

#define TRIG_PIN A0
#define ECHO_PIN A1

NewPing sonar(TRIG_PIN,ECHO_PIN, 100);

void setup()
{
  Serial.begin(9600);
  myMotorShield.begin();
  set_speed(100);
  stop();
}
void loop()
{
  go_forward();
  long duration;
  int distance;
  duration = sonar.ping();
  distance = duration*(.034/2);
  Serial.print("Distance is : ");
  Serial.print(distance);
  Serial.println("cm");
  if(distance <= 10 && distance >0)
  {
    stop();
    turn_right();
    delay(1000);
    go_forward();
    delay(2941);
    stop();
    delay(5000);
  } else {
    go_forward();
  }
}

int get_distance()
{
  unsigned long duration = 0;
  float float_distance = 0.0;
  duration = sonar.ping_median(5);
  float_distance = duration*(.034/2);
  int distance = (int)float_distance;
  Serial.println("Distance is : "+ distance);
  delay(500);

  return distance;
}
void set_speed(int speed)
{
  Motor_A->setSpeed(speed);
  Motor_B->setSpeed(speed);
  Motor_C->setSpeed(speed);
  Motor_D->setSpeed(speed);
}
void go_forward()
{
  Motor_A->run(BACKWARD);
  Motor_B->run(FORWARD);
  Motor_C->run(BACKWARD);
  Motor_D->run(FORWARD);
}
void go_backward()
{
  Motor_A->run(BACKWARD);
  Motor_B->run(BACKWARD);
  Motor_C->run(FORWARD);
  Motor_D->run(FORWARD);
}
void stop()
{
  Motor_A->run(RELEASE);
  Motor_B->run(RELEASE);
  Motor_C->run(RELEASE);
  Motor_D->run(RELEASE);
}
void turn_right()
{
  Motor_A->run(BACKWARD);
  Motor_B->run(FORWARD);
  Motor_C->run(FORWARD);
  Motor_D->run(BACKWARD);
}
void turn_left()
{
  Motor_A->run(FORWARD);
  Motor_B->run(BACKWARD);
  Motor_C->run(BACKWARD);
  Motor_D->run(FORWARD);
}
