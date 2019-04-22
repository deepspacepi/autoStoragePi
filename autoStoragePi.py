
import os
import json
import urllib.parse as urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer


global var

if (os.path.isfile('config.json')):
    # Αν το αρχείο ρυθμίσεων υπάρχει, γίνεται ανάγνωση των τιμών των μεταβλητών
    with open('config.json') as jsonFile:
        var = json.load(jsonFile)
        print (var)
        # print('SpeedLR: ', var['SpeedLR'])
        # print('SpeedUp: ', var['SpeedUp'])
        # print('SpeedDown: ', var['SpeedDown'])
        # print('SpeedFB: ', var['SpeedFB'])
else:
    # Αν το αρχείο ρυθμίσεων δεν υπάρχει, γίνεται αποθήκευση εξ ορισμού τιμών για τις μεταβλητές
    var = {'SpeedLR' : 0.8, 'SpeedUp' : 0.8, 'SpeedDown' : -0.4, 'SpeedFB' : 0.4}
    with open('config.json', 'w') as jsonFile:
        json.dump(var, jsonFile)


request = None

# Συνάρτηση διαχείρισης HTTP request
class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global request
    global var

    # Προετοιμασία και αποστολή απάντησης
    messagetosend = bytes('Hello from Raspberry Pi!',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)

    # Ανάγνωση HTTP request μέσω της URL
    request = self.requestline
    # print(request)
    request = request[5 : int(len(request)-9)]
    parsed = urlparse.urlparse(request)
    print(urlparse.parse_qs(parsed.query))

    # Έλεγχος της παραμέτρου μέσω URL και εκτέλεση των κατάλληλων  ενεργειών
    if request == 'Left':
        print("Left")
    elif request == 'Right':
        print("Right")
    elif request == 'Up':
        print("Up")
    elif request == 'Down':
        print("Down")
    elif request == 'Play':
        print("Play")
    elif request == 'Stop':
        print("Stop")
    elif request == 'Open':
        print("Open")
    elif request == 'Close':
        print("Close")
    elif request == 'Manual':
        print("Manual")
    elif request == 'Automatic':
        print("Automatic")
    elif "SpeedLR" in urlparse.parse_qs(parsed.query):
        var['SpeedLR'] = float(urlparse.parse_qs(parsed.query)["SpeedLR"][0])
        print("SpeedLR")
    elif "SpeedUp" in urlparse.parse_qs(parsed.query):
        var['SpeedUp'] = float(urlparse.parse_qs(parsed.query)["SpeedUp"][0])
        print("SpeedUp")
    elif "SpeedDown" in urlparse.parse_qs(parsed.query):
        var['SpeedDown'] = float(urlparse.parse_qs(parsed.query)["SpeedDown"][0])
        print("SpeedDown")
    elif "SpeedFB" in urlparse.parse_qs(parsed.query):
        var['SpeedFB'] = float(urlparse.parse_qs(parsed.query)["SpeedFB"][0])
        print("SpeedFB")
    elif "ServerIP" in urlparse.parse_qs(parsed.query):
        var['ServerIP'] = float(urlparse.parse_qs(parsed.query)["ServerIP"][0])
        print("ServerIP")
    elif "Save" in urlparse.parse_qs(parsed.query):
        print("Save")
        with open('var.json', 'w') as jsonFile:
            json.dump(var, jsonFile)
    return



server_address_httpd = ('192.168.1.22',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting Server:')
httpd.serve_forever()
