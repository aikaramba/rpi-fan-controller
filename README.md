# External fan controller program for Raspberry Pi
## About
This program controls the external fan for Raspberry Pi.
It uses temperature sensor to change the output value on a selected GPIO pin.

## How to use
0) Install python3
```
sudo apt-get install python3
```
1) Copy 'fan_controller.py' file to a RaspberryPi's SDCard
2) Add the application to the '/etc/rc.local' for auto-launch on startup

For example:
```
python /home/pi/fan_controller.py &
```
This line should be inserted before 'exit 0' line.

## References
1. Original code and fan wiring guide - https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c
