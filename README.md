## Arduino Supporting Package for LinkIt Smart 7688 Duo

There is a Arduino IDE board support package for LinkIt Smart 7688 (Arduino Compatible). This allows you to program the ATMega32U4 with Arduino IDE.

## ENVIRONMENT
The board support package shoud work with Arduino IDE 1.6.4 and later

## COM port
The hardware is a USB serial COM port.
 - Bootloader COM port: `VID=0x0E8D, PID=0xAB00`
 - Arduino Sketch COM port: `VID=0x0E8D, PID=0xAB01`

### Windows
A Windows Serial COM port INF driver is located in: `{ARDUINO_SKETCHBOOK_LOCATION}/hardware/mtk/avr/driver/linkit_smart_7688.inf`
Note that in Window 8 you'll need to disable the "Driver Signature Enforcement" and in Windows 10 there is no need to install INF drivers - Windows 10 should recognize the board as a general USB Serial port.

### Linux
It should work without the need to install a driver and mounted as. But just like normal arduino boards, it needs some additional permission configurations. For more detailed information, see the article on [ArchWiki](https://wiki.archlinux.org/index.php/arduino#Accessing_serial) and [Debian Wiki](https://wiki.debian.org/Arduino) for different distributions.

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
