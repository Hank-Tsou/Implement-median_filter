# Median Filter
#### implement a Median filter and compare to other methods.
#### 2. Spatial Filter (input image name: input_image.jpg)

>> This file include: </br>
>>* Readme_1-2</br>
>>* input image.jpg</br>
>>* (Question 2-a) median_filter.py + output_image_a</br>
>>* (Question 2-b) 2_compare.py and compare_median_filter.py + output_image_b</br>

>> #### (A) How to run the code [median_filter.py]
>>> (a) Using the command prompt and direct to the file position. (my example)
>>> <pre> >> [C:\Users\hank\Desktop\Computer Vision\Assignment_1\1-2]

>>> (b) input >> "python median_filter.py" to run the code.
>>> <pre> >> [C:\Users\hank\Desktop\Computer Vision\Assignment_1\1-2>python median_filter.py]

>>> (c) The program will ask to input the image name and filter size (odd number only), 
>>> if the input number is an even number it will ask to input again. Remember have to 
>>> put '' (single quote) when input the image name => 'image name'
>>> <pre> >> [image name(with .pnh .jpg): 'input_image.jpg']</br> >> [filter size (odd number): 3]

>>> (d) The program will show the result include original image and result image. 
	    In the "output_image_a" the first image is original image and then result image with 
	    filter size = 3, 5 and 7. (output_Image_a)

>> #### (B) Compare with openCV function [2_compare.py + compare_median_filter.py]
>>> (a) Using the command prompt and direct to the file position. (my example)
>>> <pre> >> [C:\Users\hank\Desktop\Computer Vision\Assignment_1\1-2]

>>> (b) input >> "python 2_compare.py" to run the code.
>>> <pre> >> [C:\Users\hank\Desktop\Computer Vision\Assignment_1\1-2>python 2_compare.py]

>>> (c) The program will ask to input the filter size (odd number only).
>>> <pre> >> [filter size (odd number): 3]

>>> (d) The program will show five image to compare. (output_Image_b)
>>> Original image, Result image, Blur image, Gaussian blur image and Median blur image    
