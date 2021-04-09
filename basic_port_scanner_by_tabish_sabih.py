#!/usr/bin/python3

from socket import * #connection qaaim karne k liye
import optparse #is library mein hmen command line programs banane mein help mil jaati hai
from threading import * #taakay ek waqt mein multiple ports scan horahe hain rather than k one by one

def connScan(target_host, connection_type, target_port,):

	if connection_type == "tcp":
		try:
			sock = socket(AF_INET, SOCK_STREAM)  # Connection type TCP
			#sock.setdefaulttimeout(1)
			sock.connect((target_host, target_port))
			print(f"\n[+] TCP port {target_port} is Open")
		except:
			print(f"\n[-] TCP port {target_port} is Closed")
		finally:
			sock.close()

	else:
		try:
			sock = socket(AF_INET, SOCK_DGRAM)  # Connection type UDP
			#sock.setdefaulttimeout(1)
			sock.connect((target_host, target_port))
			print(f"\n[+] UDP port {target_port} is Open")
		except:
			print(f"\n[-] UDP port {target_port} is Closed")
		finally:
			sock.close()


def portScan(target_host , target_ports):
	try:
		target_ip = gethostbyname(target_host) #hostname ko ip address mein resolve karne k liye
	except:
		print(f"\nUnknown Host {target_host}")
	try:
		target_name = gethostbyaddr(target_ip) #ip address ko hostname mein resolve karne k liye
		print(f"\n[+] Scan Results For :{target_name[0]}\n")
	except:
		print(f"\n[-] Scan Results For : {target_ip}\n")

	setdefaulttimeout(1) #1 second ka default timeout
	connection_type = input("Would you like to scan open ports for TCP or UDP? ").lower().strip()

	if connection_type == "tcp" or connection_type == "udp": #to make sure k protocol tcp ya udp hi ho
		for target_port in target_ports:  # target ports k har har port pe connScan ka function threading functionality k saath.
			t = Thread(target=connScan, args=(target_host, connection_type, int(target_port)))
			t.start()

	else:
		print("Incorrect protocol. You had to choose either TCP or UDP Terminating Program.")
		exit(1)

def main():
	parser = optparse.OptionParser('Usage of Program : ' + ' -H or --host <target host> -p or --port <target port>')
	parser.add_option('-H', '--host', dest = 'target_host' , type='string', help='specify target Host')
	parser.add_option('-p', '--port', dest = 'target_port' , type='string', help='specify target ports separated by comma')
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
