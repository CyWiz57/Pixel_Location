import math
import cv2
import numpy as np

path = 'Resources/coin1.jpeg'
x = path.split("/")
x = x[1]
y = x.split(".")
y = y[1]
print(y)
if y == "jpeg": param21 = int(70)
else: param21 = int(20)

image = cv2.imread(path)
output = image.copy()

img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

a = int(input())
b = int(input())

cv2.circle(output, (a, b), 1, (0, 255, 0), 2)

# Find circles
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 100,param1=70,param2=param21,minRadius=28,maxRadius=205)

# If some circle is found
if circles is not None:
   # Get the (x, y, r) as integers
   circles = np.round(circles[0, :]).astype("int")
   print(circles)
   # loop over the circles
   for (x, y, r) in circles:
      cv2.circle(output, (x, y), r, (0, 255, 0), 2)
      cv2.circle(output, (x, y), 1, (0, 255, 0), 2)
      cv2.line(output, (a, b), (x, y), (0, 255, 255), 5)

dist = math.sqrt((x - a)**2 + (y - b)**2)

print("distance between point is ", dist)
print("cordinate X is ", x)
print("cordinate Y is ", y)
print("radius of circle is ", r)

if dist == r:
   print("point is on the circle")
elif dist < r:
   print("point is inside the circle")
else:
   print("point is outside of the circle")

# show the output image
cv2.imshow("circle",output)
cv2.waitKey(0)