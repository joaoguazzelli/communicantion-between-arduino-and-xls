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
      Serial.println(123);
      Serial.println(123);
      Serial.println(123);
      Serial.println(123);
      Serial.println(123);
      Serial.println(123);
    }
  }
}
 
