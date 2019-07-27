from django.http import HttpResponse
from .models import PolycomIpPhone, On_Off_hook, Call_details
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging 
#import sys
import requests
import xml.etree.ElementTree as et
import time
from datetime import datetime
import dateutil.parser


event = []
ip_phone_info = {}
poly_ip = {}
event2 = []
layer_info = {}
call_info = {}

call_i = Call_details()
c_info = PolycomIpPhone()
ofstatus = On_Off_hook()

class BasicHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])    
        self.post_data = self.rfile.read(content_length)



        def get_data(self):    
            tree = et.fromstring(self.post_data)
            root = tree.getchildren()

            def get_phone_info(request):
                for child in root:
                    for child2 in child.getchildren():
                        #print(child.tag , child2.tag, child2.text)
                        event.append(child.tag)
                        ip_phone_info.update({child2.tag : child2.text})
                        poly_ip = zip(event, ip_phone_info.items())
                        #d = {event: ip_phone_info for stamp, (key, value) in zip(event, ip_phone_info)}
                        for stamp , (key, value) in poly_ip:
                            if stamp == 'CallStateChangeEvent':
                                if key == 'PhoneIP':
                                    c_info.phone_ip = value
                                    c_info.save()
                                    call_i.phone_ip = value
                                    call_i.save()
                                if key == 'MACAddress':
                                    c_info.mac_address = value
                                    c_info.save()
                                    call_i.mac_address = value
                                    call_i.save()
                                if key == 'TimeStamp':
                                    value = value[0:19]
                                    c_info.time_stamp = value
                                    c_info.save()
                                    call_i.time_stamp = value
                                    call_i.save()
                            if stamp == 'OnHookEvent':
                                #print(stamp)
                                ofstatus.status = stamp
                                ofstatus.save()
                                if key == 'PhoneIP':
                                    #print('IP:', value)
                                    ofstatus.phone_ip = value
                                    ofstatus.save()
                                if key == 'MACAdress':
                                    #print('Add:', value)
                                    ofstatus.mac_address = value
                                    ofstatus.save()
                                if key == 'TimeStamp':
                                    value = value[0:19]
                                    ofstatus.time_stamp = value
                                    ofstatus.save()
                                if key == 'Linenumber':
                                    #print('Linenum:', value)
                                    ofstatus.line_num = value
                                    ofstatus.save()
                            if stamp == 'OffHookEvent':
                                #print(stamp)
                                ofstatus.status = stamp
                                ofstatus.save()
                                if key == 'PhoneIP':
                                    #print('IP:', value)
                                    ofstatus.phone_ip = value
                                    ofstatus.save()
                                if key == 'MACAdress':
                                    #print('Add:', value)
                                    ofstatus.mac_address = value
                                    ofstatus.save()
                                if key == 'TimeStamp':
                                    value = value[0:19]
                                    ofstatus.time_stamp = value
                                    ofstatus.save()
                                if key == 'Linenumber':
                                    #print('Linenum:', value)
                                    ofstatus.line_num = value
                                    ofstatus.save() 
                        

                            #print (stamp, ':', '{', key, ':', value, '}')
                        
                        for child3 in child2.getchildren():
                            for child4 in child3.getchildren():
                                event2.append(child3.tag)
                                layer_info.update({child4.tag : child4.text})
                                call_info = zip(event2, layer_info.items())
                               
                                for stamp , (key, value) in call_info:
                                    #print (stamp, ':', '{', key, ':', value, '}')
                                    if key == 'CallReference':
                                        call_i.call_reference = value
                                        call_i.save()
                                    if key == 'CallState':
                                        call_i.call_state = value
                                        call_i.save()
                                    if key == 'CallType':
                                        call_i.call_type = value
                                        call_i.save()
                                    if key == 'UIAppearanceIndex':
                                        call_i.call_type = value
                                        call_i.save()
                                    if key == 'CalledPartyName':
                                        call_i.called_party_name = value
                                        call_i.save()
                                    if key == 'CalledPartyDirNum':
                                        call_i.called_party_dir_num = value
                                        call_i.save()
                                    if key == 'CallingPartyName':
                                        call_i.calling_party_name = value
                                        call_i.save()
                                    if key == 'CallingPartyDirNum':
                                        call_i.calling_party_dir_num = value
                                        call_i.save()
                                    if key == 'CallDuration':
                                        call_i.call_duration = value
                                        call_i.save()
                                    if key == 'Protocol':
                                        call_i.protocol = value
                                        call_i.save()
                                    if key == 'Muted':
                                        call_i.muted = value
                                        call_i.save()
                                    if key == 'Ringing':
                                        call_i.ringing = value
                                        call_i.save()

            def dele(self):
                Call_details.objects.filter(called_party_name = None).delete()
                PolycomIpPhone.objects.filter(phone_ip = None).delete()

            get_phone_info(self) 
            dele(self)

        get_data(self)

def run(server_class = HTTPServer, handler_class = BasicHandler, port = 8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting")
    try:
        httpd.serve_forever()
        #time.sleep(30)
    except KeyboardInterrupt:
        pass
    httpd.server_close()

class IndexView(generic.ListView):
    template_name = 'pull/page.html'
    context_object_name = 'latest_Call_details_list'
    def get_queryset(request):
        return Call_details.objects.all().order_by('-id')[:]
        """ 
        ''' items = Call_details.objects.all()
        for items in items.values('calling_party_name'):
            if items['calling_party_name'] == 'Gaurav Bhagwat'or 'Kent Iverson':
                return Call_details.objects.filter(calling_party_name__startswith='Gaurav Bhagwat').values().order_by('-id')[:5]
            if items['calling_party_name'] == 'Kent Iverson':
                return Call_details.objects.filter(calling_party_name__startswith='Kent Iverson').values().order_by('-id')[:5]
 ''' """
        #return Call_details.objects.all().order_by('-calling_party_name')[:10]

#run()


 