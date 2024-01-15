import cv2
import pytesseract

# Read the image file
image = cv2.imread('vaping_refill_pods.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to improve text recognition
thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Use pytesseract to extract text
text = pytesseract.image_to_string(thresholded)

# Print the extracted text
print(text)