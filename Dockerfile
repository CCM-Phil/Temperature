FROM resin/rpi-raspbian:stretch

# Install Python and other dependencies
RUN apt-get update && apt-get install -y python python-dev python-pip mplayer

#RUN pip install RPi.Gpio w1thermsensor
#RUN sudo modprobe w1-gpio
#RUN sudo modprobe w1-therm

ADD . /app

#CMD ["python", "/app/hello.py"]