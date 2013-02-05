#! /usr/bin/env python
import random, platform, subprocess, sys, os, time, getopt
import getMAN

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
	output = subprocess.Popen(["ifconfig", "%s" % device], stdout=subprocess.PIPE).communicate()[0]
	index = output.find('ether') + len('ether ')
	localAddr = output[index:index+17] 
	return mac == localAddr 

def parsePrefix(prefix):
	"""Parses user-define prefix, ex: de:ad:be:ef"""
	tempList = []
	prefList = prefix.split(":")
	try:
		for pair in prefList:	  
			tempList.append(int(pair,16))
	except:
		print "[-] Unable to parse prefix %s. Correct format: 00:00:00" % prefix
		sys.exit(2)
	return tempList
	
def printUsage():
	print "Usage: %s INTERFACE <-m MANUFACTURER> <-p PREFIX>" % sys.argv[0]
	print "Example: %s eth0 -m Apple" % sys.argv[0]
	print "Example: %s eth0 -p de:ad:be:ef" % sys.argv[0]
			

if __name__ == '__main__':
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'm:p:')
	except getopt.GetoptError, err:
		print str(err) 
		printUsage()
		sys.exit(2)
	
	if len(args) < 1:
		printUsage()
		sys.exit(2)
	
	prefix = None
	for o, a in opts:
		if o in ("-m","--manufacturer"):
			manu = getMAN.getMACfMAN(a)
			if len(manu) == 0:
				print "[-] Manufacturer: %s not found." % a
			prefix = parsePrefix(random.choice(manu))
		elif o in ("-p","--prefix"):
			prefix = a
			prefix = parsePrefix(a)
			
	if not prefix:
		prefix = [0x00]	   
	
	device = args[0]
	
	if not isRoot():
		print "[-] Your have to be root"
		sys.exit(0)
	
	mac = randomMacAddress(prefix)
	print "[*] Generated MAC address: %s for device %s" % (mac,device)

	# Call the setMAC for either Linux or OSx
	try:
		if isOSx():									 
			setOSxMAC(device,mac)
		elif isLinux():
			setLinuxMAC(device,mac)		   
	except:
		print "[-] Unable to set MAC for device: %s. Does this device exist?" % device
		sys.exit(2)
	# Verify if the interface has the new mac address set	
	if checkMac(device,mac):
		print "[*] Done"
	else:
		print "[-] Something went wrong"
	