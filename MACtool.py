#! /usr/bin/env python
import random, platform, subprocess, sys, os,time
	
def isLinux():
	"""Verifies if the current platform is Linux"""
	OS = platform.system()
	return OS == 'Linux'
	
def isOSx():
	"""Verifies if the current platform is OSx"""
	OS = platform.system()
	return OS == 'Darwin'

def isRoot():
	"""Verifies if the current user is root"""
	return os.getuid() & os.getgid() == 0

def setLinuxMAC(device,mac):
	"""Sets the new mac for device, in a Linux system"""
	subprocess.check_call(["ifconfig","%s" % device, "up"])
	subprocess.check_call(["ifconfig","%s" % device, "hw", "ether","%s" % mac])

def setOSxMAC(device,mac):
	"""Sets the new mac for device, in a Darwin system"""
	subprocess.check_call(["ifconfig","%s" % device,"up"])
	subprocess.check_call(["ifconfig","%s" % device,"lladdr","%s" % mac])	
	
def randomMacAddress(prefix):
	"""Randomly generates the missing bytes of the MAC address started by prefix"""
	for _ in xrange(6-len(prefix)):
		prefix.append(random.randint(0x00, 0x7f))
	return ':'.join('%02x' % x for x in prefix)

def checkMac(device,mac):
	"""Returns true if the current device mac address matches the mac given as input"""
	local = ""        
	output = subprocess.Popen(["ifconfig", "%s" % device], stdout=subprocess.PIPE).communicate()[0]
	index = output.find('ether') + len('ether ')
	localAddr = output[index:index+17] 
	return mac == localAddr 

def parsePrefix(prefix):
	"""Parses user-define prefix, ex: de:ad:be:ef"""
	tempList = []
	prefList = prefix.split(":")
	for pair in prefList:     
		tempList.append(int(pair,16))
	return tempList
	
def printUsage():
	pass		

if __name__ == '__main__':
	if len(sys.argv) < 2:
		printUsage()
		sys.exit(0)
	   
	device = sys.argv[1]
 	
	if not isRoot():
		print "[-] Your have to be root"
		sys.exit(0)

	try:
		prefix = sys.argv[2]
		prefix = parsePrefix(prefix)
	except IndexError:
		prefix = [0x00]
    
	mac = randomMacAddress(prefix)
	print "[*] Generated MAC address: %s for device %s" % (mac,device)

	# Call the setMAC for either Linux or OSx
	if isOSx():									 
		setOSxMAC(device,mac)
	elif isLinux():
		setOSxMAC(device,mac)		   

	# Verify if the interface has the new mac address set	
	if checkMac(device,mac):
		print "[*] Done"
	else:
		print "[-] Something went wrong"
	