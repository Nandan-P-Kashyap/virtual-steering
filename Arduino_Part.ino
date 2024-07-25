int data;
int en=12;
int in1=11;
int in2=10;
void setup() {
  Serial.begin(9600);
  pinMode(en,OUTPUT);
  digitalWrite(en,HIGH);
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
}

void loop() {
  while(Serial.available())
  { 
    data=Serial.read();
    Serial.write(data);
  }
  if (data=='1')
  {digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  delay(1000);
  }
  if (data=='2')
  {digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  delay(1000);
  }
  if(data=='0')
  {digitalWrite(in1,LOW);
   digitalWrite(in2,LOW);
  }
  if(data=='3')
 digitalWrite(en,LOW);
 digitalWrite(in1,LOW);
   digitalWrite(in2,LOW);
}
