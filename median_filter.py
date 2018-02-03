import pylab as pl	#matplotlib's subpackage as pl use for graph
import numpy as np	#use numpy library as np for array object
import cv2			#opencv-python

def filtering(padding_mage, size):	#median filtering function (padding image, size of filter)
    
    final = np.zeros((x, y), dtype='i')					# create a metrix the size same as grayimg image
    m_filter = np.zeros((size*size), dtype='i')			# create the filter array
     
    for count_pixel_x in range(((size-1)/2), x+1):		#count grayimg pixel on padding image
        for count_pixel_y in range(((size-1)/2), y+1):	#count grayimg pixel on padding image
            count_filter = 0							# filter counter in order to fill the pixel in the filter to sort and find the median value
            for count_compare_pixel_x in range(count_pixel_x-((size-1)/2), count_pixel_x+((size-1)/2)+1):		# count the filter position
                for count_compare_pixel_y in range(count_pixel_y-((size-1)/2), count_pixel_y+((size-1)/2)+1):	# count the filter position
                        m_filter[count_filter] = padding_mage[count_compare_pixel_x, count_compare_pixel_y]		#fill the image value in the filter
                        count_filter = count_filter+1	# move to next filter value
            
            m_filter.sort()	# sort the value in the filter
            final[count_pixel_x-((size-1)/2), count_pixel_y-((size-1)/2)]=m_filter[((size*size)-1)/2]			# add the median value in the new image

    return final	#return new image

### main
image_name = input ('image name(with .png .jpg): ')		# input image name

filter_size = input ('filter size (odd number): ')		# input filter size
while filter_size % 2 == 0:								# while input filter size is an even number re-input
    filter_size = input ('filter size (odd number): ')	# input filter size

img = cv2.imread(image_name)							# read image
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)			# convert image to grayscal

### padding image with zero: set all pixels outside the grayimg image to 0
x, y = grayimg.shape																# get image size x*y, for a image with x rows and y columns
padding_mage = np.zeros((x+(filter_size-1), y+(filter_size-1)), dtype = 'i')		#create a zero metrix the size of zero depend on the size of image and filter											

for i in range((filter_size-1)/2, x+((filter_size-1)/2)):							# count the x-position where grayimg pixel fill in 
    for j in range((filter_size-1)/2, y+((filter_size-1)/2)):						# count the y-position where grayimg pixel fill in 
        padding_mage[i, j] = grayimg[i-((filter_size-1)/2), j-((filter_size-1)/2)]	# add the image in the center of the zero metrix
																					# so now we create a padding image with zero

final = filtering(padding_mage, filter_size)	#call function to do median filtering

### show original and blurring image
pl.subplot(121)				# image position 1 row, 2 column, first position
pl.imshow(grayimg)			# show image "grayimg"
pl.title('original image')	# graph title "original image"
pl.set_cmap('gray')			# show in gray scale

pl.subplot(122)				# image position 1 row, 2 column, second position
pl.imshow(final)			# show image "final"
pl.title('result image')	# graph title "result image"
pl.set_cmap('gray')			# show in gray scale

pl.show()	                # output image