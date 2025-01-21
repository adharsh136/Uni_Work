#include "HX711.h"
#define LOADCELL_DOUT_PIN  35
#define LOADCELL_SCK_PIN  15
HX711 scale;
 

 
float weight; 
#define calibration_factor 211000 // for me this value works
 
void setup() {
  // Set up serial monitor
  Serial.begin(9600);
  
  Serial.println("HX711 scale");
  
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor);
  scale.tare(); //Reset the scale to 0
  Serial.println("Readings:");
}

void measureweight(){
  weight = scale.get_units(); 
    if(weight<0)
  {
    weight=0.00;
    }
  //Serial.print(scale.get_units(), 2);
  Serial.print("Kilogram:");
  Serial.print( weight); 
  Serial.print(" Kg");
  Serial.println();
  // Delay before repeating measurement
  delay(1000);
}

 void loop() {
  measureweight();
}
 


