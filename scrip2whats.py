import pywhatkit

try:
    pywhatkit.sendwhatmsg("+524445808274", "No", 9, 12)
    print("Mensaje enviado")
except:
    print("Error")