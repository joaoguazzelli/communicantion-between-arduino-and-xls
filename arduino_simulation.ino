int i;
int led = 7;
int sup;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led,OUTPUT);
 }

void loop() {
  if(Serial.read() == '<')
  {
    while(Serial.read() != '>')
    {
      Serial.println(analogRead(A0));
      Serial.println(analogRead(A0));
      Serial.println(analogRead(A0));
      Serial.println(analogRead(A3));
      Serial.println(analogRead(A3));
      Serial.println(analogRead(A3));
    }
  }
  if(Serial.read() == '$')
  {
    while(Serial.read() != '*')
    {
      if(Serial.read() == '0')
      {
        digitalWrite(led,HIGH);
        delay(500);
        digitalWrite(led,LOW);
      }
    }
   }
}
 
