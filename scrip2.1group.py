import pywhatkit

try:
    pywhatkit.sendwhatmsg_to_group_instantly("HMSd7sLfFPy4ivP0YtAqvE", "No", 19, 9)
    print("Mensaje enviado")
except:
    print("Error")