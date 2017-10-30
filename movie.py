import cv2,PIL
vidcap = cv2.VideoCapture('movie.mp4')
success,image = vidcap.read()
count = 0
success = True

while success:
  print image[375,833]
  #print('Read a new frame: ', success)
  #cv2.imwrite("./frames/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  count += 1