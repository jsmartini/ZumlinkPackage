import serial
import time
from enum import Enum

class mode(Enum):

    def __init__(self):
        pass

    GATEWAY = "GATEWAY"
    ENDPOINT = "ENDPOINT"
    TERM = "TERM"

class Debug(serial.Serial):

    def __init__(self):
        pass

    def __init__(self,device: str, mode = mode.TERM, baud = 9600, bytesize = serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE):
        self.mode = mode
        try:
            super().__init__(
                port = device,
                baudrate=baud,
                bytesize=bytesize,
                stopbits=stopbits
            )
        except serial.SerialException("Device Not Configured, Dying"):
            exit(-1)

    def debug(self):
        #debug terminal to set env variables
        assert mode == mode.TERM
        assert super().isOpen() == True
        while 1:
            req = input("term>>>")
            if req == "exit()":
                break
            req = req.encode()
            super().write(req + b'\r\n')
            output = b''
            time.sleep(0.5)  # set at half second, if device doesnt res increment
            while super().inWaiting() > 0:
                output = super().read(1)
                if output != '':
                    print(output.decode(), end='')

    def transmit(self, data:str):
        assert super().isOpen() == True
        #baud is probably > 115200; transmit mode
        assert mode == mode.GATEWAY
        try:
            super().write(data.encode())
        except serial.SerialException("Well shit"):
            print("Transmit Failed")

    def transmitEchoTerminal(self):
        assert super().isOpen() == True
        while 1:
            req = input("echo>>>")
            if req == "exit()":
                break
            super().write(req.encode() + b'/r/n')

    def recv(self):
        assert super().isOpen() == True
        #baud is probably > 115200; recv mode
        assert mode == mode.ENDPOINT
        while 1:
            print(super().readline().decode())

