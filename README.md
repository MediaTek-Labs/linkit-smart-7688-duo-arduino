## Arduino Supporting Package for LinkIt Smart 7688 Duo

There is a Arduino IDE board support package for LinkIt Smart 7688 (Arduino Compatible). This allows you to program the ATMega32U4 with Arduino IDE.

## ENVIRONMENT
The board support package works with Arduino IDE 1.6.4.

## Installation via Board Manager
{refer to http://pablo-sun.github.io/}

## COM port Driver
The hardware is a USB serial COM port.
 - Bootloader COM port: `VID=0x0E8D, PID=0xAB00`
 - Arduino Sketch COM port: `VID=0x0E8D, PID=0xAB01`

### Windows
A Windows Serial COM port INF driver is located in: `{ARDUINO_SKETCHBOOK_LOCATION}/hardware/mtk/avr/driver/linkit_smart_7688.inf`

### Linux
It should work without the need to install a driver and mounted as {need confirm}

### OS X
It should work without the need to install a driver and mounted as a serial device under `/dev/tty.usbmodem1413`. The number `1413` can be different on each OS X machine.

### How to Build the Release Package
At this moment building the release pakcages requires:
 - Windows
 - 7-zip
 - Python 2.7 with `requests` package installed
 - Internet connection

To build the release package
 - edit [`gen_repo.bat`](gen_repo.bat) and modify the version number
 - then execute `gen_repo.bat`

The build script will zip the `avr` supporting package and create a JSON description file, merging current JSON repository file from `download.labs.mediatek.com`.