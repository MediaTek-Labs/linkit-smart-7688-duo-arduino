Notes on building LinkIt Smart 7688 Duo ATMega32u4 Caterina bootloader:

1. Must download LUFA-111009(http://www.github.com/abcminiuser/lufa/archive/LUFA-111009.zip) and extract to the same-named directory. Alternatively, if you pulled this repository with git, do a `git submodule update --init` to pull from its repository.

2. You need avr toolchain (Win-AVR / avr-gcc) to build this bootloader.

3. The "build.txt" file and "program.txt" files can be renamed
    to .bat files and run to build and program the boards listed
    herein (Windows only, unfortunately).

Notes on this bootloader:

This booloader is modified from SparkFun Arduino boards. https://github.com/sparkfun/Arduino_Boards.git