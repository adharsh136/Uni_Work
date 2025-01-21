#include <LiquidCrystal.h>

  LiquidCrystal lcd(12,11,5,4,3,2);

void setup() {
  // put your setup code here, to run once:
  analogWrite(6,100);
  lcd.begin(16,2);
}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.setCursor(1,0);
  lcd.print("SUPERB TECH");
}
