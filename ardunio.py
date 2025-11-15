#include <Adafruit_MotorShield.h>
#include <NewPing.h>
#include <Servo.h>

Servo myServo1;

int pos1 = -45;
long duration;
int distance;
bool objectDetected1 = False;
int posDetected1;

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
  myServo1.attach(9);
}

void loop()
{
  go_forward();
  check_distance();
  while(get_distance() >= 10 || get_distance() < 1 && objectDetected1 == False)
  {
    servo1();
    check_distance();
    go_forward();
  } else {
    
  }
}

void servo1()
{
  int pos = pos1;
  for (pos = -45; pos <= 44; pos + 1)
  {
    myServo1.write(pos);
    delay(50);
    if(distance <= 10 && distance >0)
    {
      posDetected1 = pos;
      check_distance();
      while(objectDetected1 == True)
      {
        for(int tempPos = pos; tempPos <= 45; tempPos +1)
        {
          turn_left();
          pos = tempPos;
          myServo1.write(pos);
        }
      }
    }
  }
  pos = 45
  for (pos = 45; pos >= -46; pos - 1)
  {
    myServo1.write(pos);
    delay(50);
    if(distance <= 10 && distance >0)
    {
      posDetected1 = pos;
      check_distance();
      while(objectDetected1 == True)
      {
        for(int tempPos = pos; tempPos <= 45; tempPos +1)
        {
          turn_left();
          pos = tempPos;
          myServo1.write(pos);
        }
      }
    }
  }
}

bool check_distance()
{
  if(distance <= 10 && distance > 0)
  {
    objectDetected1 == True;
  } else {
    objectDetected1 == False;
  }
return objectDetected1;
}

int get_distance()
{
  duration = sonar.ping();
  distance = duration*(.034/2);
  Serial.print("Distance is : ");
  Serial.print(distance);
  Serial.println("cm");
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
