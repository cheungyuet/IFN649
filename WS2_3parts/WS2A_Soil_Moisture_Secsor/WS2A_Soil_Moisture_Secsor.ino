const int ledPin = 11;
const int soilPin = 20;

//the setup method runs once, when the stetch starts

void setup() {
  // initialize the digitial pin as an output
  pinMode(ledPin, OUTPUT);
  Serial.begin(9800);
}

void loop() {
  int val = analogRead(soilPin);
  Serial.print("Soil: ");
  Serial.println(val);
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(1000);
}
