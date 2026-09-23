import cv2

filename = "in.png"

img = cv2.inread(filename)

img[:,:,1] = 0

img = cv2.resize(img(100,100)) 