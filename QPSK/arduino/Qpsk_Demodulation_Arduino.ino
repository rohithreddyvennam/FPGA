void setup() {
  
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT); 
  pinMode(4, OUTPUT); 
  pinMode(5, OUTPUT); 
  pinMode(6, OUTPUT); 
  pinMode(7, OUTPUT); 
  pinMode(8, OUTPUT); 
  pinMode(9, OUTPUT);
  
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  
  Serial.begin(9600);                       // set the baud rate
  //Serial.println("Ready");                  // print "Ready" once
}

//bool  b[8] = {1,1,1,1,1,1,1,1};
bool  b[8] = {0,0,0,0,0,0,0,0};
int count = 0 ;

void loop() {
  static char buffer[20];
  static size_t pos;
    if (Serial.available()) {
      char c = Serial.read();
      if (c == '\n') {                      // on end of line, parse the number
        buffer[pos] = '\0';
        int value = atof(buffer);    
	//Serial.println(value);
        if(value>0){
          b[count]= 0;
          b[count+1]= 1;
        } else {
          b[count]= 1;
          b[count+1]= 1;      
        }
        //Serial.println(b[7-count]);
        count = count + 2;
		
	if(count == 8) {
	    digitalWrite(2, b[0]);
	    digitalWrite(3, b[1]);
	    digitalWrite(4, b[2]);
	    digitalWrite(5, b[3]);
	    digitalWrite(6, b[4]);
	    digitalWrite(7, b[5]);
	    digitalWrite(8, b[6]);
            digitalWrite(9, b[7]);
			
	    delayMicroseconds(4);
			
	    int z3 = digitalRead(13);
	    int z2 = digitalRead(12);
	    int z1 = digitalRead(11);
	    int z0 = digitalRead(10);
			
	    Serial.println(z0);
	    Serial.println(z1);
	    Serial.println(z2);
	    Serial.println(z3);
			
	    count = 0 ;
        }
        pos = 0;
      } else if (pos < sizeof buffer - 1) {   // otherwise, buffer it
      buffer[pos++] = c;
      }
   }
}

