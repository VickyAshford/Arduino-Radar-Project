#include <Servo.h>   // Include the library
#define TRIG 10
#define ECHO 11

Servo myservo;       // Create servo object

void setup() {
  myservo.attach(9); // Connect servo to pin 9
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Add variable i declaration
  for (int i = 0; i <= 180; i++) { 
    myservo.write(i); 
    Measure();
    delay(15); // Small delay for smooth servo movement
  }
  
  myservo.write(0);    // Turn to 0 degrees
  Measure();
  delay(1000);         // Wait 1 second

  myservo.write(90);   // Turn to 90 degrees
  Measure();
  delay(1000);

  myservo.write(180);  // Turn to 180 degrees
  Measure();
  delay(1000);
}

void Measure() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10); // Short pulse
  digitalWrite(TRIG, LOW);

  long duration = pulseIn(ECHO, HIGH); // Measure duration
  int distance = duration * 0.034 / 2; // 0.034 cm/µs - speed of sound

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(100); // Reduce delay for more frequent measurements
}