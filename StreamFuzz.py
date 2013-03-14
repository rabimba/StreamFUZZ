#imports
import socket
import time
import sys
from ConfigParser import ConfigParser
from itertools import islice, product, chain
import string

END = '\r\n'


def go(data):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((RHOST,RPORT))
	except socket.error, (value,message):
		if s:
			s.close()
		print "Could not open socket: " + message
		sys.exit(1)

	s.send(data)
	file = open('LOG.TXT','a')
	file.write(data)
	file.close()
	rcv = s.recv(1024)
	s.close()

#Functions to Craft Patterns Starts Here
def craft0(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Basic crafting 0)"
	buff = ''
	buff += focus                     #OPTIONS AAAAAAAAAAAAAAAAA\r\n
	buff += ''
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += END
	go(buff);

def craft1(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Basic crafting 1)"
	buff = ''
	buff += focus                     #OPTIONS rtsp://192.168.56.1/xpAAAAAAAAAAAAAAAAA RTSP/1.0
	buff += ' '                       #CSeq: 1
	buff += 'rtsp://'                 #User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 1'
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);

def craft2(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Basic crafting 2)"
	buff = ''
	buff += focus                  #OPTIONS rtsp://192.168.56.1/xp RTSP/1.0
	buff += ' '                    #CSeq: 1
	buff += 'rtsp://'              #User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)AAAAAAAAAAAAAAAAAAAAAAAAA
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 1'
	buff += END
	buff += 'User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)'
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += END
	buff += "\n"
	go(buff);
def craft3(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Basic crafting 3)"
	buff = ''
	buff += focus                  #OPTIONS AAAAAAAAAAAAAAAAAAAAAA RTSP/1.0
	buff += ' '                    #CSeq: 1
	if msfpat == "ON":             #User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)         
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 1'
	buff += END
	buff += 'User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)'
	buff += END
	buff += "\n"
	go(buff);	

def craft4(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Basic crafting 4)"
	buff = ''
	buff += focus                  #OPTIONS rtsp://192.168.56.1/xp RTSP/1.0
	buff += ' '                    #CSeq: AAAAAAAAAAAAAAAAAAAAAAAAA
	buff += 'rtsp://'              #User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: '
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += END
	buff += 'User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)'
	buff += END
	buff += "\n"
	go(buff);


#This fumction will always accept Describe as focus parameter and Sequence parameter will be always 2
def craft5(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 1)"
	buff = ''
	buff += focus                     #DESCRIBE rtsp://192.168.56.1/xp RTSP/1.0
	buff += ' '                       #CSeq: 2
	buff += 'rtsp://'                 #Accept: application/sdpAAAAAAAAAAAAAAAAAAA
	buff += RHOST                     #User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 2'
	buff += END
	buff +='Accept: '
	buff += 'application/sdp'
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);

#SETUP rtsp://server.com:554/xp/trackID=0 RTSP/1.0
#CSeq: 3
#Transport: RTP/AVP;unicast;client_port=36142-36143
#User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)
def craft6(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 2)"
	buff = ''
	buff += focus                     
	buff += ' '                       
	buff += 'rtsp://'                 
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 3'
	buff += END
	buff += 'Transport: '
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += '/'
	buff += 'AVP;unicast;client_port=36142-36143'
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);

def craft7(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 3)"
	buff = ''
	buff += focus                      #Transport: RTP/AAAAAAAA;unicast;client_port=36142-36143
	buff += ' '                       
	buff += 'rtsp://'                 
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 3'
	buff += END
	buff += 'Transport: RTP/'
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += ';'
	buff += 'unicast;client_port=36142-36143'
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);
def craft8(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 4)"
	buff = ''                       #Transport: RTP/AVP;AAAAAAAAAAAAAAA;client_port=36142-36143
	buff += focus                     
	buff += ' '                       
	buff += 'rtsp://'                 
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 3'
	buff += END
	buff += 'Transport: RTP/AVP;'
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += ';client_port=36142-36143'
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);
def craft9(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 5)"
	buff = ''          #Transport: RTP/AVP;unicast;client_port=AAAAAAAAAAAAAAAAAAAAAAAAAA-36143
	buff += focus                     
	buff += ' '                       
	buff += 'rtsp://'                 
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 3'
	buff += END
	buff += 'Transport: RTP/AVP;unicast;client_port='
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += '-36143'
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);
def craft10(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 6)"
	buff = ''      #Transport: RTP/AVP;unicast;client_port=36142-AAAAAAAAAAAAAAAAAAAAAAAAAAA
	buff += focus                     
	buff += ' '                       
	buff += 'rtsp://'                 
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 3'
	buff += END
	buff += 'Transport: RTP/AVP;unicast;client_port=36142-'
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);
#GET_PARAMETER rtsp://server.com:554/xp RTSP/1.0
#CSeq: 6
#Session: e539b3f49ccf77ea
#User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)

def craft11(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 7)"
	buff = ''
	buff += focus                     
	buff += ' '                       
	buff += 'rtsp://'                 
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 6'
	buff += END
	buff += 'Session: '
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);
#TEARDOWN rtsp://server.com:554/xp RTSP/1.0
#CSeq: 7
#Session: e539b3f49ccf77ea
#User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)
def craft12(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 8)"
	buff = ''
	buff += focus                     
	buff += ' '                       
	buff += 'rtsp://'                
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 7'
	buff += END
	buff += 'Session: '
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);	
	
#PLAY rtsp://server.com:554/xp RTSP/1.0
#CSeq: 5
#Session: e539b3f49ccf77ea
#Range: npt=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)	
def craft13(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 8)"
	buff = ''
	buff += focus                     
	buff += ' '                       
	buff += 'rtsp://'                
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 7'
	buff += END
	buff += 'Session: '
	buff += SESSION
	buff += END
	buff += 'Range: npt='
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);	
#PLAY rtsp://server.com:554/xp RTSP/1.0
#CSeq: 5
#Session: e539b3f49ccf77ea
#Range: AAAAAAAAAAAAAAAAAAAAAAA=0.000-
#User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)	
def craft14(focus,size):
	print "[*]  -> Fuzzing ",focus,"Fuzzing size set to ",size," (Advanced crafting 8)"
	buff = ''
	buff += focus                     
	buff += ' '                       
	buff += 'rtsp://'                
	buff += RHOST
	buff += '/'
	buff += SERVERPATH
	buff += ' RTSP/1.0'
	buff += END
	buff += 'CSeq: 7'
	buff += END
	buff += 'Session: '
	buff += SESSION
	buff += END
	buff += 'Range: '
	if msfpat == "ON":
		buff += createpattern(size)
	else:                       
		buff += junk*int(size)
	buff += '=0.000-'
	buff += END
	buff += "User-Agent: VLC media player (LIVE555 Streaming Media v2010.02.10)"
	buff += END
	buff += "\n"
	go(buff);
#Clear the previous Log file
def clearlog():
	cl = open('LOG.TXT','w')
	cl.write("")
	cl.close()
#Append the buffer size in LOG.TXT
def bufflen(bl):
	bl = str(bl)
	f = open('LOG.TXT','w')
	f.write("[*]  Buffer Length :")
	f.write(bl)
	f.write("\nRequest :\n")
	f.close()

#Start Basic Crafting
def start():
	PARAMETERS = ['OPTIONS',        
					'DESCRIBE',
					'SETUP',
					'PLAY',
					'GET_PARAMETER',
					'TEARDOWN',
					'PAUSE']
	t = len(PARAMETERS)
	for i in range(0,t):
		line = PARAMETERS[i]
		STS = STARTSIZE
		EDS = ENDSIZE
		STEP = STEPSIZE
		div = EDS/STEP
		line = line.replace("\n","")
		for i in range(0,div):
			bufflen(STS)
			craft0(line,STS)
			craft1(line,STS)
			craft2(line,STS)
			craft3(line,STS)
			craft4(line,STS)
			time.sleep(DELAY)
			STS = STS+STEP
#Start Advanced Crafting
def startadvcraft():	
	STS = STARTSIZE
	EDS = ENDSIZE
	STEP = STEPSIZE
	div = EDS/STEP
	for j in range(0,div):
		STEP = STEPSIZE
		bufflen(STS)
		craft5("DESCRIBE",STS)
		STS = STS+STEP
	STS = STARTSIZE
	STEP = STEPSIZE
	for k in range(0,div):
		bufflen(STS)
		craft6("SETUP",STS)
		craft7("SETUP",STS)
		craft8("SETUP",STS)
		craft9("SETUP",STS)
		craft10("SETUP",STS)
		STS = STS+STEP
	STS = STARTSIZE
	STEP = STEPSIZE
	for l in range(0,div):
		STEP = STEPSIZE
		bufflen(STS)
		craft11("GET_PARAMETER",STS)
		STS = STS+STEP
	STS = STARTSIZE
	STEP = STEPSIZE
	for m in range(0,div):
		STEP = STEPSIZE
		bufflen(STS)
		craft12("TEARDOWN",STS)
		STS = STS+STEP
	STS = STARTSIZE
	STEP = STEPSIZE
	for n in range(0,div):
		STEP = STEPSIZE
		bufflen(STS)
		craft13("PLAY",STS)
		STS = STS+STEP
	STS = STARTSIZE
	STEP = STEPSIZE
	for o in range(0,div):
		STEP = STEPSIZE
		bufflen(STS)
		craft14("PLAY",STS)
		STS = STS+STEP

def createpattern(length):
	length = int(length)
	data = ''.join(tuple(islice(chain.from_iterable(product(string.ascii_uppercase, string.ascii_lowercase, string.digits)), length)))
	return data

#Global Start
config = ConfigParser()
config.read('rtsp.conf')
RHOST = config.get('rtspfuzz', 'RHOST')
RPORT = config.get('rtspfuzz', 'RPORT')
STARTSIZE = config.get('rtspfuzz', 'STARTSIZE')
ENDSIZE = config.get('rtspfuzz', 'ENDSIZE')
STEPSIZE = config.get('rtspfuzz', 'STEPSIZE')
STOPAFTER = config.get('rtspfuzz', 'STOPAFTER')
DELAY = config.get('rtspfuzz', 'DELAY')
SERVERPATH = config.get('rtspfuzz', 'SERVERPATH')
SESSION = config.get('rtspfuzz', 'SESSION')
junk = config.get('rtspfuzz', 'JUNK')
msfpat = config.get('StreamFuzz', 'MSFPATTERN')

#Little Bit Typecasting
RPORT=int(RPORT)
STARTSIZE=int(STARTSIZE)
ENDSIZE=int(ENDSIZE)
STEPSIZE=int(STEPSIZE)
STOPAFTER=int(STOPAFTER)
DELAY=int(DELAY)
print "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]"
print "[*]                      WELCOME                   [*]"
print "[*]                StreamFuzzer version 02            [*]"
print "[*]                rtsp Protocol fuzzer            [*]"
print "[*]               Author :Rabimba                  [*]"
print "[*]           Site:http://www.rabimba.com/         [*]"
print "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]"
print "[*]              Your Preferences                     "
print "[*] Target Host :" ,RHOST,"on PORT",RPORT
print "[*] Start Size :",STARTSIZE
print "[*] End Size :",ENDSIZE
print "[*] Step Size :",STEPSIZE
print "[*] Time Delay between two requests :",DELAY,"Sec"
print "[*] Server path rtsp://",RHOST,"/",SERVERPATH
print "[*] Session ID to use when required :",SESSION
print "[*] Fuzzing with Metasploit Pattern :",msfpat
print "[*]"
print "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]"
raw_input("[*] If above information are correct Press Enter \nto start fuzzing if not then re-edit the rtsp.conf file _")
if msfpat == "ON":
	print "[*] You are going to start fuzzing with Metasploit Pattern"
	print "[*] This fuzzing process may take some extra time"
	q = raw_input("[*] Are you sure(y/n)??")
	if q == "n":
		print "[*] Turning off Metasploit Pattern feature.."
		msfpat = "OFF"
clearlog();
start();
print "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]"
print "[*]                  Starting Advanced fuzzing with Specially Crafted requests               [*]"
print "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]"
startadvcraft();
print "[*] To see last successful request go to LOG.TXT file"
print "[*] Exiting."
