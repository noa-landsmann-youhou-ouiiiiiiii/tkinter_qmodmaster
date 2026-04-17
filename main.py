from tkinter import *
import serial
from modbus import envoyer_donnees
vitesse_transmission = "9600"
port = "COM8" #en haut à droite de b307-p06, à compléter
requete_modbus = bytes([0x01,0x03,0x00,0x00, 0x00, 0x05, 0x85, 0xC9])

#Définition des couleurs

bleu_fonce_style= '#' + '2f2869' #bleu foncé stylé
bleu_style= '#' + '4338a2' #bleu stylé
rouge= '#' + 'ff0000' #rouge
orange= '#' + 'ff6e00' #orange
bleu_cyan= '#' + '00ffff' #bleu cyan
vert= '#' + '00ff00' #vert

def envoyer_requete():
    global port
    global vitesse_transmission
    global requete_modbus
    global reponse_modbus
    try:
        reponse_modbus = envoyer_donnees(port, vitesse_transmission, requete_modbus)
        trame_reponse_label.config(text=reponse_modbus)
        message_label.config(text="Trame envoyée avec succès",bg=bleu_style)
        frame_message.config(bg=bleu_style)
        if reponse_modbus[4] == 0x00:
            statut_alarme.config(bg="green",text="RAS")
        if reponse_modbus[4] == 0x01:
           statut_alarme.config(bg="yellow",text="Alarme")
        if reponse_modbus[4] == 0x02:
            statut_alarme.config(bg="red",text="CRITIQUE")
    except serial.serialutil.SerialException:
        frame_message.config(bg="red")
        message_label.config(text="Erreur : capteur modbus non connecté",bg="red")
fenetre = Tk()

fenetre.title("Interface IHM pour capteur modbus RS485")
fenetre.geometry("600x500")
fenetre.config(bg=bleu_fonce_style)

label_titre = Label(fenetre, text="SURVEILLANCE ENVIRONNEMENTALE DE LA SALLE BLANCHE", bg=bleu_fonce_style, fg=bleu_cyan, font=("Arial", 15, "bold"), wraplength=550)
label_titre.pack(side='top', fill='x',expand=True,pady=30)

#**************************************MESSAGE UTILISATEUR*************************************

frame_message = LabelFrame(fenetre, borderwidth=5, relief="sunken",padx=5, pady=5,text="Avertissements utilisateur",bg=bleu_style)
frame_message.pack(expand=True,fill="x",padx=5,pady=5)

statut_alarme = Label(frame_message,height="2",width="5",bg="green",text="RAS")
statut_alarme.pack(side="left")

message_label = Label(frame_message, text="Message : ", padx=10,bg=bleu_style)
message_label.pack(side="left")

#*************************CONFIGURATION************************************************
frame_configuration = LabelFrame(fenetre, text="Configuration",pady=10, padx=10, borderwidth=5, relief="sunken",bg=bleu_style)
frame_configuration.pack(fill="x",padx=10,expand=True)

BAUDRATE_label = Label(frame_configuration, text="Vitesse de transmission : ", padx=10,bg=bleu_style)
BAUDRATE_label.pack(side="left")

BAUDRATE = Entry(frame_configuration,width=10)
BAUDRATE.insert(0,vitesse_transmission)
BAUDRATE.pack(side="left")

port_label = Label(frame_configuration,text="Port : ",padx=20,bg=bleu_style)
port_label.pack(side="left")

port_entry = Entry(frame_configuration,width=10)
port_entry.insert(0,port)
port_entry.pack(side="left")

#*************************REQUETE MODBUS************************************************

frame_requete = LabelFrame(fenetre, text="Requête Modbus", pady=10, padx=10, borderwidth=5, relief="sunken",bg=bleu_style)
frame_requete.pack(fill="x", padx=10,expand=True)

requete_label = Label(frame_requete, text="Requête", padx=20,bg=bleu_style)
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