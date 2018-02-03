import pylab as pl	# matplotlib's subpackage as pl use for graph
import numpy as np	# use numpy library as np for array object
import cv2			# opencv-python
from compare_median_filter import filtering

filter_size = input ('filter size (odd number): ')		# input filter size
while filter_size % 2 == 0:								# while input filter size is an even number re-input
    filter_size = input ('filter size (odd number): ')	# input filter size
	
img = cv2.imread('input_image.jpg')						# read image
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)			# convert image to grayscal

x, y = grayimg.shape																# get image size x*y, for a image with x rows and y columns
padding_mage = np.zeros((x+(filter_size-1), y+(filter_size-1)), dtype = 'i')		# create a zero metrix the size of zero depend on the size of image and filter											

for i in range((filter_size-1)/2, x+((filter_size-1)/2)):							# count the x-position where source pixel fill in 
    for j in range((filter_size-1)/2, y+((filter_size-1)/2)):						# count the y-position where source pixel fill in 
        padding_mage[i, j] = grayimg[i-((filter_size-1)/2), j-((filter_size-1)/2)]	# add the image in the center of the zero metrix
																					# so now we create a padding image with zero
final = filtering(grayimg, padding_mage, filter_size)	# call function to do median filtering


blur = cv2.blur(img,(filter_size,filter_size))						# call opencv Bler function
Gaussian_blur = cv2.GaussianBlur(img,(filter_size,filter_size),0)	# call opencv GaussianBlur function
median_blur = cv2.medianBlur(img,filter_size)						# call opencv medianBlur function


### show original and blurring image
pl.subplot(231)					# image position 
pl.imshow(img)					# show image "img"
pl.title('original image')		# graph title "original image"
pl.set_cmap('gray')				# show in gray scale

pl.subplot(232)					# image position
pl.imshow(final)				# show image "final"
pl.title('result image')		# graph title "result image"
pl.set_cmap('gray')				# show in gray scale

pl.subplot(234)					# image position 
pl.imshow(blur)					# show image "blur"
pl.title('blur image')			# graph title "blur image"
pl.set_cmap('gray')				# show in gray scale

pl.subplot(235)					# image position
pl.imshow(Gaussian_blur)		# show image "Gaussian_blur"
pl.title('Gaussian_blur image')	# graph title "Gaussian_blur image"
pl.set_cmap('gray')				# show in gray scale

pl.subplot(236)					# image position
pl.imshow(median_blur)			# show image "median_blur"
pl.title('median_blur image')	# graph title "median_blur image"
pl.set_cmap('gray')				# show in gray scale

pl.show()	                	# output image