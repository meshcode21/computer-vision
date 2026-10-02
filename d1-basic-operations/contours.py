import cv2 as cv, os

# read image
image_path = os.path.join('public', 'birds.png')
image = cv.imread(image_path)

# image thresholding
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(image_gray, 127, 255, cv.THRESH_BINARY_INV) 
# thresh = cv.adaptiveThreshold(image_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,2)

# find contours
contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# draw contours
cv.drawContours(image, contours, -1, (0, 255, 0), 1)

# find up-per-left and bottom-right points of contours
for contour in contours:
    x, y, w, h = cv.boundingRect(contour)
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)

# display number of contours on the image
cv.putText(image, f"Contours: {len(contours)}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

# display image
cv.imshow("Image", image)
# cv.imshow("Threshold", thresh)

cv.waitKey(0)
cv.destroyAllWindows()