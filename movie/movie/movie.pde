import processing.video.*;
 
   Movie test;
 
   void setup() {
     size(1920, 1080);
     background(0);
     test = new Movie(this, "movie.mp4");
     test.loop();
     test.volume(0);
   }
 
   void movieEvent(Movie m) {
     m.read();
   }
 
   void draw() {
     image(test, 0, 0, width, height);
   }