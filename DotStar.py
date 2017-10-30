# import time
import numpy as np
# from dotstar import Adafruit_DotStar
# numpixels = 592 # Number of LEDs in strip

# datapin   = 23
# clockpin  = 24
# strip     = Adafruit_DotStar(numpixels, datapin, clockpin)
# strip.begin()           # Initialize pins for output
# strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

count = 0;
while True:
	counter = 0;
	if(count < 400):
		with open("./textfiles/"+str(count)+'.txt') as f:
			for i in range(592):
				s=f.readline();
				ss = s.split(',');

                color = (np.uint8(ss[0])<<8)+(np.uint8(ss[1])<<8)+(np.uint8(ss[2])<<8)
                counter=counter+1
                print(color)

				#strip.setPixelColor(i, color)
				#strip.show()                     # Refresh strip
       			#time.sleep(1.0 / 50)

		count+=1
	else:
		count=0
		break


