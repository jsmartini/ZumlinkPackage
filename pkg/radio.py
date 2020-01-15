import serial
import time
import enum

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

