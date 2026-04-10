import cv2


img = cv2.imread("assets/snap_logo.png",cv2.IMREAD_UNCHANGED)

img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

img = cv2.resize(img, (0,0), fx=2,fy=4)

cv2.imshow("Snapchat_Logo", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
