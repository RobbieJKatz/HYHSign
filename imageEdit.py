from __future__ import print_function
import cv2, math
f = cv2.imread("./frames/frame98.jpg")
p = [120,120,255]

l = range(126)
l = l[::-1]
for i in l:
	f[425+(int)(i*1.31),838] =p 
	y=425+(int)(i*1.31)
	x=838
	print('[',y,',',x,"],",sep='')



for i in range(70):
	y = 523 + (int)(35*math.sin(2*3.141/360*(i-70)*154/(70)))
	x = 880 + (int)(35*math.cos(2*3.141/360*(i-70)*154/(70)))
	f[y,x] = p
	print('[',y,',',x,"],",sep='')


for i in range(30):
	f[524+i,914] = p
	y=524+i
	x=914
	print('[',y,',',x,"],",sep='')


l = range(66);
l = l[::-1]
for i in l:
	y = 556 + (int)(37*math.sin(2*3.141/360*(i+2)*180/(66)))
	x = 959 + (int)(37*math.cos(2*3.141/360*(i+2)*180/(66)))
	f[y,x] = p
	print('[',y,',',x,"],",sep='')

for i in range(96):
	f[558-(int)(i*1.4), 995]=p
	y=558-(int)(i*1.4)
	x=995
	print('[',y,',',x,"],",sep='')


for i in range(76):
	y = 523 + (int)(36*math.sin(2*3.141/360*(i-76)*154/(76)))
	x = 1040 + (int)(36*math.cos(2*3.141/360*(i-76)*154/(76)))
	f[y,x] = p
	print('[',y,',',x,"],",sep='')

for i in range(51):
	f[522+(int)(i*1*1.4), 1075]=p
	y=522+(int)(i*1*1.4)
	x=1075
	print('[',y,',',x,"],",sep='')

for i in range(77):
	f[575 + (int)(i*1.1),995]=p
	y=575 + (int)(i*1.1)
	x=995
	print('[',y,',',x,"],",sep='')

cv2.imwrite("./test.jpg",f)