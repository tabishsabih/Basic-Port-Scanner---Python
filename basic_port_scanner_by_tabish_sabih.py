#!/usr/bin/python3

from socket import * #connection qaaim karne k liye
import optparse #is library mein hmen command line programs banane mein help mil jaati hai
from threading import * #taakay ek waqt mein multiple ports scan horahe hain rather than k one by one

def connScan(target_host, target_port):
	try:
		sock = socket(AF_INET, SOCK_STREAM) #Connection type TCP
		sock.connect((target_host,target_port))
		print(f"[+] {target_port} tcp Open")
	except:
		print(f"[-] {target_port} tcp Closed")
	finally:
		sock.close()

def portScan(target_host , target_ports):
	try:
		target_ip = gethostbyname(target_host) #hostname ko ip address mein resolve karne k liye
	except:
		print(f"Unknown Host {target_host}")
	try:
		target_name = gethostbyaddr(target_ip) #ip address ko hostname mein resolve karne k liye
		print(f"[+] Scan Results For :{target_name[0]}")
	except:
		print(f"[-] Scan Results For : {target_ip}")
	setdefaulttimeout(1) #1 second ka default timeout

	for target_port in target_ports: #target ports k har har port pe connScan ka function threading functionality k saath.
		t = Thread(target=connScan , args=(target_host , int(target_port)))
		t.start()


def main():
	parser = optparse.OptionParser('Usage of Program : ' + ' -H or --host <target host> -p or --port <target port>')
	parser.add_option('-H', '--host', dest = 'target_host' , type='string', help='specify target Host')
	parser.add_option('-p', '--port', dest = 'target_port' , type='string', help='specify target ports seperated by comma')
	(options,args) = parser.parse_args()
	target_host = options.target_host
	target_ports = str(options.target_port).split(',') #commas ki base pe parsing hogi taakay commas k zariye se ports specify kiye jasaken.

	#agar ghalat command line argument insert ki jae tou dobara instructions print karani hain aur program terminate kardena hai.
	if (target_host == None) | (target_ports[0]== None):
		print(parser.usage)
		exit(0)
	portScan(target_host,target_ports)

#taakay script directly run kare
if __name__== '__main__':
	main()