import serial
import time
from ihm import *

def envoyer_donnees():
    PORT = port_usb

    requete = bytes([0x01,0x03,0x00,0x00, 0x00, 0x05, 0x85, 0xC9])

    ser = serial.Serial(PORT, int(vitesse_transmission), timeout=1)

    ser.write(requete)

    time.sleep(0.1)

    reponse = ser.read(15)

    print(reponse)

    ser.close()

    return reponse