import cv2
"""
#reading image
img = cv2.imread("F:\\phone\\pho d\\Download\\images (3).jpeg")
#img = cv2.imread("C:\\Users\\dell\\Desktop\\Trupti\\my photo\\pic 1.jpg")
#converting BGR image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#image inversion
inverted_img = 255 - gray_img
blurred = cv2.GaussianBlur(inverted_img, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_img, inverted_blurred , scale = 256.0)

#show image
cv2.imshow("Original image",img)

cv2.imshow("Pencil image",pencil_sketch)

cv2.waitKey(0)

#save
#pencil_sketch.save("F:\\phone\\pho d\\Download\\images (3) sketch.png") #error
#cv2.imwrite("C:\\Users\\dell\\Desktop\\Trupti\\my photo\\pic 1 sketch.jpg",pencil_sketch)

"""
#reading image
#img2 = cv2.imread("C:\\Users\\dell\\Desktop\\Trupti\\my photo\\pic 1.jpg")
img_path = input("Enter path: ")
img2 = cv2.imread(img_path)
#convert into gray
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#blurr gray image
gray_blurred2 = cv2.GaussianBlur(gray_img2, (21, 21), 0)


pencil_sketch2 = cv2.divide(gray_img2, gray_blurred2 , scale = 256.0)

#show both original and edited image
cv2.imshow("Oiginal image 2 ",img2)
cv2.imshow("pencil sketch 2 ",pencil_sketch2)
