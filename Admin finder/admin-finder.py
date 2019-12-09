import requests,sys,os
import platform
import urllib
import time
from colorama import init
init()
from colorama import Fore, Back, Style
start_time = time.time()
a = platform.system()
print (Fore.BLUE + '################### ID T.ME @NASHENAS_TM ####################')
time.sleep(2)
print (Fore.BLUE + '################### NAME IS : MEHRSHAD   ####################')
time.sleep(2)
print (Fore.BLUE + 'MY SYSTEM : '+a )
time.sleep(2)


def scaner(url):
	try:
		r = requests.get(url,allow_redirects=False)
		print (Fore.RED + '[-]'+url)
		if r.status_code == 200:
			print  (Fore.GREEN + '[+]'+url+' ok panel admin')
			time.sleep(1)

	except Exception as e:
		print e
		print (Fore.RED  + "not foun link")


def main():
	if(len(sys.argv) == 2):
		url = sys.argv[1].strip()
		if not url.startswith('http://') or not url.startswith('https://'):
			print (Fore.RED + 'Either use http:// or https://')
		if(not url.endswith('/')):
			url += '/' 
		if not os.path.exists('pass.txt'):
			print "File pass.txt  not  FOUND "
			sys.exit()

		print (Fore.GREEN + '[+] Please wait a moment!!! ')
		f = open('pass.txt','r')
		for line in f.read().splitlines():
			line2 = line.strip()
			if line2 == '':
				continue
			line2 = line2.replace('//','/')
			if(line2.find('.') == -1):
				line2+='/'
			url2 = url+line2
			scaner(url2)
		end_time = time.time() - start_time
		print 'total scan time :  ',str(end_time)
	
	else:
		usage()

def usage():
	print "admin finder v.1.0"
	time.sleep(2)
	print "python admin-finder.py url"

try:

	if __name__ == '__main__':
		main()
except (KeyboardInterrupt, SystemExit):
	pass