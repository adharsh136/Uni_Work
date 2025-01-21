#include <WiFi.h>
#include <ThingSpeak.h>

#define CHANNEL_ID 2286761
#define CHANNEL_API_KEY "EPBNJOD1B8ZXNTRM"

WiFiClient client;

int counter = 0;

#define WIFI_NETWORK "SpeedWagon 2.4G"
#define WIFI_PASSWORD "jamesbond007"
#define WIFI_TIMEOUT_MS 20000 //U dont want ESP32 to keep trying to connect in case the name and password dont match

void connectToWiFi(){
  Serial.print("Connecting to Wifi");
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_NETWORK,WIFI_PASSWORD);

  unsigned long startAttemptTime = millis();

  //millis() function returns the uptime of the ESP32

  while(WiFi.status() != WL_CONNECTED && millis() - startAttemptTime < WIFI_TIMEOUT_MS){
    Serial.print(".");
    delay(100);
  }

  if(WiFi.status() != WL_CONNECTED){
  Serial.println("Failed to connect to the network!");
  // take action write some code bitch
  }
  else{
  Serial.println("Connected to the network!");
  Serial.println(WiFi.localIP());
  }
}
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  connectToWiFi();
  ThingSpeak.begin(client);
}

void loop() {
  // put your main code here, to run repeatedly:
  counter++;
  ThingSpeak.setField(1,counter);
  ThingSpeak.setField(2,WiFi.RSSI());

  ThingSpeak.writeFields(CHANNEL_ID, CHANNEL_API_KEY);


  delay(15000);

}
