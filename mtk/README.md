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

## Using LinkIt Smart 7688 Duo as a Boot Loader Programmer

You can use LinkIt Smart 7688 Duo as a boot loader programmer to program the bootloader of another LinkIt Smart 7688 Duo.

To do this, suppose we have 2 LinkIt Smart 7688 Duo boards. The first board _A_ act as the programmer to program the second board _B_.

1. Open sketch `Example > ArduinoISP` 
2. Modify the line `#define RESET     SS` to `#define RESET     10`
3. Upload the modified sketch to board _A_
4. Connect pin `S0`, `S1`, `S2`, `GND` of board _A_ to the same pin of board _B_
5. Connect pin `10` of board _A_ to pin `RST` of board _B_
6. Select `Tools > Programmer > LinkIt Smart 7688 as ISP`
7. Select `Tools > Burn Bootloader`


(This one is still verifying)
1. Upload sketch `Example > ArduinoISP` to board _A_
2. Connect pin `S0`, `S1`, `S2`, `GND` of board _A_ to the same pin of board _B_
3. Connect pin `S3` of board _A_ to pin `RST` of board _B_
4. Select `Tools > Programmer > LinkIt Smart 7688 as ISP`
5. Select `Tools > Burn Bootloader`