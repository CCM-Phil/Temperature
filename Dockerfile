FROM resin/rpi-raspbian:stretch

# Install Python and other dependencies
RUN apt-get update && apt-get install -y python python-dev python-pip mplayer

#RUN pip install RPi.Gpio w1thermsensor
RUN modprobe w1-gpio
RUN modprobe w1-therm
RUN apt-get install git-all -y
RUN pip install git+https://github.com/resin-io/resin-sdk-python.git
ADD . /app

#CMD ["python", "/app/hello.py"]