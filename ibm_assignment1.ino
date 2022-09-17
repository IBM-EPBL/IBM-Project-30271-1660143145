int t=2;
int e=3;
void setup()
{
  pinMode(t,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
  pinMode(e,INPUT);
  Serial.begin(9600);
}
void loop()
{
  digitalWrite(t,0);
  digitalWrite(t,1);
  delayMicroseconds(10);
  digitalWrite(t,0);
  float dur=pulseIn(e,HIGH);
  int dis=(dur*0.0343)/2;
  Serial.print("Distance is");
  Serial.println(dis);
  if(dis<100)
    digitalWrite(12,1);
  else
    digitalWrite(12,0);
  analogWrite(1,map(dis,2,320,255,0));
  double a=analogRead(A0);
  double t=(((a/1024)*5)-0.5)*100;
  Serial.print("Temperature is:");
  Serial.println(t);
  if(t>100)
    digitalWrite(13,1);
  else
    digitalWrite(13,0);
 }