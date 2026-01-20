# Demo code for pothole detection 

import cv2

image = cv2.imread("sample_road_image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 150)

cv2.imshow("Detected Road Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
