import time
from dotstar import Adafruit_DotStar
datapin   = 23
clockpin  = 24
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)
strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

count = 0;
while True:
	counter = 0;
	if(count < 400):
		with open("./textfiles/"+str(count)+'.txt') as f:
			for i in range(592):
				s=f.readline();
				ss = s.split(',');

				color = ss[0]<<8+ss[1]<<8+ss[2]
				strip.setPixelColor(i, color)
				counter=counter+1
				strip.show()                     # Refresh strip
       			time.sleep(1.0 / 50)

		count+=1
	else:
		count=0
		break


