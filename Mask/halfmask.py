import cv2
import numpy as np

# original image
image = cv2.imread('zero.jpg')

# mask (of course replace corners with yours)
mask = np.zeros(image.shape, dtype=np.uint8)
roi_corners = np.array([[(1,1), (1,190), (140,190), (140,1)]], dtype=np.int32)

#271x195
#roi_corners = np.array([[(1,1), (340,340), (100,300)]], dtype=np.int32)
#                           t     lb triangle rb
#    top
#  l     r
#
#   bottom
#



white = (255, 255, 255)
cv2.fillPoly(mask, roi_corners, white)

# apply the mask
masked_image = cv2.bitwise_and(image, mask)

# display your handywork
cv2.imshow('masked image', masked_image)
cv2.imwrite('Masked.jpg',masked_image)
cv2.waitKey()
cv2.destroyAllWindows()
