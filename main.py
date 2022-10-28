import numbers
import phonenumbers
import os
from pystyle import Colors, Colorate, Write, Box
from phonenumbers import geocoder
from phonenumbers import carrier


langue = "fr"

# check langue if en or fr
if langue == "en":
    os.system("cls")
    print(Box.Lines("Welcome to the phone number checker"))
    print(Colors.blue + "Please enter the phone number you want to check")
    print(Colors.white + "Example: +33612345678")
    number = input("Number: ")

    os.system("cls")
    print(Box.Lines("Results"))
    ch_number = phonenumbers.parse(number, "CH")
    service_number = phonenumbers.parse(number, "RO")
    #print(geocoder.description_for_number(ch_number, "en"))
    print(Box.DoubleCube(geocoder.description_for_number(ch_number, "en") + "\n" + carrier.name_for_number(service_number, "en")))
    service_number = phonenumbers.parse(number, "RO")


elif langue == "fr":
    
    os.system("cls")
    print(Box.Lines("Bienvenue dans le vérificateur de numéro de téléphone"))
    print(Colors.blue + "Veuillez entrer le numéro de téléphone que vous souhaitez vérifier")
    print(Colors.white + "Exemple: +33612345678")
    number = input("Numéro: ")
    
    os.system("cls")
    print(Box.Lines("Results"))
    ch_number = phonenumbers.parse(number, "CH")
    service_number = phonenumbers.parse(number, "RO")
    #print(geocoder.description_for_number(ch_number, "en"))
    print(Box.DoubleCube(geocoder.description_for_number(ch_number, "en") + "\n" + carrier.name_for_number(service_number, "en")))
    service_number = phonenumbers.parse(number, "RO")

else:
    print("Error: Language not found")


