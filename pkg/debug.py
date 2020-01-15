import serial
import time
from enum import Enum

class mode(Enum):
    GATEWAY = "GATEWAY"
    ENDPOINT = "endpoint"
    TERM = "term"

class Debug(serial.Serial):

    def __init__(self,device: str, mode = mode.TERM, baud = 9600, bytesize = serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE):
        self.mode = mode
        try:
            super().__init__(
                port = device,
                baudrate=baud,
                bytesize=bytesize,
                stopbits=stopbits
            )
        except serial.SerialException("WELL SHIT"):
            exit(-1)

    def debug(self):
        #debug terminal to set env variables
        assert mode == mode.TERM
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
        #baud is probably > 115200; transmit mode
        assert mode == mode.GATEWAY
        try:
            super().write(data.encode())
        except serial.SerialException("Well shit"):
            print("Transmit Failed")

    def recv(self):
        #baud is probably > 115200; recv mode
        assert mode == mode.ENDPOINT
        while 1:
            print(super().readline().decode())

