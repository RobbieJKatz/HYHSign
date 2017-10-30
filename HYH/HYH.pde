/**
 * Array 2D. 
 * 
 * Demonstrates the syntax for creating a two-dimensional (2D) array.
 * Values in a 2D array are accessed through two index values.  
 * 2D arrays are useful for storing images. In this example, each dot 
 * is colored in relation to its distance from the center of the image. 
 */
color pick = color(#10FF00);

float[][] distances;
float maxDistance;
int spacer;
PrintWriter output;
void setup() {
  size(1000 , 1000);
  print(pos[0][0]);
output = createWriter("positions.txt"); 

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
    for (int y = 0; y < 130;y++) {

      point(10, 10+y*spacer/2 + spacer/2);
      output.print('{');
      output.print(10);
      output.print(',');
      output.print(10+y*spacer/2 + spacer/2);
      output.println("},");
    }
    
   // point(5, 380);
    for(int d = -90; d < 0; d++){
      point(10+spacer/2+145+145*cos(d*4*3.141/360),10+380+145*sin(d*4*3.141/360)); 
      output.print('{');
      output.print(10+spacer/2+145+145*cos(d*4*3.141/360));
      output.print(',');
      output.print(10+380+145*sin(d*4*3.141/360));
      output.println("},");
    }
    
    for(int y = 0;y<25;y++){
      point(10+spacer/2+ 290, 10+380+y*spacer/2);
      output.print('{');
      output.print(10+spacer/2+ 290);
      output.print(',');
      output.print( 10+380+y*spacer/2);
      output.println("},");
    }
    
    for(int d = 0; d < 90; d++){
      point(10+spacer/2+145+145+145+145*cos(d*4*3.141/360),10+380+125+145*sin(d*4*3.141/360)); 
      output.print('{');
      output.print(10+spacer/2+145+145+145+145*cos(d*4*3.141/360));
      output.print(',');
      output.print(10+380+125+145*sin(d*4*3.141/360));
      output.println("},");
    }
    for(int y = 171;y>-1;y--){
      point(10+ 290+290+5, 10+ y*spacer/2 + spacer/2);
      output.print('{');
      output.print(10+ 290+290+5);
      output.print(',');
      output.print(10+ y*spacer/2 + spacer/2);
      output.println("},");
    }
    for(int d = -90; d < 0; d++){
      point( 10+290+290+5+145+145*cos(d*4*3.141/360),10+380+145*sin(d*4*3.141/360)); 
      output.print('{');
      output.print(10+290+290+5+145+145*cos(d*4*3.141/360));
      output.print(',');
      output.print(10+380+145*sin(d*4*3.141/360));
      output.println("},");
    }
        for (int y = 0; y < 55;y++) {
      point( 10+290+290+5+145+145, 10+75*5+y*spacer/2 + spacer/2);
      output.print('{');
      output.print(10+290+290+5+145+145);
      output.print(',');
      output.print(10+75*5+y*spacer/2 + spacer/2);
      output.println("},");
    }
 output.flush(); // Writes the remaining data to the file
  output.close(); // Finishes the file
}