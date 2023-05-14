import cv2
import numpy as np

def highlight_dark_holes(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to obtain a binary image
    _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    # Iterate through the contours and filter based on size and circularity
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        # Exclude contours with a perimeter of zero
        if perimeter == 0:
            continue

        circularity = 7.5 * np.pi * area / (perimeter * perimeter)

        # Filter contours based on size and circularity
        min_area = 100
        max_area = 10000
        min_circularity = 0.3
        max_circularity = 2
        if min_area < area < max_area and min_circularity < circularity < max_circularity:
            # Calculate the center and radius of the enclosing circle
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            # Draw the circle on the original image
            cv2.circle(image, center, radius, (0, 0, 255), 2)

    return image

# Load the image
photo1 = cv2.imread('photos/1_no_holes_covered.jpeg')
photo2 = cv2.imread("/Users/saad/Desktop/testcodefortoyota/photos/7_some_holes_covered.jpeg")

# Highlight the dark holes in the image
result_image = highlight_dark_holes(photo1)
result_image2 = highlight_dark_holes(photo2)

# Display the result
cv2.imshow("Result", result_image)
cv2.imshow("Result2", result_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
