import cv2

# Read the image file
img = cv2.imread("solar-system.jpg")

# Add text below each planet
cv2.putText(img, "Sun", (102, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 2, 255), 2)
cv2.putText(img, "Mercury", (110, 235), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Venus", (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Earth", (300, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Mars", (380, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img, "Jupiter", (550, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
cv2.putText(img, "Saturn", (800, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
cv2.putText(img, "Uranus", (950, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
cv2.putText(img, "Neptune", (1090, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_systemwithname.jpg", img)
