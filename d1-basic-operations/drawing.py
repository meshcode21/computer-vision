import cv2, os

# read image
image_path = os.path.join('public', 'whiteboard.jpg')
image = cv2.imread(image_path)

# circle
cv2.circle(image, (300, 300), 100, (0, 0, 255), -1) # draw a circle with center at (300, 300), radius 100, color green and thickness 5

#line
cv2.line(image, (900, 100), (900, 800), (0, 0, 0), 5) # draw a line from (100, 100) to (500, 500) with color green and thickness 5

# rectangle
cv2.rectangle(image, (100, 100), (500, 500), (0, 0, 0), 5, ) # draw a rectangle from (100, 100) to (500, 500) with color green and thickness 5

# display image
print("Image Shape:", image.shape)
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()