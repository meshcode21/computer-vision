import cv2, os

#read image
image_path = os.path.join('public', 'cat.jpg')
image = cv2.imread(image_path)

# display original image
print("Original Image Shape:", image.shape)
cv2.imshow("Original Image", image)

# crop image
cropped_image = image[400:800, 400:800] # crop the image from y=400 to y=800 and x=400 to x=800
print("Cropped Image Shape:", cropped_image.shape)
cv2.imshow("Cropped Image", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
