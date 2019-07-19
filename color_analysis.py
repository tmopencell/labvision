# From https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
# import the necessary packages
import sys
sys.path.append('/home/pi/.local/lib/python3.5/site-packages')
import numpy as np
import argparse
import cv2
import datetime
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load the image
image = cv2.imread(args["image"])
# define the list of boundaries
boundaries = [
    ([0, 0, 10], [50, 50, 255])
]
# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    # Save the images
    timenow = datetime.datetime.now()
    filename1 = timenow.strftime("%Y-%m-%d-%H%M%S")
    cv2.imwrite(filename1+".jpg", output)   # Or np.hstack([image,output])
    #cv2.waitKey(0)
    output_max = np.max(output)
    output_min = np.min(output)
    output_norm = (output - output_min)/(output_max - output_min)
    total_pixels = output_norm.shape[0]*output_norm.shape[1]
    abovethreshold_pixels = (output_norm > 1).sum()
    norm_abovethreshold = (abovethreshold_pixels/total_pixels)*100
    print(total_pixels, abovethreshold_pixels, norm_abovethreshold )
    if norm_abovethreshold > 10:
        print (filename1, "Red in frame")
	f = open('binary.csv','a')
	f.write(filename1+', 1 \n') #Give your csv text here.
	## Python will convert \n to os.linesep
	f.close()
    elif norm_abovethreshold <= 10:
        print (filename1, "NO Red in frame")
	f = open('binary.csv','a')
        f.write(filename1+', 0 \n') #Give your csv text here.
        ## Python will convert \n to os.linesep
        f.close()
