int volt_read1;
int volt_read2;
int curr_read1;
int curr_read2;
int temp_read1;
int temp_read2;

float volt1;
float volt2;
float curr1;
float curr2;
float temp1;
float temp2;
float Tr1;
float R1;
float Tr2;
float R2;


void setup() {
  Serial.begin(9600);
}

void loop() {

  volt_read1 = analogRead(A0);
  volt1 = volt_read1 * (5/1023.0) * (1 / 1.04) * 2;
  Serial.print("(volt1)");
  Serial.print(volt1);
 
  volt_read2 = analogRead(A1);
  volt2 = volt_read2 * (5/1023.0) * 1.0;
  Serial.print("(volt2)");
  Serial.print(volt2);

  curr_read1 = analogRead(A2);
  curr1 = ((curr_read1 * (5/1023.0) * (1 / 1.04) - 0.5) / 0.4) * (10/7);
  Serial.print("(curr1)");
  Serial.print(curr1);
  
  curr_read2 = analogRead(A3);
  curr2 = curr_read2 * (5/1023.0) * 1.0;
  Serial.print("(curr2)");
  Serial.print(curr2);

  temp_read1 = analogRead(A6);
  temp1 = temp_read1 * (5/1023.0) * (1 / 1.04);
  R1 = temp1 / ((5 - temp1) / 22100);
  Tr1 = 1 / (0.003354016 + 0.000256985 * log(R1 / 10000) + 0.000002620131 * pow(log(R1 / 10000), 2) + 0.00000006833091 * pow(log(R1 / 10000), 3)) - 273.15;
  Serial.print("(temp1)");
  Serial.print(Tr1);

  temp_read2 = analogRead(A7);
  temp2 = temp_read2 * (5/1023.0) * (1 / 1.04);
  R2 = temp1 / ((5 - temp2) / 22100);
  Tr2 = 1 / (0.003354016 + 0.000256985 * log(R2 / 10000) + 0.000002620131 * pow(log(R2 / 10000), 2) + 0.00000006833091 * pow(log(R2 / 10000), 3)) - 273.15;
  Serial.print("(temp2)");
  Serial.print(Tr2);

}
