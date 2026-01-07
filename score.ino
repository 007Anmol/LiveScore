#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

String incomingData = "";

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(200);  // IMPORTANT
  
  Wire.begin();
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 10);
  display.println("Waiting for data...");
  display.display();
}

void loop() {
  if (Serial.available() > 0) {
    incomingData = Serial.readStringUntil('\n');
    incomingData.trim();  // REMOVE \r, spaces, junk
    
    if (incomingData.length() > 0) {
      showOnOLED(incomingData);
    }
  }
}

void showOnOLED(String text) {
  display.clearDisplay();
  display.setCursor(0, 0);
  
  int splitIndex = text.indexOf('|');
  
  if (splitIndex > 0) {
    String line1 = text.substring(0, splitIndex);
    String line2 = text.substring(splitIndex + 1);
    
    line1.trim();
    line2.trim();
    
    display.println(line1);
    display.println();
    
    // Handle long headlines (truncate safely)
    if (line2.length() > 60) {
      line2 = line2.substring(0, 60);
    }
    
    display.println(line2);
  } else {
    display.println(text);
  }
  
  display.display();
}