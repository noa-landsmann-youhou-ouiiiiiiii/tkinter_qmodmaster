from tkinter import *
import serial
from modbus import envoyer_donnees
vitesse_transmission = "9600"
port = "COM16"
requete_modbus = bytes([0x01,0x03,0x00,0x00, 0x00, 0x05, 0x85, 0xC9])


def envoyer_requete():
    global port
    global vitesse_transmission
    global requete_modbus
    global reponse_modbus
    try:
        reponse_modbus = envoyer_donnees(port, vitesse_transmission, requete_modbus)
        trame_reponse_label.config(text=reponse_modbus)
        message_label.config(text="Trame envoyée avec succès",bg="beige")
        if reponse_modbus[4] == 0x00:
            statut_alarme.config(bg="green",text="RAS")
        if reponse_modbus[4] == 0x01:
           statut_alarme.config(bg="yellow",text="Alarme")
        if reponse_modbus[4] == 0x02:
            statut_alarme.config(bg="red",text="CRITIQUE")
    except serial.serialutil.SerialException:
        message_label.config(text="Erreur : capteur modbus non connecté")

fenetre = Tk()

fenetre.title("Interface IHM pour capteur modbus RS485")
fenetre.geometry("600x500")

#**************************************MESSAGE UTILISATEUR*************************************

frame_message = LabelFrame(fenetre, borderwidth=5, relief="sunken",padx=5, pady=5,text="Avertissements utilisateur",bg="beige")
frame_message.pack(expand=True,fill="x",padx=5,pady=5)

statut_alarme = Label(frame_message,height="2",width="5",bg="green",text="RAS")
statut_alarme.pack(side="left")

message_label = Label(frame_message, text="Message : ", padx=10,bg="beige")
message_label.pack(side="left")

#*************************CONFIGURATION************************************************
frame_configuration = LabelFrame(fenetre, text="Configuration",pady=10, padx=10, borderwidth=5, relief="sunken")
frame_configuration.pack(fill="x",padx=10,expand=True)

BAUDRATE_label = Label(frame_configuration, text="Vitesse de transmission : ", padx=10)
BAUDRATE_label.pack(side="left")

BAUDRATE = Entry(frame_configuration,width=10)
BAUDRATE.insert(0,vitesse_transmission)
BAUDRATE.pack(side="left")

port_label = Label(frame_configuration,text="Port : ",padx=20)
port_label.pack(side="left")

port_entry = Entry(frame_configuration,width=10)
port_entry.insert(0,port)
port_entry.pack(side="left")

#*************************REQUETE MODBUS************************************************

frame_requete = LabelFrame(fenetre, text="Requête Modbus", pady=10, padx=10, borderwidth=5, relief="sunken")
frame_requete.pack(fill="x", padx=10,expand=True)

requete_label = Label(frame_requete, text="Requête", padx=20)
requete_label.pack(side="left")

requete = Entry(frame_requete, width=50)
requete.pack(side="left")
requete.insert(0,requete_modbus.hex())

Envoyer = Button(frame_requete, text="Envoyer", command=envoyer_requete)
Envoyer.pack(side="right")

#*************************REPONSE MODBUS************************************************

frame_reponse_modbus = LabelFrame(fenetre, text="Données reçues", pady=10, padx=10, borderwidth=5, relief="sunken")
frame_reponse_modbus.pack(fill="x", padx=10,expand=True)

reponse_label = Label(frame_reponse_modbus, text="Réponse : ", padx=20)
reponse_label.pack(side="left")


trame_reponse_label = Label(frame_reponse_modbus, text="trame", padx=20)
trame_reponse_label.pack(side="left")

'''sous_frame_temperature = LabelFrame(frame_reponse_modbus, text="Temperature", padx=10)
sous_frame_temperature.pack()

sous_frame_humidite = LabelFrame(frame_reponse_modbus, text="Humidite", padx=10)
sous_frame_humidite.pack()

sous_frame_pression = LabelFrame(frame_reponse_modbus, text="Pressure", padx=10)
sous_frame_pression.pack()

sous_frame_temperature_label = Label(sous_frame_temperature, text="temperature", padx=20)
sous_frame_temperature_label.pack()

sous_frame_humidite_label = Label(sous_frame_humidite, text="humidity", padx=20)
sous_frame_humidite_label.pack()

sous_frame_pression_label = Label(sous_frame_pression, text="pressure", padx=20)
sous_frame_pression_label.pack()'''

fenetre.mainloop()