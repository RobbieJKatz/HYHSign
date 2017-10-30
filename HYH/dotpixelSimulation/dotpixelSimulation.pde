Pixels pixel;
 color pick = color(#10FF00);

float[][] distances;
float maxDistance;
int spacer;
void setup() {
  size(1000 , 1000);
  spacer = 10;
  strokeWeight(5);
  noLoop();  // Run once and stop
}
void draw() {
  background(0);
  // This embedded loop skips over values in the arrays based on
  // the spacer variable, so there are more values in the array
  // than are drawn here. Change the value of the spacer variable
  // to change the density of the points
       stroke(pick);
      stroke(255,0,0);

        for(int i = 0; i < 652;i++){
              point(pixel.getX(i), pixel.getY(i));

        }
      
}