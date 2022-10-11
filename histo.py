import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:/FYP/Rotoscope/Data sets/New folder (3)/persons/person_005.bmp")

b, g, r = cv2.split(img)

cv2.imshow("img",img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

plt.hist(b.ravel(), 256, [0,256])

plt.hist(g.ravel(), 256, [0,256])

plt.hist(r.ravel(), 256, [0,256])

#hist = cv2.calcHist([img], [0], None, [256], [0, 256])

#plt.plot(hist)

plt.show()