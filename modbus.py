import serial
import time


def envoyer_donnees(port, vitesse_transmission, requete):
    ser = serial.Serial(port, int(vitesse_transmission), timeout=1)
    ser.write(requete)
    time.sleep(0.1)
    reponse = ser.read(15)
    print(reponse.hex())
    ser.close()
    return reponse.hex()