import requests
import base64
import cPickle
import time
import ConfigParser
import os

config = ConfigParser.RawConfigParser()
filename = os.path.abspath("hermes.ini")
config.read(filename)

localcallsign = config.get('UNIT1', 'CALLSIGN')
localnodeid = int(config.get('UNIT1', 'NODEID'))
destinationcallsign = config.get('UNIT0', 'CALLSIGN')
destinationnodeid = int(config.get('UNIT0', 'NODEID'))

def main():
    """
    Main function of the transmit example of Hermes messaging application using Flask. This function loops continously
    getting user input text to transmit to the Flask server for wireless transmission to the intended remote device.
    """
    while 1:
        message = raw_input("Enter Message: ")
        payload = {'localcallsign': localcallsign, 'localnodeid': localnodeid, 'destinationcallsign': destinationcallsign, 'destinationnodeid': destinationnodeid, 'data': message}
        txdata = requests.post('http://127.0.0.1:8005/', params=payload)

if __name__ == '__main__':
    main()



