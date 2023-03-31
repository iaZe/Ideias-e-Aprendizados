import pywhatkit as whatsapp
import datetime

phone_number = input("Enter the phone number: ")

message = input("Enter the message: ")

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute + 1

whatsapp.sendwhatmsg(phone_number, message, hour, minute)