int i=100;
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
    i++;
    while(Serial.read() != '>')
    {
      Serial.println(i);
      Serial.println(i);
      Serial.println(i);
      Serial.println(i);
      Serial.println(i);
      Serial.println(i);
    }
  }
}
 