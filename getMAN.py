#! /usr/bin/env python
import sys, os, urllib2

MANSOURCE = "http://anonsvn.wireshark.org/wireshark/trunk/manuf"
MANFILENAME= "manufacturer_list.txt"

def getManList(manfile,source=MANSOURCE):
    if not os.path.isfile("./"+manfile):
        try:
            print "[-] Manufacturer list not found. Retreiving it from: %s" % source
            u = urllib2.urlopen(source)
            localFile = open(manfile, 'wb')
            localFile.write(u.read())
            localFile.close()
        except Exception:
            print "[-] Unable to retreive manufacturer list from: %s" % source
            sys.exit(0)
    
def getMACfMAN(manufacturer,manfile=MANFILENAME):
    outList = []
    getManList(manfile)
    print "[+] Found Manufacturer List: %s" % manfile
    f = open(manfile,"r")
    for line in f:
        try:
            currentMAC = line.split()[0]
            currentMAN = line.split()[1]
            if manufacturer == currentMAN and len(currentMAC)<17 and len(currentMAC) > 1:
                outList.append(line.split()[0])
        except IndexError:
            pass
    f.close()
    return outList
    
def printUsage():
    pass        

if __name__ == '__main__':
    if len(sys.argv) < 2:
        printUsage()
        sys.exit(0)
       
    manufacturer = sys.argv[1]
    
    macs = getMACfMAN(manufacturer)
    
    if len(macs) > 0: 
        print macs
    else:
        print "[-] Manufacturer: %s, not found." % manufacturer
