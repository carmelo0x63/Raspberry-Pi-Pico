### Install
```
$ mkdir Raspberry-Pico && cd $_

$ python3 -m venv .

$ source bin/activate

$ python3 -m pip install --upgrade pip setuptools wheel
```

Additionally, let's install `rshell`:
```
$ python3 -m pip install rshell
```
**NOTE**: `rshell` is a "remote shell for working with MicroPython boards".
Its home page is https://github.com/dhylands/rshell.

### Connect to Raspberry Pico (USB serial)
```
$ rshell -p /dev/ttyACM0 --buffer-size 512
Using buffer-size of 512
Connecting to /dev/ttyACM0 (buffer-size 512)...
Trying to connect to REPL  connected
Retrieving sysname ... rp2
Testing if ubinascii.unhexlify exists ... Y
Retrieving root directories ... /main.py/
Setting time ... *** 
Evaluating board_name ... pyboard
Retrieving time epoch ... Jan 01, 1970
Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
/home/<user>/Raspberry-Pico> 
```

A few commands are available:
```
/home/<user>/Raspberry-Pico> help
Documented commands (type help <topic>):
========================================
args    cat  connect  date  edit  filesize  help  mkdir  rm     shell
boards  cd   cp       echo  exit  filetype  ls    repl   rsync
```

`repl` is the command leading us to the MicroPython interpreter:
```
/home/<user>/Raspberry-Pico> repl
Entering REPL. Use Control-X to exit.
>
MicroPython v1.19.1 on 2022-06-18; Raspberry Pi Pico with RP2040
Type "help()" for more information.
```
**NOTE**: use `Control-X` to exit the REPL environment. The usual `Control-D will` soft reboot the board!

### Hello, world!
When tinkering with microcontrollers and IoThings "Hello, world!" is replaced by blinking an onboard LED. Let's try that:
```
from machine import Pin
led = Pin(25, Pin.OUT)
led.toggle()
```

One can go on forever clicking arrow UP, ENTER, arrow UP, ENTER...</br>
How do we properly program the board? `rshell` comes to rescue...
1. create a simple program:
```
from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

2. connect to the board with `rshell`

3. copy the script into the approproate position, also rename it to `main.py`

4. hard reset the board

