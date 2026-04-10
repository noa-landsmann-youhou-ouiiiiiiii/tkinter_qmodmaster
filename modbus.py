from tkinter import *
import main
from main import reponse,envoyer_donnees

vitesse_transmission = "9600"
port_usb = "COM20"

fenetre = Tk()

fenetre.title("Capteur modbus rs485")
fenetre.geometry("600x500")

titre = Label(fenetre, text="Interface IHM pour capteur modbus rs485",bg="yellow",pady=20)
titre.pack(fill="x")

frame_configuration = LabelFrame(fenetre, text="Configuration",pady=10, padx=10)
frame_configuration.pack(fill="x",padx=10,expand=True)

statut_alarme = Label(frame_configuration,height=2,width=5,bg="green",text="RAS")
statut_alarme.pack(side="left")

BAUDRATE_label = Label(frame_configuration, text="Vitesse de transmission : ", padx=10)
BAUDRATE_label.pack(side="left")

BAUDRATE = Entry(frame_configuration,width=10)
BAUDRATE.insert(0,vitesse_transmission)
BAUDRATE.pack(side="left")

port_label = Label(frame_configuration,text="Port : ",padx=20)
port_label.pack(side="left")

port = Entry(frame_configuration,width=10)
port.insert(0,port_usb)
port.pack(side="left")

frame_requete_modbus = LabelFrame(fenetre, text="Requête Modbus", pady=10, padx=10)
frame_requete_modbus.pack(fill="x", padx=10,expand=True)

requete_label = Label(frame_requete_modbus, text="Requête", padx=20)
requete_label.pack(side="left")

requete = Entry(frame_requete_modbus, width=50)
requete.pack(side="left")

Envoyer = Button(frame_requete_modbus, text="Envoyer", command=envoyer_donnees)
Envoyer.pack(side="right")

frame_reponse_modbus = LabelFrame(fenetre, text="Données reçues", pady=10, padx=10)
frame_reponse_modbus.pack(fill="x", padx=10,expand=True)

reponse_label = Label(frame_reponse_modbus, text=capteur_scada.reponse, padx=20)
reponse_label.pack(side="left")

fenetre.mainloop()