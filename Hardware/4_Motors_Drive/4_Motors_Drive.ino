// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!

#include <AFMotor.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

int speed(int val){
  return map(val, 0, 100, 0, 255);
}





int Speed = speed(50);

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");

  // turn on motor
  //motor.setSpeed(200);
 
  //motor.run(RELEASE);
}


void loop() {

  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim(); // Remove any leading or trailing whitespace


    if (input=="s" || input=="S"){
      Serial.println("STOP");
      Serial.println("STOP, STOP, STOP, STOP.");
      motor1.run(RELEASE);
      motor2.run(RELEASE);
      motor3.run(RELEASE);
      motor4.run(RELEASE);
    }

    else if (input=="f" || input=="F"){
      Serial.println("FORWARD");
      Serial.println("FORWARD, FORWARD, FORWARD, FORWARD.");

      motor1.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor2.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor3.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor4.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)

      motor1.run(FORWARD);
      motor2.run(FORWARD);
      motor3.run(FORWARD);
      motor4.run(FORWARD);
    }

    else if (input=="b" || input=="B"){
      Serial.println("BACKWARD");
      Serial.println("BACKWARD, BACKWARD, BACKWARD, BACKWARD.");

      motor1.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor2.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor3.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor4.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)

      motor1.run(BACKWARD);
      motor2.run(BACKWARD);
      motor3.run(BACKWARD);
      motor4.run(BACKWARD);
    }

    else if (input=="l" || input=="L"){
      Serial.println("LEFT");
      Serial.println("FORWARD, FORWARD, BACKWARD, BACKWARD.");

      motor1.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor2.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor3.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor4.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)

      motor1.run(FORWARD);
      motor2.run(FORWARD);
      motor3.run(BACKWARD);
      motor4.run(BACKWARD);
    }
 
    else if (input=="r" || input=="R"){
      Serial.println("RIGHT");
      Serial.println("BACKWARD, BACKWARD, FORWARD, FORWARD.");

      motor1.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor2.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor3.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor4.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)

      motor1.run(BACKWARD);
      motor2.run(BACKWARD);
      motor3.run(FORWARD);
      motor4.run(FORWARD);
    }






////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


    else if (input=="F1" || input=="f1") {
      motor1.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor1.run(FORWARD);
      Serial.println("MOTOR_1 FORWARD.");

      //delay(5000);
      //motor1.run(RELEASE);
    }

    else if(input=="F2" || input=="f2"){
      motor2.setSpeed(Speed);  
      motor2.run(FORWARD);
      Serial.println("MOTOR_2 FORWARD.");

      //delay(5000);
      //motor2.run(RELEASE);
    } 
    
    else if(input=="F3" || input=="f3"){
      motor3.setSpeed(Speed);  
      motor3.run(FORWARD);
      Serial.println("MOTOR_3 FORWARD.");
      //delay(5000);
      //motor3.run(RELEASE);
    }

    else if(input=="F4" || input=="f4"){
      motor4.setSpeed(Speed);  
      motor4.run(FORWARD);
      Serial.println("MOTOR_4 FORWARD.");
      //delay(5000);
      //motor4.run(RELEASE);
    }

    else if (input=="B1" || input=="b1") {
      motor1.setSpeed(Speed); // val between stop [0 - 255] max or speeg(0%--100%)
      motor1.run(BACKWARD);
      Serial.println("MOTOR_1 BACKWARD.");
      //delay(5000);
      //motor1.run(RELEASE);
    }

    else if(input=="B2" || input=="b2"){
      motor2.setSpeed(Speed);  
      motor2.run(BACKWARD);
      Serial.println("MOTOR_2 BACKWARD.");
      //delay(5000);
      //motor2.run(RELEASE);
    } 
    
    else if(input=="B3" || input=="b3"){
      motor3.setSpeed(Speed);  
      motor3.run(BACKWARD);
      Serial.println("MOTOR_3 BACKWARD.");
      //delay(5000);
      //motor3.run(RELEASE);
    }

    else if(input=="B4" || input=="b4"){
      motor4.setSpeed(Speed);  
      motor4.run(BACKWARD);
      Serial.println("MOTOR_4 BACKWARD.");
      //delay(5000);
      //motor4.run(RELEASE);
    }

    else if (input=="S1" || input=="s1") {
      //motor1.setSpeed(speed(80)); // val between stop [0 - 255] max or speeg(0%--100%)
      //motor1.run(BACKWARD);
      //delay(5000);
      motor1.run(RELEASE);
      Serial.println("MOTOR_1 STOP.");

    }

    else if(input=="S2" || input=="s2"){
      //motor2.setSpeed(speed(80));  
      //motor2.run(BACKWARD);
      //delay(5000);
      motor2.run(RELEASE);
      Serial.println("MOTOR_2 STOP.");
    } 
    
    else if(input=="S3" || input=="s3"){
      //motor3.setSpeed(speed(0));  
      motor3.run(RELEASE);
      Serial.println("MOTOR_3 STOP.");
    }

    else if(input=="S4" || input=="s4"){
      //motor4.setSpeed(speed(0));  
      motor4.run(RELEASE);
      Serial.println("MOTOR_4 STOP.");
    }
    else {
      Serial.println("ALL MOTORS RELEASED.");
      motor1.run(RELEASE);
      motor2.run(RELEASE);
      motor3.run(RELEASE);
      motor4.run(RELEASE);
    }
    delay(100);

  }
  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
  uint8_t i;
  
  Serial.print("tick");
  
  motor.run(FORWARD);
  for (i=0; i<255; i++) {
    motor.setSpeed(i);  
    delay(10);
 }
 
  for (i=255; i!=0; i--) {
    motor.setSpeed(i);  
    delay(10);
 }
  
  Serial.print("tock");

  motor.run(BACKWARD);
  for (i=0; i<255; i++) {
    motor.setSpeed(i);  
    delay(10);
 }
 
  for (i=255; i!=0; i--) {
    motor.setSpeed(i);  
    delay(10);
 }
  

  Serial.print("tech");
  motor.run(RELEASE);
  delay(1000);*/
}
