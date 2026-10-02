import cv2
import os

# read image
# cat.jpg is inside the public folder of the project
image_path = os.path.join('public', 'cat.jpg')
image = cv2.imread(image_path)

#write image to file
output_path = os.path.join(os.path.dirname(__file__), "output_cat.jpg")
cv2.imwrite(output_path, image)

# visualize image
cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()