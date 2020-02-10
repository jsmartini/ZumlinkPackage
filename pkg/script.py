from serial import Serial
import time
freq = 3000000


def terminal(device: Serial):
    while 1:
        req= input(">>>")
        if "exit()".upper() in req:
            return
        req = req.encode()
        device.write(req + b'\r\n')
        output = b''
        time.sleep(0.5)  # set at half second, if device doesnt res increment
        while device.inWaiting() > 0:
            output = device.read(1)
            if output != '':
                print(output.decode(), end='')

def transmitstr(device: Serial, msg: str):
    return device.write(msg.encode())

def listen(device):
    while 1:
        output = device.inWaiting()
        print(device.read(output).decode())



if __name__ == "__main__":

    device = Serial("COM11")
    device.baud = 115200
    terminal(device)    
    #device.baud = 3000000
    #print(device.write(b'0'))

