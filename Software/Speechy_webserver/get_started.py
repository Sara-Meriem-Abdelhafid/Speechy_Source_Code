import network 
import ubinascii
import socket
from time import sleep
#from picozero import pico_temp_sensor, pico_led
from machine import Pin


wlan = network.WLAN(network.STA_IF)# wirless lan network as a station STA_IF ,,,, AP_IF if we want it to be the acess point
wlan.active(True)

#print(wlan.scan()) #to see all ap adresses 
#mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode() #to print my devise mac adress 
#print('\n\n MAC', mac) 

ssid = 'MyNetwork'
password = 'abdelhafid2023A@abd'
wlan.connect(ssid, password)

led_one = Pin(14, Pin.OUT)
led_two = Pin(15, Pin.OUT)

def Website():
    value_one = led_one.value()
    value_two = led_two.value()
    website = """<!DOCTYPE html>
    <html>
        <head> <title>Raspberry Pico W WebServer</title> </head>
        <body>
            <h1>Raspberry Pico W WebServer</h1>
            
            <table style="width:400px" class="center">
                  <tr>
                    <th><center>LED Number </center></th>
                    <th><center>Button </center> </th>
                    <th><center>Pin State</center> </th>
                  </tr>
                  <tr>
                    <td><center>one </td>
                    <td><center><input type='button' value='toggle' onclick='toggleLed("one")'/> </center></td>
                    <td> <center>  <span id="value_one">""" + str(value_one) + """</span></center> </td>
                  </tr>
                  <tr>
                    <td><center>two</center> </td>
                    <td><center><input type='button' value='toggle' onclick='toggleLed("two")'/></center></td>
                    <td><center>  <span id="value_two">""" + str(value_two) + """</span></center></td>
                   </tr>
            </table>
            
            <input type='button' value='update' onclick='update()'/>
                        
            <script>
                function toggleLed(led){
                    var xhttp = new XMLHttpRequest();
                    xhttp.open('GET', '/led/'+led, true);
                    xhttp.send();
                }
                function update(){
                    location.reload(true);
                }
                    
            </script>
        </body>
    </html>
    """
    return website
    
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
    
max_wait = 10
print('Waiting for connection')
while max_wait > 10:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1    
    sleep(1)
status = None
if wlan.status() != 3:
    raise RuntimeError('Connections failed')
else:
    status = wlan.ifconfig()
    print('connection to', ssid,'succesfull established!', sep=' ')
    print('IP-adress: ' + status[0])
ipAddress = status[0]
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
while True:
    try:
        cl, addr = s.accept()
        print('Connection from ', addr, "accepted!")
        request = cl.recv(1024)
        request = str(request)      

        if request.find('/led/one') == 6:
            led_one.toggle()
            
        if request.find('/led/two') == 6:
            led_two.toggle()
             
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(Website())
        cl.close()
    except OSError as e:
        cl.close()
        print('connection closed')