FROM valian/docker-python-opencv-ffmpeg

# Here we add current folder on local machine to the container.
ADD . ./code
WORKDIR /code

ENTRYPOINT ["/bin/bash"]
## you can uncommment it here if you want to run start.py from here.
#ENTRYPOINT ["python3"]
#CMD ["readframe.py"]

