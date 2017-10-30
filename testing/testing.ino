#include <FastLED.h>

#define NUM_LEDS    288
#define BRIGHTNESS  125
#define LED_TYPE    APA102
#define COLOR_ORDER GRB
CRGB leds[NUM_LEDS];

#define UPDATES_PER_SECOND 100
void setup() {
    delay( 3000 ); // power-up safety delay
  //  FastLED.addLeds<LED_TYPE, 11,13, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
    FastLED.addLeds<APA102,11,13,RGB,DATA_RATE_MHZ(1) >(leds,NUM_LEDS);
    FastLED.setBrightness(  BRIGHTNESS );
    int i;

}


void loop() {
  // put your main code here, to run repeatedly:
          int i =0;
    for(i=0; i < 75;i++){
      leds[i].r=0;
      leds[i].g=0;
      leds[i].b=BRIGHTNESS;
     FastLED.show();
    FastLED.delay(1000 / UPDATES_PER_SECOND);
    }
    for(i=0; i < 288;i++){
      leds[i].r=0;
      leds[i].g=0;
      leds[i].b=0;
     FastLED.show();
    FastLED.delay(1000 / UPDATES_PER_SECOND);
    }
}


