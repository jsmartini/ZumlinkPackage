from serial import Serial

class Zumlink:

    def __init__(self, device, baud, dump_file="data.recv"):
        self.zumlink = Serial(device)
        self.zumlink.baud = baud
        self.data = open(dump_file, 'w')

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
            while self.zumlink.inWaiting() >0:
                output = self.zumlink.read(1)
                if output != '':
                    print(output.decode(), end='')
            
    def transmitBulkFile(self):
        pass

    def transmitBSON(self):
        pass


        

