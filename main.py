import cv2

# Load the two images
img1 = cv2.imread('Photos/noSticker.jpg')
img2 = cv2.imread('Photos/oneSticker.jpg')

# Compute the absolute difference between the two images
diff = cv2.absdiff(img1, img2)

# Convert the difference to grayscale
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# Apply threshold to filter out small differences
threshold_value = 32 # adjust to fit your use case
_, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# Apply a median filter to remove noise
kernel_size = 3 # adjust to fit your use case
median = cv2.medianBlur(thresh, kernel_size)

# Find contours of the differences
contours, _ = cv2.findContours(median, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles around the differences
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Display the images with differences highlighted
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
