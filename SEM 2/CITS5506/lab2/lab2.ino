#include <LiquidCrystal.h>
LiquidCrystal lcd(12,11,5,4,3,2);
const int switchPin = 6;
int SwitchState =0;
int prevSwitchState = 0;
int reply;
void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  pinMode(switchPin,INPUT);
  lcd.print("Ask the");
  lcd.setCursor(0,1);
  lcd.print("Crystal Ball!");

}
 
void loop() {
  // put your main code here, to run repeatedly:
  SwitchState = digitalRead(switchPin);
  if (SwitchState != prevSwitchState)
  {
    if (SwitchState == LOW){
      reply = random(8);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("The ball says: ");
      lcd.setCursor(0, 1);
      switch(reply){
        case 0:
          lcd.print("Yes");
          break;
        case 1:
          lcd.print("Most Likely");
          break;
        case 2:
          lcd.print("Certainly");
          break;
        case 3:
          lcd.print("Outlook good");
          break;
        case 4:
          lcd.print("Unsure");
          break;
        case 5:
          lcd.print("Ask Again");
          break;
        case 6:
          lcd.print("Doubtful");
          break;
        case 7:
          lcd.print("No");
          break;
      }
    }
  }
  prevSwitchState = SwitchState;
}
