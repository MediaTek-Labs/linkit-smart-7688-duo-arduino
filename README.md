## Arduino Supporting Package for LinkIt Smart 7688 Duo

There is a Arduino IDE board support package for LinkIt Smart 7688 (Arduino Compatible). This allows you to program the ATMega32U4 with Arduino IDE.

## ENVIRONMENT
The board support package works with Arduino IDE 1.6.4.

## Installation via Zip Package
 - Unzip the zip archive `board_support.zip` to `{ARDUINO_SKETCHBOOK_LOCATION}/hardware/...
 - If there is no `hardware` folder please create it manually
 - The resulting path should be like this: `{ARDUINO_SKETCHBOOK_LOCATION}/hardware/mtk/avr/boards.txt`
 - Restart Arduino IDE
 - Then a "LinkIt Smart 7688 Duo" option should appear under Arduino IDE's Board sub-menu

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

## Using LinkIt Smart 7688 Duo as an ATMega32U4 Boot Loader Programmer

Sometimes you need to re-program the boot loader of the ATMega32U4 on LinkIt Smart 7688 Duo. You can use LinkIt Smart 7688 Duo as a ATMega boot loader programmer to program the bootloader of the ATMega32U4 on another LinkIt Smart 7688 Duo.

To do this, suppose we have 2 LinkIt Smart 7688 Duo boards. The first board _A_ act as the programmer to program the second board _B_.

1. Select `Tools > Board > LinkIt Smart 7688 Duo`
2. Open sketch `Example > ArduinoISP` 
3. Modify the line `#define RESET     SS` to `#define RESET     10`
4. Upload the modified sketch to board _A_
5. Connect pin `S0`, `S1`, `S2`, `GND` of board _A_ to the same pin of board _B_
6. Connect pin `D10` of board _A_ to pin `RST` of board _B_
7. Select `Tools > Programmer > LinkIt Smart 7688 Duo as ISP`
8. Select `Tools > Burn Bootloader`


(This one is still verifying)
1. Upload sketch `Example > ArduinoISP` to board _A_
2. Connect pin `S0`, `S1`, `S2`, `GND` of board _A_ to the same pin of board _B_
3. Connect pin `S3` of board _A_ to pin `RST` of board _B_
4. Select `Tools > Programmer > LinkIt Smart 7688 Duo as ISP`
5. Select `Tools > Burn Bootloader`