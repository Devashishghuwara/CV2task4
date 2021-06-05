import cv2

bear = cv2.imread("Bear.jpg")
building = cv2.imread("Building.jpg")

bear_resize = cv2.resize(bear,(200,200))
building_resize = cv2.resize(building,(200,200))


h_concat = cv2.hconcat([building_resize, bear_resize])
cv2.imshow("h_concate",h_concat)
cv2.waitKey()
cv2.destroyAllWindows()

v_concat = cv2.vconcat([building_resize, bear_resize])
cv2.imshow("v_concate",v_concat)
cv2.waitKey()
cv2.destroyAllWindows()

