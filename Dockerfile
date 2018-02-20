FROM jrottenberg/ffmpeg:3.1

#ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y --force-yes build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
                    libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev \
                    python3-dev python3-tk python3-numpy python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
           /tmp/* \
           /var/tmp/*

RUN pip3 install ffmpy

# Here we add the library that we must need
RUN cd
RUN apt-get update && \
    apt-get install -y -q libavdevice-dev libbz2-dev



# Here we add current folder on local machine to the container.
RUN mkdir /code
ADD . /code
WORKDIR /code

ENTRYPOINT ["/bin/bash"]
## you can uncommment it here if you want to run start.py from here.
#ENTRYPOINT ["python3"]
#CMD ["readframe.py"]

