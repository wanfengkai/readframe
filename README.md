# Read mp4 and get frame img by index with scalable video option 
install ffmpeg on Mac should follow the instruction here [install on Mac](http://www.renevolution.com/ffmpeg/2013/03/16/how-to-install-ffmpeg-on-mac-os-x.html)

Use this with [docker](https://hub.docker.com/r/valian/docker-python-opencv-ffmpeg/) is much easier .


To run the docker:

1. ***docker build -t ffmpeg .***
2. *** docker run -it -v ./vis_folder:/vis_folder ffmpeg:latest ***
3. *** python readframe.py ***
