#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M%S")

# This handy command will simply delay the next command by a specified interval
echo "sleeping" 
 sleep 1
echo "done sleeping"

# This takes two photos and stores them in respective folders for each cam
 sudo fswebcam -d /dev/video0 -r 352x288 --no-banner /home/pi/webcam/cam1/$DATE.jpg
 sudo fswebcam -d /dev/video2 -r 352x288 --no-banner /home/pi/webcam/cam2/$DATE.jpg

# This command places another image (with time banner) into a folder that streams to the web note the file location “../../var/www”
 sudo fswebcam -d /dev/video0 -r 352x288 /var/www/webcam/cam1/timelapse.jpg
 sudo fswebcam -d /dev/video2 -r 352x288 /var/www/webcam/cam2/timelapse.jpg

# Now we use the convert command (see imagemagik) to creat gifs
# The -delay gives the interval between picture changes and -loop sets it to repeat
sudo convert -delay 20 -loop 0 /home/pi/webcam/cam1/*.jpg /home/pi/webcam/cam1/timelapse.gif
sudo convert -delay 20 -loop 0 /home/pi/webcam/cam2/*.jpg /home/pi/webcam/cam2/timelapse.gif
echo "creating gif"
 # Now we copy these gifs to the webstream folder  “../../var/www”
 sudo cp /home/pi/webcam/cam1/timelapse.gif /var/www/webcam/cam1/timelapse.gif
 sudo cp /home/pi/webcam/cam2/timelapse.gif /var/www/webcam/cam2/timelapse.gif
echo "copying gif to www folder!"
echo "DONE"
