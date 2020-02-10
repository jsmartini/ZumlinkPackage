from serial import Serial
from bson import BSON


class Zumlink:
    # common frequencies
    terminal9600 = 9600
    terminal112500 = 112500
    broadcast = 3000000 #default across all radios for ARA

    def __init__(self, device, baud, dump_file="data.recv"):
        self.zumlink = Serial(device)
        self.zumlink.baud = baud
        self.data = open(dump_file, 'w')

    def __init__(self, device, baud=0, dump_file="data.recv", transmit=True):
        self.zumlink = Serial(device)
        if transmit:
            self.zumlink.baud = self.broadcast
        elif baud == 0:
            self.zumlink.baud = self.terminal9600
        else:
            self.zumlink.baud = baud

    def __del__(self):
        self.data.close()
        self.zumlink.__del__()

    def transmitText(self, msg: str):
        bytes_transmitted = self.zumlink.write(msg.encode())
        return bytes_transmitted

    def listen(self):
        while True:
            recv = self.zumlink.readline()
            self.data.write(recv.decode())

    def debugTerminal(self):
        while True:
            req = input("DEBUG>>>")
            if "EXIT()".upper() in req.upper():
                return
            req.encode()
            self.zumlink.write(req)
            while self.zumlink.inWaiting() > 0:
                output = self.zumlink.read(1)
                if output != '':
                    print(output.decode(), end='')

    def transmitBulkFile(self, path: str):
        try:
            binary = open(path, 'rb').read()
        except FileNotFoundError:
            print("file not found")
            return
        return self.zumlink.write(binary)

    def transmitBSON(self, data: dict):
        data_BSON = BSON.encode(data)
        return self.zumlink.write(data_BSON)