#!/usr/bin/python
import time
from dotstar import Adafruit_DotStar
#grb
numpixels = 590
datapin   = 23
clockpin  = 24
strip     = Adafruit_DotStar(numpixels)
strip.begin()           # Initialize pins for output
strip.setBrightness(255) # Limit brightness to ~1/4 duty cycle
x = [[[0 for k in xrange(3)] for j in xrange(592)] for i in xrange(400)]
for i in range(400):
#       print i
        with open("/home/pi/Adafruit_DotStar_Pi/newest/"+str(i)+'.txt') as f:
#               print "open"
                for ii in range(590):
                        s=((f.readline()))
                #       print s
                        if(s=='0\n'):
                                x[i][ii][0] = int(0.4*(255))
                                x[i][ii][1] = int(0.4*(255))
                                x[i][ii][2] = int(0.4*(255))

                        if(s=="1\n"):
                                x[i][ii][0] = int(0.4*(0))
                                x[i][ii][1] = int(0.4*(0))
                                x[i][ii][2] = int(0.4*int(0))

                        if(s=="2\n"): #turquoise
                                x[i][ii][0] = int(0.4*int(208))#64 224 208
                                x[i][ii][1] = int(0.4*int(64))
                                x[i][ii][2] = int(0.4*int(224))
                        if(s=="3\n"): #yellow
                                x[i][ii][0] = int(0.4*int(255))#255 255 0
                                x[i][ii][1] = int(0.4*int(255))
                                x[i][ii][2] = int(0.4*int(0))
                        if(s=="4\n"):#grey
                                x[i][ii][0] = int(0.4*int(100))
                                x[i][ii][1] = int(0.4*int(100))
                                x[i][ii][2] = int(0.4*int(100))
                        if(s=="5\n"):#orange
                                x[i][ii][0] = int(0.4*int(65)) #255 165 0
                                x[i][ii][1] = int(0.4*int(255))
                                x[i][ii][2] = int(0.4*int(0))
count = 0;
while True:
        counter = 0;
        if(count < 397):

                for i in range(590):
                        color = x[count][i]
                        strip.setPixelColor(i, color[0],color[1],color[2])
                        counter=counter+1
                strip.show()                     # Refresh s    
                time.sleep(1.0 / 25)

#               print(count)
                count+=1

        else:
                time.sleep(10)
                count=0


