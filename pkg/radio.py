import serial
import time
from pkg.debug import mode

#rewritten from https://github.com/jsmartini/Cubesat-Telemetry/blob/master/test.py

def generate_config(radioMode = "Endpoint", rfDataRate = "RATE_1M", txPower=10, networkId = 77777, frequencyKey=0, radioFrequency=915.0000, radioHoppingMode="Hopping_On", beaconInterval="ONE_HUNDRED_MS", beaconBurstCount=1, lnaBypass=0, maxLinkDistanceInMiles=5, maxPacketSize=900, cliBaudRate=115200, packetizedBaudRate=3000000, passthruBaudRate = 3000000, databits=8, parity="None", stopbits=1, flowControl="Hardware", passthruLatencyMode="auto", passthruLatencyTimer=16):
    return {
        "radioSettings":[
            "radioMode={0}".format(radioMode),
            "rfDataRate={0}".format(rfDataRate),
            "txPower={0}".format(txPower),
            "networkId={0}".format(networkId),
            "frequencyKey={0}".format(frequencyKey),
            "radioFrequency={0}".format(radioFrequency),
            "radioHoppingMode={0}".format(radioFrequency),
            "beaconInterval={0}".format(beaconInterval),
            "beaconBurstCount={0}".format(beaconBurstCount),
            "lnaBypass={0}".format(lnaBypass),
            "maxLinkDistanceInMiles={0}".format(maxLinkDistanceInMiles),
            "maxPacketSize={0}".format(maxPacketSize),
            "frequencyMasks="
        ],
        "serialPortConfig":[
            "cliBaudRate={0}".format(cliBaudRate),
            "packetizedBaudRate={0}".format(packetizedBaudRate),
            "passthruBaudRate={0}".format(passthruBaudRate),
            "databits={0}".format(databits),
            "parity={0}".format(parity),
            "stopbits={0}".format(stopbits),
            "flowControl={0}".format(flowControl),
            "passthruLatencyMode={0}".format(passthruLatencyMode),
            "passthruLatencyTimer={0}".format(passthruLatencyTimer)
        ]
    }


class Zumlink(serial.Serial):

    def __init(self):
        pass

    def __init__(self, device: str, baudrate=9600, mode=mode.TERM, configuration = generate_config(txPower=0)):
        # True -> baud: 30000000 (I think the actual radio socket)
        # False -> baud:9600 Terminal
        self.mode = mode
        try:
            super().__init__(
                port=device,
                baudrate=baudrate,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS
            )
        except serial.SerialException("Not Configured, Dying"):
            exit(-1)

        if self.mode == mode.TERM:
            self.setup(settings=configuration)
        # making sure connection is open
        assert super().isOpen() == True
        print("{0} Connection opened".format(device))
        time.sleep(1)

    def command(self, c: str) -> str:
        assert super().isOpen() == True
        assert self.mode == mode.TERM
        # test function
        super().write(c.encode() + b"\r\n")
        output = b''
        time.sleep(0.5)
        while super().inWaiting() > 0:
            output += super().read(1)
        return output.decode()

    def terminal(self):
        assert mode == mode.TERM
        assert super().isOpen() == True
        while True:
            req = input(">>>")
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

    def transmit(self, dataFile: str) -> None:
        assert super().isOpen() == True
        assert mode == mode.GATEWAY
        # writes data to the serial port device
        # to be tested
        super().write(open(dataFile, "rb").read())

    def listen(self) -> str:
        assert super().isOpen() == True
        assert mode == mode.ENDPOINT
        # to be tested
        # reads data from the serial port device
        return super().readline().decode("utf-8")

    def setup(self, settings):
        assert super().isOpen() == True
        assert mode == mode.TERM
        for radioSetting in settings["radioSettings"]:
            self.command("radioSettings." + radioSetting)
        #Serial settings should not change, but uncomment if needed
        for serialSetting in settings["serialSettings"]:
            self.command("serialPortConfig." + serialSetting)
        self.command("save")

