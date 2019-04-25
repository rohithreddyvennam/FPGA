void setup() {
  pinMode(2, INPUT);
  pinMode(3, INPUT); 
  pinMode(4, INPUT); 
  pinMode(5, INPUT); 
  pinMode(6, INPUT); 
  pinMode(7, INPUT); 
  pinMode(8, INPUT); 
  pinMode(9, INPUT);
  
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  
  Serial.begin(9600);                       // set the baud rate
  //Serial.println("Ready");                  // print "Ready" once
}

int index=0, nBits=4; 
bool b[4] = {0,0,0,0};

void loop() {
  static char buffer[20];
  static size_t pos;
    if (Serial.available()) {
      char c = Serial.read();
      if (c == '\n') {                      // on end of line, parse the number
            buffer[pos] = '\0';
            int value = atof(buffer);
            b[index] = value;
            index = index+1 ;
            //Serial.println(value);
            if(index == 4){
            index = 0;
            digitalWrite(13,b[3]);
            digitalWrite(12,b[2]);
            digitalWrite(11,b[1]);
            digitalWrite(10,b[0]);
            
            /*
            Serial.println(b[0]);
            Serial.println(b[1]);
            Serial.println(b[2]);
            Serial.println(b[3]);
            */
            delayMicroseconds(4);
            
            int z0 = digitalRead(2);
            int z1 = digitalRead(3);
            int z2 = digitalRead(4);
            int z3 = digitalRead(5);
            int z4 = digitalRead(6);
            int z5 = digitalRead(7);
            int z6 = digitalRead(8);
            int z7 = digitalRead(9);
            
            
            Serial.println(z0);
            Serial.println(z1);
            Serial.println(z2);
            Serial.println(z3);
            Serial.println(z4);
            Serial.println(z5);
            Serial.println(z6);
            Serial.println(z7);
            
        
        }
        pos = 0;
      } else if (pos < sizeof buffer - 1) {   // otherwise, buffer it
      buffer[pos++] = c;
      }
   }
}
