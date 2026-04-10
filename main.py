import cv2 

#Load Image 
image = cv2.imread('assets/snap_logo.png',cv2.IMREAD_UNCHANGED)

# Resize Image
image = cv2.resize(image,(0,0), fx=2,fy=2)

# Rotate Image
image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# save_image
cv2.imwrite('new_snap_logo.png', image)

# cv2.IMREAD_COLOR = -1
# cv2.IMREAD_GRAYSCALE = 0
# cv2.IMREAD_UNCHANGED = 1

#Show/Display Image
cv2.imshow("SnapChat Logo",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

