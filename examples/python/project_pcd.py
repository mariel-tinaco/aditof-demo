import numpy as np
import cv2
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('tkagg')



height, width = 256, 256

# generate a random sample of 1000 (x,y) coordinates and colors
x, y, = np.random.randint(0, 256, size=(2, 1000))
color = np.random.randint(0, 256, size=(1000, 3))

# generate a blank image
# int16 to manage overflow colors when convolving
pointsPlotted = np.zeros((height, width, 3), np.uint16)

# plot x,y,color into blankImage
pointsPlotted[y, x] = color


cv2.imshow("points", pointsPlotted.astype(np.uint8))

# convlove the image with a kernel of ones, size k
k = 5
kernel = np.ones((k, k), np.int16)

largerSquares = cv2.filter2D(src=pointsPlotted, ddepth=-1, kernel=kernel)

# limit max color to 255
largerSquares[largerSquares > 255] = 255

# Convert to uint8
largerSquares = largerSquares.astype(np.uint8)

# cv2.imshow("Larger Squares", largerSquares)
plt.imshow(largerSquares)
plt.scatter(x, y, c=color/255, marker="s",s=1)
plt.show()