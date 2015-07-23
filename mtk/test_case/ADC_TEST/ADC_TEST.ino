

void setup() {

  Serial.begin(115200);
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  pinMode(A3,INPUT);
  pinMode(A4,INPUT);
}

void loop() {
 
// unsigned long t1 = millis();
int data = 0;
//for (int i = 0; i < 100; ++i)
//{
//  data// =analogRead(A0) ;
//}
//unsigned long t2 = millis();
//Serial.println((t2-t1)/100.0);
Serial.print(analogRead(A0));
Serial.print(",");
Serial.print(analogRead(A1));
Serial.print(",");
Serial.print(analogRead(A2));
Serial.print(",");
Serial.print(analogRead(A3));
Serial.print(",");
Serial.print(analogRead(A4));
Serial.print(",");
Serial.println(analogRead(A5));
delay(1000);
}
