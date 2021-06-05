import numpy as np, cv2
#return image data in array
bear = cv2.imread("Bear.jpg")
desert= cv2.imread("desert.jpg")

cv2.imshow("Bear",bear)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Desert",desert)
cv2.waitKey()
cv2.destroyAllWindows()

bear.shape

desert.shape

#swapping
bear_crop = bear[50:270,150:420]
desert[50:270,150:420] = bear_crop
cv2.imshow("new",desert)
cv2.waitKey()
cv2.destroyAllWindows()

bear = cv2.imread("Bear.jpg")
desert= cv2.imread("desert.jpg")

#swapping
crop_desert = desert[50:270,150:420]
bear[50:270,150:420] = crop_desert
cv2.imshow("new",bear)
cv2.waitKey()
cv2.destroyAllWindows()







