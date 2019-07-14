
#------------------------------------#
# Author: Yueh-Lin Tsou              #
# Update: 7/10/2019                  #
# E-mail: hank630280888@gmail.com    #
#------------------------------------#

"""---------------------------
Implement Median Filtering
---------------------------"""

# Import OpenCV Library, numpy and command line interface
import cv2
import numpy as np
import argparse
from matplotlib import pyplot as plt

# -------------------------- Median filter function -------------------------- #

def filtering(grayimg, padding_mage, size):	#median filtering function (padding image, size of filter)
    x, y = grayimg.shape
    final = np.zeros((x, y), dtype='i') # create a metrix the size same as grayimg image
    m_filter = np.zeros((size*size), dtype='i') # create the filter array

    for count_pixel_x in range(((size-1)//2), x+1):		#count grayimg pixel on padding image
        for count_pixel_y in range(((size-1)//2), y+1):	#count grayimg pixel on padding image
            count_filter = 0							# filter counter in order to fill the pixel in the filter to sort and find the median value
            for count_compare_pixel_x in range(count_pixel_x-((size-1)//2), count_pixel_x+((size-1)//2)+1):		# count the filter position
                for count_compare_pixel_y in range(count_pixel_y-((size-1)//2), count_pixel_y+((size-1)//2)+1):	# count the filter position
                        m_filter[count_filter] = padding_mage[count_compare_pixel_x, count_compare_pixel_y]		#fill the image value in the filter
                        count_filter = count_filter+1	# move to next filter value

            m_filter.sort()	# sort the value in the filter
            final[count_pixel_x-((size-1)//2), count_pixel_y-((size-1)//2)]=m_filter[((size*size)-1)//2]			# add the median value in the new image

    return final #return new image

# -------------------------- main -------------------------- #
if __name__ == '__main__':
    # read one input from terminal
    # (1) command line >> python re.py -i input_image.jpg -s 3

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the input image")
    ap.add_argument("-s", "--fsize", required=True, help="input filter size (odd)")
    args = vars(ap.parse_args())

    # Read image
    image = cv2.imread(args["image"])
    fsize = int(args["fsize"])

    boarder = (fsize-1)//2

    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    padding_mage= cv2.copyMakeBorder(grayimg,boarder,boarder,boarder,boarder,cv2.BORDER_CONSTANT,value=0)

    final = filtering(grayimg, padding_mage, fsize)	#call function to do median filtering

    ### show original and result image
    plt.subplot(121)
    plt.imshow(grayimg)
    plt.title('original image')
    plt.set_cmap('gray')
    plt.subplot(122)
    plt.imshow(final)
    plt.title('result image')
    plt.set_cmap('gray')
    plt.show()
