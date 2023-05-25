import network
import rp2
import socket
import time

from machine import Pin
led = Pin("LED", Pin.OUT)

ssid = 'Vodafone-42265784'
password = 'A5#ydn)&fYP>2IQ'

rp2.country('IT')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140)  # Disable power-saving mode
wlan.connect(ssid, password)

html = """<!DOCTYPE html>
<html>
  <head> <title>Pico W</title> </head>
  <body>
    <h1>Pico W</h1>
    <p>Hello World</p>
  </body>
</html>
"""

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
#    led.toggle()
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
#    led.on()
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print(f'Listening on {addr}')

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print(f'Client connected from {addr}')
        request = cl.recv(1024)
        print(request)

        request = str(request)
        led_on = request.find('/light/on')
        led_off = request.find('/light/off')
        print(f'LED on = {str(led_on)}')
        print(f'LED off = {str(led_off)}')

        if led_on == 6:
            print('LED on')
            led.value(1)
            stateis = 'LED is ON'

        if led_off == 6:
            print('LED off')
            led.value(0)
            stateis = 'LED is OFF'

#        response = html % stateis
        response = html
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    except OSError as e:
        cl.close()
        print('Connection closed')

