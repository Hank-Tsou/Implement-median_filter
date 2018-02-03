import pylab as pl	# matplotlib's subpackage as pl use for graph
import numpy as np	# use numpy library as np for array object
import cv2			# opencv-python

def filtering(grayimg, padding_mage, size):	# median filtering function (original image, padding image, size of filter)
    x, y = grayimg.shape
    final = np.zeros((x, y), dtype='i')					# create a metrix the size same as source image
    m_filter = np.zeros((size*size), dtype='i')			# create the filter array
     
    for count_pixel_x in range(((size-1)/2), x+1):		#count source pixel on padding image
        for count_pixel_y in range(((size-1)/2), y+1):	#count source pixel on padding image
            count_filter = 0							# filter counter in order to fill the pixel in the filter to sort and find the median value
            for count_compare_pixel_x in range(count_pixel_x-((size-1)/2), count_pixel_x+((size-1)/2)+1):		# count the filter position
                for count_compare_pixel_y in range(count_pixel_y-((size-1)/2), count_pixel_y+((size-1)/2)+1):	# count the filter position
                        m_filter[count_filter] = padding_mage[count_compare_pixel_x, count_compare_pixel_y]		# fill the image value in the filter
                        count_filter = count_filter+1	# move to next filter value
            
            m_filter.sort()	# sort the value in the filter
            final[count_pixel_x-((size-1)/2), count_pixel_y-((size-1)/2)]=m_filter[((size*size)-1)/2]			# add the median value in the new image

    return final	# return new image
