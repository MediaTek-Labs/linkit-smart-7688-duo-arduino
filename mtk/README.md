## LinkIt Smart 7688 (Arduino-Compatible)

This is a Arduino IDE board support package for LinkIt Smart 7688 (Arduino Compatible).

## ENVIRONMENT
This board support package works on Windows 7 and OS X with Arduino IDE 1.6.4+ installed.

## Installation
 - Unzip the zip archive `board_support.zip` to {ARDUINO_SKETCHBOOK_LOCATION}/hardware/...
 - If there is no `hardware` folder please create it manually
 - The resulting path should be like this: `{ARDUINO_SKETCHBOOK_LOCATION}/hardware/mtk/avr/boards.txt`
 - Restart Arduino IDE
 - Then a "LinkIt Smart 7688" option should appear under Arduino IDE's Board sub-menu

## COM port Driver
The hardware is a USB serial COM port.
 - Bootloader COM port: `VID=0x0E8D, PID=0xAB00`
 - Arduino Sketch COM port: `VID=0x0E8D, PID=0xAB01`

A Windows Serial COM port INF driver is located in: `{ARDUINO_SKETCHBOOK_LOCATION}/hardware/mtk/avr/driver/linkit_smart_7688.inf`