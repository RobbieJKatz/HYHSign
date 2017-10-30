import time
from dotstar import Adafruit_DotStar

numpixels = 592
datapin   = 23
clockpin  = 24
strip     = Adafruit_DotStar(numpixels)
strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

x []
for i in range(400):
	with open("./textfiles/"+str(i)+'.txt') as f:
		x[i].append(int(f.readLine()));



count = 0;
while True:
        counter = 0;
        if(count < 400):
               
		for i in range(592):
			color = x[count][i]
			strip.setPixelColor(i, color)
			counter=counter+1
			strip.show()                     # Refresh strip
			time.sleep(1.0 / 50)
            print(count)
            count+=1
        else:
                count=0