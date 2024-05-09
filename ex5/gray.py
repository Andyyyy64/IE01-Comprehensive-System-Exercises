import cv2
img = cv2.imread("ex5_2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite("ex5_2_gray.jpg", gray)
