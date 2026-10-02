import os, cv2

# read image
image_path = os.path.join('public', 'cat.jpg')
image = cv2.imread(image_path)

# display original image
print("Original Image Shape:", image.shape)
cv2.imshow("Original Image", image)

# resize image
resized_image = cv2.resize(image, (400, 400))
print("Resized Image Shape:", resized_image.shape)
cv2.imshow("Resized Image", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()