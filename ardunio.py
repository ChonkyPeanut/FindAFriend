#include <Adafruit_MotorShield.h>
#include <NewPing.h>
#include <Servo.h>

Adafruit_MotorShield myMotorShield = Adafruit_MotorShield();

Adafruit_DCMotor *Motor_A = myMotorShield.getMotor(4);
Adafruit_DCMotor *Motor_B = myMotorShield.getMotor(1);
Adafruit_DCMotor *Motor_C = myMotorShield.getMotor(3);
Adafruit_DCMotor *Motor_D = myMotorShield.getMotor(2);

#define TRIG_PIN A0
#define ECHO_PIN A1

long duration;
int distance;

Servo myservo1;

int pos1 = -45;
int wait_time1 = 100;
bool object_detected1 = false;

NewPing sonar(TRIG_PIN, ECHO_PIN, 100);

void setup() {
  Serial.begin(9600);
  myMotorShield.begin();
  set_speed(100);
  stop();

  myservo1.attach(9);
  myservo1.write(pos1);
}

void loop() {
  check_distance();
  while (isObjectDetected() == false) {
    for (int i = pos1; i <= 45; i++) {
      myservo1.write(i);
      check_distance();
      pos1 = i;
      if (isObjectDetected() == true) {
        turn_left();
      } else {
        go_forward();
      }
    }
    for (int i = pos1; i >= -45; i--) {
      myservo1.write(i);
      check_distance();
      pos1 = i;
      if (isObjectDetected() == true) {
        turn_right();
      } else {
        go_forward();
      }
    }
  }
}

int check_distance() {
  duration = sonar.ping();
  distance = duration * (.034 / 2);
  Serial.print("Distance is : ");
  Serial.print(distance);
  Serial.println("cm");
  return distance;
}

bool isObjectDetected() {
  check_distance();
  if (check_distance() <= 10 && check_distance() > 0) {
    return true;
  } else {
    return false;
  }
}

void set_speed(int speed) {
  Motor_A->setSpeed(speed);
  Motor_B->setSpeed(speed);
  Motor_C->setSpeed(speed);
  Motor_D->setSpeed(speed);
}
void go_forward() {
  Motor_A->run(BACKWARD);
  Motor_B->run(FORWARD);
  Motor_C->run(BACKWARD);
  Motor_D->run(FORWARD);
}
void go_backward() {
  Motor_A->run(BACKWARD);
  Motor_B->run(BACKWARD);
  Motor_C->run(FORWARD);
  Motor_D->run(FORWARD);
}
void stop() {
  Motor_A->run(RELEASE);
  Motor_B->run(RELEASE);
  Motor_C->run(RELEASE);
  Motor_D->run(RELEASE);
  delay(500);
}
void turn_right() {
  Motor_A->run(BACKWARD);
  Motor_B->run(FORWARD);
  Motor_C->run(FORWARD);
  Motor_D->run(BACKWARD);
}
void turn_left() {
  Motor_A->run(FORWARD);
  Motor_B->run(BACKWARD);
  Motor_C->run(BACKWARD);
  Motor_D->run(FORWARD);
}
