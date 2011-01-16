# MAC Address Generator & Changer for Linux and OS X

This application generates and changes the interface MAC Address. There is the possibility of generating a completely random MAC Address:
	
	husk:py-MacTool hip$ sudo python MACtool.py en0
	[*] Generated MAC address: 00:4a:5d:44:70:0f for device en0
	[*] Done
	
But you can also choose a Manufacturer from which the MAC Address should be generated:

	husk:py-MacTool hip$ sudo python MACtool.py -m Apple en0
	[+] Found Manufacturer List: manufacturer_list.txt
	[*] Generated MAC address: 00:26:08:0f:09:1a for device en0
	[*] Done
	husk:py-MacTool hip$ sudo python MACtool.py -m Intel en0
	[+] Found Manufacturer List: manufacturer_list.txt
	[*] Generated MAC address: 00:02:b3:4f:6c:0c for device en0
	[*] Done
	husk:py-MacTool hip$ sudo python MACtool.py -m FAKE en0
	[+] Found Manufacturer List: manufacturer_list.txt
	[-] Manufacturer: FAKE not found.
	
Finally, you can also choose your own MAC Address, or just the prefix (in this example we are setting the DE:AD:BE:EF prefix). The application will generate the remainder of the MAC Address randomly.
	
	husk:py-MacTool hip$ sudo python MACtool.py -p de:ad:be:ef en0
	[*] Generated MAC address: de:ad:be:ef:55:0e for device en0
	[*] Done

This Application was tested on Ubuntu 10.10 and OS X 10.6+.
	
	